import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))  # allow running without `pip install -e .`

from ulr.runtime import load_config  # noqa: E402


def base_parser(desc: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=desc)
    p.add_argument("--config", default=str(ROOT / "configs" / "colab_t4.yaml"))
    p.add_argument("--backend", choices=["config", "mock"], default="config", help="'mock' = offline dry run")
    p.add_argument("--judge", default="paper", help="paper | auto | reject | llm | interactive | keyword:<k1,k2>")
    p.add_argument("--scorer", default=None, help="dir of a trained LogitScorer (adds a logit per rule-based step)")
    p.add_argument("--rag", action="store_true", help="retrieve theory / precedents from data/corpus (BM25)")
    p.add_argument("--out", default=None, help="write JSON trace here (and .md next to it)")
    return p


def llm_spec(args):
    return {"type": "mock"} if args.backend == "mock" else load_config(args.config)["llm"]


def save(result, out):
    if not out:
        return
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    result.save(out)
    Path(out).with_suffix(".md").write_text(result.to_markdown())
    print(f"saved {out} (+ .md)")
