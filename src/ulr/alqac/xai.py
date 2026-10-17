"""ALQAC explainability experiment on top of the unified framework (civil-law style, OUTCOME GIVEN):

    Fact (case_fact) + Theory (provisions) + Outcome (verdict_label, given)
        --abductive-->  Hypotheses (candidate explanations)
        --judge-->      top-k accepted
        --rule-based--> reasoning with F,T,H  (explanation text + 'does it lead back to the outcome?')

Nothing here optimises or reports outcome-prediction accuracy as a headline."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..components import Hypothesis
from ..judges import JudgeDecision
from ..reasoners import AbductiveReasoner, RuleBasedReasoner
from . import metrics as M
from .adapter import build_fact, build_issue, build_outcome, build_theory, clean_query
from .laws import LawIndex, LawRetriever
from .schema import AlqacCase
from .xai_judge import EmbeddingScorer, XAIJudge


@dataclass
class XAIConfig:
    theory_source: str = "oracle"  # oracle | rag
    top_k_hypotheses: int = 3
    max_fact_chars: int = 16000
    decontaminate: bool = False
    baseline: bool = True  # also run rule-based F,T without hypotheses (reference for the 'lift')
    rag_k: int = 5
    system: Optional[str] = "Bạn là chuyên gia pháp lý Việt Nam. Hãy lập luận chặt chẽ và trả lời bằng tiếng Việt."
    max_new_tokens: int = 900
    out_dir: str = "outputs/xai"
    extra: Dict[str, Any] = field(default_factory=dict)

    @property
    def run_name(self) -> str:
        return self.theory_source + ("_decon" if self.decontaminate else "")


class TopKJudge:
    """Batch-experiment judge: accepts the first k candidate hypotheses (the explanation is evaluated, not selected)."""

    def __init__(self, k: int):
        self.k = k

    def decide(self, candidates, **_):
        return JudgeDecision(accepted=list(candidates[: self.k]), note=f"top-{self.k}")


def run_case(case: AlqacCase, rule: RuleBasedReasoner, abd: AbductiveReasoner, cfg: XAIConfig,
             index: Optional[LawIndex], retriever: Optional[LawRetriever],
             xai_judge: Optional[XAIJudge] = None, embedder: Optional[EmbeddingScorer] = None) -> Dict[str, Any]:
    t0 = time.time()
    issue = build_issue(case)
    gold = build_outcome(case, issue)  # GIVEN to the model
    fact, fmeta = build_fact(case, cfg.max_fact_chars, cfg.decontaminate)
    theory, tmeta = build_theory(case, cfg.theory_source, index, retriever, fact, cfg.rag_k)

    ab = abd.run(fact, theory, gold)  # abductive: F,T,O -> H
    dec = TopKJudge(cfg.top_k_hypotheses).decide(ab.hypotheses)
    accepted: List[Hypothesis] = dec.accepted
    rr = rule.run(fact, theory, issue, accepted)  # rule-based: F,T,H
    pred_h = M.classify_label_vi(rr.response)
    base_resp, pred_0 = None, None
    if cfg.baseline:
        r0 = rule.run(fact, theory, issue)
        base_resp, pred_0 = r0.response, M.classify_label_vi(r0.response)

    hyp_text = "\n".join(h.statement for h in accepted)
    explanation = (hyp_text + "\n" + rr.response).strip()
    sources = [case.case_fact, case.case_query, theory.render()]
    gold_arts = {p.article for p in case.provisions if p.article is not None}
    cited = M.cited_articles(explanation)
    given_arts = M.cited_articles(theory.render())
    rl = M.rouge_l(case.reference_reasoning, explanation)
    cov_full = M.point_coverage(explanation, case.reference_reasoning)
    cov_hyp = M.point_coverage(hyp_text, case.reference_reasoning)
    metrics: Dict[str, Any] = {
        "citation": M.prf(cited, gold_arts),
        "ungiven_citation_rate": (len(cited - given_arts) / len(cited)) if cited and given_arts else None,
        "rouge_l_vs_court": rl,
        "coverage_full": cov_full,
        "coverage_hyp_only": cov_hyp,
        "unsupported_numbers": M.unsupported_numbers(explanation, sources),
        # explanation <-> outcome consistency (NOT prediction accuracy: the outcome was given to the abductive step)
        "consistency_with_h": (pred_h == case.verdict_label) if pred_h else None,
        "consistency_baseline": (pred_0 == case.verdict_label) if pred_0 else None,
        "n_hypotheses": len(accepted),
        "explanation_chars": len(explanation),
    }
    if embedder is not None:
        metrics["embedding_coverage"] = embedder.coverage(M.sentences(case.reference_reasoning, 8), M.sentences(explanation, 4))
    if xai_judge is not None:
        metrics["llm_judge"] = xai_judge.score("\n".join(fact.statements), gold.text, case.reference_reasoning, explanation)
    return {
        "case_id": case.case_id, "run": cfg.run_name, "given_outcome": case.verdict_label, "given_outcome_text": gold.text,
        "fact_meta": fmeta, "theory_meta": tmeta,
        "leakage": M.leakage(case.case_fact, case.reference_reasoning),
        "abductive": {"prompt": ab.prompt, "response": ab.response, "hypotheses": [h.statement for h in ab.hypotheses]},
        "accepted": [h.statement for h in accepted],
        "rule_with_h": {"prompt": rr.prompt, "response": rr.response, "label": pred_h},
        "rule_baseline": {"response": base_resp, "label": pred_0},
        "metrics": metrics, "seconds": round(time.time() - t0, 1),
    }


def run_all(cases: List[AlqacCase], rule, abd, cfg: XAIConfig, index=None, retriever=None, xai_judge=None,
            embedder=None, log=print) -> List[Dict[str, Any]]:
    """Resumable: one JSON line per case in <out_dir>/<run>/records.jsonl (re-run the same command after an interruption)."""
    out = Path(cfg.out_dir) / cfg.run_name
    out.mkdir(parents=True, exist_ok=True)
    path = out / "records.jsonl"
    done = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                done[r["case_id"]] = r
    for c in cases:
        if c.case_id in done:
            log(f"[xai] {c.case_id}: already done")
            continue
        log(f"[xai] {c.case_id} ({c.verdict_label}) ...")
        rec = run_case(c, rule, abd, cfg, index, retriever, xai_judge, embedder)
        done[c.case_id] = rec
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return [done[c.case_id] for c in cases if c.case_id in done]
