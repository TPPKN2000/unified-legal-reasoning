"""§4.2 fine-tuning approach: learn Logit = Agg(O(Encode(F,T,H,O))). Needs torch + transformers + peft."""
import argparse
import json

from _common import ROOT, load_config

from ulr.scoring import LogitScorer, evaluate_scorer, train_scorer
from ulr.synthetic import load_jsonl

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--config", default=str(ROOT / "configs" / "colab_t4.yaml"))
p.add_argument("--data", default=str(ROOT / "data" / "logit"))
p.add_argument("--epochs", type=int, default=None)
p.add_argument("--out", default=None)
args = p.parse_args()

cfg = load_config(args.config)["scorer"]
train, ev = load_jsonl(f"{args.data}/train.jsonl"), load_jsonl(f"{args.data}/eval.jsonl")
scorer = LogitScorer(base_model_id=cfg["base_model_id"], agg=cfg.get("agg", "last"), dtype=cfg.get("dtype", "float32"))
print("before:", evaluate_scorer(scorer, ev))
train_scorer(scorer, train, ev, epochs=args.epochs or cfg.get("epochs", 8))
print("after :", evaluate_scorer(scorer, ev))
out = args.out or cfg["out_dir"]
scorer.save(out)
print("saved scorer to", out)
