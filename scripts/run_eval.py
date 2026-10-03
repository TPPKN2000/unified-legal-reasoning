"""§4.4 evaluation: generate -> LLM-as-a-Judge -> Fig.4 / Fig.5. Resumable (re-run the same command)."""
import argparse

from _common import ROOT, load_config

from ulr.evaluation import build_tasks
from ulr.evaluation.report import make_report
from ulr.evaluation.runner import generate_all, judge_all

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--config", default=str(ROOT / "configs" / "colab_t4.yaml"))
p.add_argument("--stage", choices=["all", "generate", "judge", "report"], default="all")
args = p.parse_args()

ev = load_config(args.config)["evaluation"]
tasks = build_tasks()
out = ev["out_dir"]
if args.stage in ("all", "generate"):
    generate_all(ev["candidates"], tasks, out)
if args.stage in ("all", "judge"):
    judge_all(ev["judges"], tasks, out)
if args.stage in ("all", "report"):
    print(make_report(out, {t.id: t.mode for t in tasks}))
    print(f"\nfigures + results.md in {out}/")
