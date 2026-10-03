"""Glue used by scripts / notebook: config loading and component wiring."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from .judges import build_judge
from .llm import build_backend
from .reasoners import AbductiveReasoner, CaseBasedReasoner, RuleBasedReasoner


def load_config(path: Optional[str]) -> Dict[str, Any]:
    if not path:
        return {}
    return yaml.safe_load(Path(path).read_text()) or {}


def build_components(llm_spec: Dict[str, Any], scorer_dir: Optional[str] = None, judge_kind: str = "paper"):
    llm = build_backend(llm_spec)
    scorer = None
    if scorer_dir:
        from .scoring import LogitScorer

        scorer = LogitScorer.load(scorer_dir)
    rule = RuleBasedReasoner(llm, scorer=scorer)
    abd = AbductiveReasoner(llm)
    case = CaseBasedReasoner(llm)
    judge = build_judge(judge_kind, llm)
    return llm, rule, abd, case, judge
