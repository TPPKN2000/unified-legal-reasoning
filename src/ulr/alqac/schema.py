"""ALQAC-style data: cases (ALQAC_public_test_sample.json) and law corpus (corpus_law_pub_sample.json)."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

REQUIRED_CASE_FIELDS = ("case_id", "case_fact", "case_query", "verdict_label")
VERDICT_LABELS = ("A_WIN", "PARTIAL_A_WIN", "B_WIN")

# Fields the model may SEE. verdict_label is only used as the given Outcome; related_law_provisions only in the
# `oracle` theory setting.
ALLOWED_INPUT_FIELDS = ("case_fact", "case_query", "case_type", "court", "court_level", "A_role", "B_role",
                        "A_description", "B_description", "related_law_provisions", "verdict_label")
# Reference-only fields (used for scoring, NEVER put into a prompt).
FORBIDDEN_INPUT_FIELDS = ("judgment_text", "court_verdict", "court_reasoning")


@dataclass
class Provision:
    law: str
    article: Optional[int]
    raw: str


@dataclass
class AlqacCase:
    case_id: str
    case_fact: str
    case_query: str
    verdict_label: str
    case_type: str = ""
    court: str = ""
    court_level: str = ""
    A_role: str = "Nguyên đơn"
    B_role: str = "Bị đơn"
    provisions: List[Provision] = field(default_factory=list)
    reference_reasoning: str = ""  # court_reasoning — scoring only
    reference_verdict: str = ""  # court_verdict — scoring only


@dataclass
class LawArticle:
    law_id: str
    aid: int
    text: str
    article_no: Optional[int] = None


def parse_provisions(text: str) -> List[Provision]:
    """'Bộ luật dân sự năm 2005 | Điều 245' per line; lines without 'Điều N' keep article=None."""
    out: List[Provision] = []
    seen = set()
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        law, _, art = line.partition("|")
        m = re.search(r"Điều\s*(\d+)", art)
        p = Provision(law=law.strip(" .;"), article=int(m.group(1)) if m else None, raw=line)
        if (p.law, p.article) not in seen:
            seen.add((p.law, p.article))
            out.append(p)
    return out


def load_cases(path: str | Path) -> List[AlqacCase]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a JSON list of cases, got {type(data).__name__}")
    cases = []
    for i, d in enumerate(data):
        missing = [k for k in REQUIRED_CASE_FIELDS if not d.get(k)]
        if missing:
            raise ValueError(f"{path}: case #{i} ({d.get('case_id')}) missing fields {missing}")
        if d["verdict_label"] not in VERDICT_LABELS:
            raise ValueError(f"{path}: case {d['case_id']} has unsupported verdict_label {d['verdict_label']!r}; "
                             f"expected one of {VERDICT_LABELS}")
        cases.append(AlqacCase(
            case_id=d["case_id"], case_fact=d["case_fact"], case_query=d["case_query"], verdict_label=d["verdict_label"],
            case_type=d.get("case_type", ""), court=d.get("court", ""), court_level=d.get("court_level", ""),
            A_role=d.get("A_role") or "Nguyên đơn", B_role=d.get("B_role") or "Bị đơn",
            provisions=parse_provisions(d.get("related_law_provisions", "")),
            reference_reasoning=d.get("court_reasoning", ""), reference_verdict=d.get("court_verdict", "")))
    return cases


def load_corpus(path: str | Path) -> List[LawArticle]:
    """[{id, law_id, content:[{aid, content_Article}]}]. `aid` is a GLOBAL id (not the article number).
    The article number is parsed from a leading 'Điều N' when present, or taken from an optional `article_no` field."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    out: List[LawArticle] = []
    for law in data:
        for a in law.get("content", []):
            text = a.get("content_Article", "")
            n = a.get("article_no")
            if n is None:
                m = re.match(r"\s*Điều\s+(\d+)", text)
                n = int(m.group(1)) if m else None
            out.append(LawArticle(law_id=law["law_id"], aid=a["aid"], text=text, article_no=n))
    return out
