"""Heuristic parsers that turn free-text LLM answers into framework components."""
from __future__ import annotations

import json
import re
from typing import List, Optional, Tuple

from .components import Hypothesis, Issue, Theory

_SENT = re.compile(r"(?<=[.!?])\s+")
_CUES = re.compile(
    r"\b(based on|therefore|thus|in conclusion|overall|in summary|appears to be|likely|conclude)\b", re.I
)


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").replace("**", "").replace("*", "")).strip(" :-\n\t")


def parse_verdict(text: str, issue: Issue) -> Optional[bool]:
    """True -> the issue's claim holds (e.g. guilty); False -> negated claim; None -> inconclusive."""
    pos = re.compile(issue.positive_pattern, re.I)
    neg = re.compile(issue.negative_pattern, re.I)
    sents = [s for s in _SENT.split(text.replace("\n", " ")) if pos.search(s) or neg.search(s)]
    if not sents:
        return None
    cue = [s for s in sents if _CUES.search(s)]
    chosen = cue[0] if cue else sents[-1]
    return False if neg.search(chosen) else True


def _strip_cond(title: str) -> str:
    return _clean(re.sub(r"\(\s*Conditions?[^)]*\)", "", title, flags=re.I))


def _statement(title: str, argument: str) -> str:
    t = _strip_cond(title)
    if len(t.split()) >= 6:
        return t
    first = _SENT.split(argument.strip())[0] if argument.strip() else ""
    first = _clean(first)
    if t and first:
        return f"{t}: {first}"
    return t or first


def _strip_arg_label(s: str) -> str:
    return _clean(re.sub(r"(?i)^\s*(?:\*\*)?argument\s*:?(?:\*\*)?", "", s.strip()))


_HYP_HEAD = re.compile(r"(?mi)^[ \t>#*-]*Hypothes[ie]s\s*(\d+[a-z]?)\b[^\n]*")


def parse_hypotheses(text: str, source: str = "abductive", side: Optional[str] = None) -> List[Hypothesis]:
    items: List[Hypothesis] = []
    heads = list(_HYP_HEAD.finditer(text))
    if heads:
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            body = text[m.end():end]
            rest = re.sub(r"(?i)^[\W_]*hypothes[ie]s\s*\d+[a-z]?", "", m.group(0))
            mm = re.match(r"\s*\*{0,2}\s*(?:\(([^)]*)\))?\s*\*{0,2}\s*[:.\-–]?\s*(.*)", rest, re.S)
            label, remainder = _clean(mm.group(1) or ""), _clean(mm.group(2))
            if label:
                title, argument = label, _strip_arg_label(remainder + " " + body)
            else:
                title, argument = remainder, _strip_arg_label(body)
            st = _statement(title, argument)
            if st:
                items.append(Hypothesis(statement=st, title=title, argument=argument, source=source, side=side))
        if items:
            return items
    num = list(re.finditer(r"(?ms)^\s*(\d+)[.)]\s+(.*?)(?=^\s*\d+[.)]\s+|\Z)", text))
    for m in num:
        body = m.group(2).strip()
        b = re.match(r"\*\*(.+?)\*\*\s*:?\s*(.*)", body, re.S)
        if b:
            title, argument = _clean(b.group(1)), _clean(b.group(2))
        elif ":" in body[:200]:
            title, argument = (_clean(x) for x in body.split(":", 1))
        else:
            title, argument = _clean(body), ""
        st = _statement(title, argument)
        if st:
            items.append(Hypothesis(statement=st, title=title, argument=argument, source=source, side=side))
    if items:
        return items
    t = _clean(text)
    return [Hypothesis(statement=t[:600], title="", argument=t, source=source, side=side)] if t else []


def parse_case_based(text: str, issue: Issue, side: Optional[str] = None) -> Tuple[Theory, Hypothesis]:
    """Split a B.1-style answer into (Theory, explanatory Hypothesis)."""
    parts = re.split(r"(?i)rule-?based explanation\s*:?", text, maxsplit=1)
    theory_part = parts[0]
    explanation = _clean(parts[1]) if len(parts) > 1 else ""
    conds = [_clean(c) for c in re.findall(r"(?m)^\s*\d+[.)]\s+(.*)$", theory_part)]
    conds = [c for c in conds if c and c != "..."]
    if not conds:
        lines = [l for l in theory_part.splitlines() if l.strip() and issue.theory_head not in l]
        conds = [_clean(" ".join(lines))] if lines else []
    theory = Theory(head=issue.theory_head, conditions=conds)
    hyp = Hypothesis(
        statement=explanation or _clean(text)[:600],
        title="Analogical explanation",
        argument=explanation,
        source="case_based",
        side=side,
    )
    return theory, hyp


def extract_json(text: str) -> Optional[dict]:
    t = re.sub(r"```(?:json)?", "", text)
    a, b = t.find("{"), t.rfind("}")
    if a == -1 or b <= a:
        return None
    try:
        return json.loads(t[a:b + 1])
    except json.JSONDecodeError:
        return None
