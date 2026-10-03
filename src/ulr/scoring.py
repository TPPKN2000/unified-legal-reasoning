"""Fine-tuned LLM scorer (paper §4.2, third approach).

    S     = Encode(F, T, H, O)
    Logit = Agg(O(S))      O(S): final-layer output for the input sequence

Implementation: a small causal-LM backbone (final-layer hidden states) + LoRA adapters; `Agg` pools the
final-layer activations (last token | mean | max) and a linear head maps them to ONE scalar logit that
expresses how plausible the relation between Fact, Theory, Hypothesis and Outcome is.
A higher logit = stronger relation; a lower logit = weaker relation.
Requires: torch, transformers, peft  (imported at module import time -> import lazily).
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

from .components import Fact, Hypothesis, Outcome, Theory
from .encoding import encode


def aggregate(hidden: torch.Tensor, mask: torch.Tensor, how: str) -> torch.Tensor:
    """Agg over final-layer activations. hidden [B,L,D], mask [B,L] (right padded)."""
    if how == "last":
        idx = mask.sum(1).long() - 1
        return hidden[torch.arange(hidden.size(0), device=hidden.device), idx]
    m = mask.unsqueeze(-1).to(hidden.dtype)
    if how == "mean":
        return (hidden * m).sum(1) / m.sum(1).clamp(min=1)
    if how == "max":
        return hidden.masked_fill(m == 0, float("-inf")).max(1).values
    raise ValueError(f"unknown agg: {how}")


class LogitScorer(nn.Module):
    def __init__(
        self,
        base_model_id: str = "Qwen/Qwen2.5-0.5B-Instruct",
        agg: str = "last",
        lora_r: int = 8,
        lora_alpha: int = 16,
        lora_dropout: float = 0.05,
        dtype: str = "float32",
        max_length: int = 512,
        adapter_dir: Optional[str] = None,
        device: Optional[str] = None,
    ):
        super().__init__()
        from peft import LoraConfig, PeftModel, TaskType, get_peft_model

        self.cfg = dict(base_model_id=base_model_id, agg=agg, lora_r=lora_r, lora_alpha=lora_alpha,
                        lora_dropout=lora_dropout, dtype=dtype, max_length=max_length)
        self.agg, self.max_length = agg, max_length
        self.tok = AutoTokenizer.from_pretrained(base_model_id)
        self.tok.padding_side = "right"
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        base = AutoModel.from_pretrained(base_model_id, torch_dtype=getattr(torch, dtype))
        if adapter_dir:
            self.encoder = PeftModel.from_pretrained(base, adapter_dir, is_trainable=False)
        else:
            lcfg = LoraConfig(
                r=lora_r, lora_alpha=lora_alpha, lora_dropout=lora_dropout, task_type=TaskType.FEATURE_EXTRACTION,
                target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
            )
            self.encoder = get_peft_model(base, lcfg)
        self.head = nn.Linear(base.config.hidden_size, 1)
        self.device_ = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        self.to(self.device_)

    # ----- forward -----
    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        h = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        pooled = aggregate(h.float(), attention_mask, self.agg)
        return self.head(pooled).squeeze(-1)  # [B] logits

    def _batch(self, texts: List[str]):
        enc = self.tok(texts, return_tensors="pt", padding=True, truncation=True, max_length=self.max_length)
        return enc["input_ids"].to(self.device_), enc["attention_mask"].to(self.device_)

    # ----- inference API used by RuleBasedReasoner -----
    @torch.no_grad()
    def score_texts(self, texts: Sequence[str], batch_size: int = 8) -> List[float]:
        self.eval()
        out: List[float] = []
        for i in range(0, len(texts), batch_size):
            ids, mask = self._batch(list(texts[i:i + batch_size]))
            out += self(ids, mask).tolist()
        return out

    def score(self, fact: Fact, theory: Theory, hypotheses: Sequence[Hypothesis], outcome: Outcome) -> float:
        return self.score_texts([encode(fact, theory, hypotheses, outcome)])[0]

    def prob(self, *args) -> float:
        return 1 / (1 + math.exp(-self.score(*args)))

    # ----- persistence -----
    def save(self, out_dir: str) -> None:
        p = Path(out_dir)
        p.mkdir(parents=True, exist_ok=True)
        self.encoder.save_pretrained(str(p))
        torch.save(self.head.state_dict(), p / "head.pt")
        (p / "scorer_config.json").write_text(json.dumps(self.cfg, indent=2))

    @classmethod
    def load(cls, out_dir: str, device: Optional[str] = None) -> "LogitScorer":
        p = Path(out_dir)
        cfg = json.loads((p / "scorer_config.json").read_text())
        obj = cls(adapter_dir=str(p), device=device, **cfg)
        obj.head.load_state_dict(torch.load(p / "head.pt", map_location=obj.device_))
        return obj


# ----------------------------------------------------------------------------------------------
def expected_calibration_error(probs: Sequence[float], labels: Sequence[int], bins: int = 10) -> float:
    n, ece = len(probs), 0.0
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        idx = [i for i, p in enumerate(probs) if (lo <= p < hi) or (b == bins - 1 and p == 1.0)]
        if idx:
            conf = sum(probs[i] for i in idx) / len(idx)
            acc = sum(labels[i] for i in idx) / len(idx)
            ece += len(idx) / n * abs(conf - acc)
    return ece


def evaluate_scorer(scorer: LogitScorer, records: List[Dict]) -> Dict[str, float]:
    from .synthetic import record_to_text

    logits = scorer.score_texts([record_to_text(r) for r in records])
    probs = [1 / (1 + math.exp(-x)) for x in logits]
    labels = [r["label"] for r in records]
    acc = sum((p > 0.5) == bool(y) for p, y in zip(probs, labels)) / max(1, len(labels))
    return {"accuracy": acc, "ece": expected_calibration_error(probs, labels), "n": len(labels)}


def train_scorer(
    scorer: LogitScorer,
    train: List[Dict],
    eval_: Optional[List[Dict]] = None,
    epochs: int = 8,
    lr: float = 2e-4,
    batch_size: int = 4,
    seed: int = 0,
    log=print,
) -> None:
    """Minimise the gap between the logit prediction and the ground-truth plausibility label (BCE)."""
    import random

    from .synthetic import record_to_text

    random.seed(seed)
    torch.manual_seed(seed)
    params = [p for p in scorer.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=lr, weight_decay=0.01)
    lossf = nn.BCEWithLogitsLoss()
    data = [(record_to_text(r), float(r["label"])) for r in train]
    for ep in range(1, epochs + 1):
        scorer.train()
        random.shuffle(data)
        total = 0.0
        for i in range(0, len(data), batch_size):
            chunk = data[i:i + batch_size]
            ids, mask = scorer._batch([t for t, _ in chunk])
            y = torch.tensor([l for _, l in chunk], device=scorer.device_)
            loss = lossf(scorer(ids, mask), y)
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(params, 1.0)
            opt.step()
            total += loss.item() * len(chunk)
        msg = f"epoch {ep}/{epochs} loss={total / len(data):.4f}"
        if eval_:
            m = evaluate_scorer(scorer, eval_)
            msg += f" | eval acc={m['accuracy']:.2f} ece={m['ece']:.2f}"
        log(msg)
