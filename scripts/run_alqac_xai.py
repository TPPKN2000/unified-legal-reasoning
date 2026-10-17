"""ALQAC explainability experiment (outcome given -> abductive explanation -> rule-based check). Resumable."""
import argparse

from _common import ROOT, load_config

from ulr.alqac.laws import LawIndex, LawRetriever, load_aliases
from ulr.alqac.report import write_report
from ulr.alqac.schema import load_cases, load_corpus
from ulr.alqac.xai import XAIConfig, run_all
from ulr.alqac.xai_judge import EmbeddingScorer, XAIJudge
from ulr.llm import build_backend
from ulr.reasoners import AbductiveReasoner, RuleBasedReasoner

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--config", default=str(ROOT / "configs" / "alqac_xai.yaml"))
p.add_argument("--backend", choices=["config", "mock"], default="config")
p.add_argument("--theory-source", choices=["oracle", "rag"], default=None)
p.add_argument("--decontaminate", action="store_true", help="remove case_fact sentences that duplicate court reasoning")
p.add_argument("--limit", type=int, default=None, help="only the first N cases")
p.add_argument("--no-baseline", action="store_true")
p.add_argument("--llm-judge", action="store_true", help="use alqac.llm_judge from the config (explanation rubric)")
p.add_argument("--embed", action="store_true", help="use alqac.embed_model from the config")
args = p.parse_args()

cfgy = load_config(args.config)
ac = cfgy["alqac"]
cfg = XAIConfig(
    theory_source=args.theory_source or ac.get("theory_source", "oracle"), top_k_hypotheses=ac.get("top_k_hypotheses", 3),
    max_fact_chars=ac.get("max_fact_chars", 16000), decontaminate=args.decontaminate or ac.get("decontaminate", False),
    baseline=not args.no_baseline and ac.get("baseline", True), system=ac.get("system"),
    max_new_tokens=cfgy["llm"].get("max_new_tokens", 900) if args.backend == "config" else 900,
    out_dir=ac.get("out_dir", "outputs/xai"))

cases = load_cases(ROOT / ac["cases"])[: args.limit]
arts = load_corpus(ROOT / ac["corpus"])
index = LawIndex(arts, load_aliases(ROOT / ac["law_aliases"]) if ac.get("law_aliases") else {})
retriever = LawRetriever(arts) if arts else None

llm = build_backend({"type": "mock"} if args.backend == "mock" else cfgy["llm"])
gen = {"max_new_tokens": cfg.max_new_tokens}
if cfg.system:
    gen["system"] = cfg.system
rule = RuleBasedReasoner(llm, classifier_fallback=False, gen=gen)
abd = AbductiveReasoner(llm, gen=gen)

judge = judge_llm = embedder = None
if args.llm_judge:
    spec = ac.get("llm_judge") or ({"type": "mock", "name": "mock-judge"} if args.backend == "mock" else None)
    if spec is None:
        raise SystemExit("set alqac.llm_judge in the config to use --llm-judge")
    judge_llm = build_backend(spec)
    judge = XAIJudge(judge_llm)
if args.embed:
    embedder = EmbeddingScorer(ac["embed_model"])

recs = run_all(cases, rule, abd, cfg, index, retriever, judge, embedder)
print(write_report(recs, cfg.out_dir, cfg.run_name))
print(f"\nrecords + report in {cfg.out_dir}/{cfg.run_name}/")
llm.close()
if judge_llm:
    judge_llm.close()
