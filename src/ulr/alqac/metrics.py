"""Pure-python explanation metrics (no extra dependencies). Everything here scores an EXPLANATION text against the
case inputs / court reference; none of it measures outcome-prediction accuracy."""
from __future__ import annotations

import re
from collections import Counter
from typing import Dict, Iterable, List, Optional, Sequence, Set

_WORD = re.compile(r"\w+", re.UNICODE)


def toks(s: str) -> List[str]:
    return _WORD.findall((s or "").lower())


def sentences(text: str, min_tokens: int = 1) -> List[str]:
    parts = re.split(r"(?<=[.!?;:])\s+|\n+", text or "")
    return [p.strip() for p in parts if len(toks(p)) >= min_tokens]


def token_f1(a: Sequence[str], b: Sequence[str]) -> float:
    if not a or not b:
        return 0.0
    common = sum((Counter(a) & Counter(b)).values())
    if common == 0:
        return 0.0
    p, r = common / len(b), common / len(a)
    return 2 * p * r / (p + r)


def lcs_len(a: Sequence[str], b: Sequence[str]) -> int:
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if x == y else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]


def rouge_l(reference: str, candidate: str, cap: int = 1500) -> Dict[str, float]:
    r, c = toks(reference)[:cap], toks(candidate)[:cap]
    l = lcs_len(r, c)
    if l == 0:
        return {"p": 0.0, "r": 0.0, "f": 0.0}
    p, rec = l / len(c), l / len(r)
    return {"p": p, "r": rec, "f": 2 * p * rec / (p + rec)}


def _bigrams(t: Sequence[str]) -> Set[tuple]:
    return set(zip(t, t[1:]))


def point_coverage(candidate: str, reference: str, min_tokens: int = 8, thr: float = 0.3) -> Dict[str, Optional[float]]:
    """Each reference sentence is a 'point'; coverage = share of its bigrams present in the candidate.
    Crude lexical proxy (use the embedding scorer for a semantic one)."""
    cand = _bigrams(toks(candidate))
    pts = [s for s in sentences(reference, min_tokens)]
    if not pts:
        return {"mean": None, "frac_ge_thr": None, "n_points": 0}
    cov = []
    for s in pts:
        b = _bigrams(toks(s))
        cov.append(len(b & cand) / len(b) if b else 0.0)
    return {"mean": sum(cov) / len(cov), "frac_ge_thr": sum(c >= thr for c in cov) / len(cov), "n_points": len(pts)}


# ---------------- citations ----------------
_ART = re.compile(r"Điều(?:\s+|\s*:\s*)(\d+(?:\s*(?:,|;|và)\s*(?:Điều\s*)?\d+)*)", re.I)


def cited_articles(text: str) -> Set[int]:
    out: Set[int] = set()
    for m in _ART.finditer(text or ""):
        out |= {int(x) for x in re.findall(r"\d+", m.group(1))}
    return out


def prf(pred: Set, gold: Set) -> Dict[str, Optional[float]]:
    if not gold:
        return {"p": None, "r": None, "f": None}
    tp = len(pred & gold)
    p = tp / len(pred) if pred else 0.0
    r = tp / len(gold)
    return {"p": p, "r": r, "f": (2 * p * r / (p + r)) if (p + r) else 0.0}


# ---------------- grounding ----------------
_NUM = re.compile(r"\d[\d.,/]*\d|\d")
_STRIP = [
    _ART,
    re.compile(r"(?:khoản|điểm|mục|tiểu mục)\s+\d+\w?", re.I),
    re.compile(r"(?m)^\s*\d+[.)]\s+"),
    re.compile(r"\[\d+\]"),
]


def numbers(text: str, drop_citations: bool = True) -> Set[str]:
    t = text or ""
    if drop_citations:
        for pat in _STRIP:
            t = pat.sub(" ", t)
    out = set()
    for m in _NUM.findall(t):
        n = re.sub(r"[.,/]", "", m)
        if len(n) >= 2:
            out.add(n)
    return out


def unsupported_numbers(explanation: str, sources: Iterable[str]) -> Dict[str, Optional[float]]:
    """Share of numbers in the explanation (amounts, dates, ...) that appear nowhere in the case inputs.
    A hallucination PROXY: legitimate re-formatting (e.g. '3,2 tỷ') is counted as unsupported."""
    gen = numbers(explanation)
    if not gen:
        return {"rate": None, "n": 0, "unsupported": []}
    src: Set[str] = set()
    for s in sources:
        src |= numbers(s, drop_citations=False)
    bad = sorted(gen - src)
    return {"rate": len(bad) / len(gen), "n": len(gen), "unsupported": bad}


# ---------------- leakage ----------------
def leakage(case_fact: str, reference_reasoning: str, min_tokens: int = 6, thr: float = 0.8) -> Dict[str, float]:
    """Share of court_reasoning sentences that already appear (token-F1 >= thr) inside case_fact.
    High values mean the 'facts' already contain the court's reasoning, which inflates explanation scores."""
    fact_s = [toks(s) for s in sentences(case_fact, min_tokens)]
    ref_s = [s for s in sentences(reference_reasoning, min_tokens)]
    if not ref_s:
        return {"ratio": 0.0, "n_ref": 0, "n_leaked": 0}
    leaked = 0
    for s in ref_s:
        t = toks(s)
        if any(token_f1(t, f) >= thr for f in fact_s):
            leaked += 1
    return {"ratio": leaked / len(ref_s), "n_ref": len(ref_s), "n_leaked": leaked}


def decontaminate(case_fact: str, reference_reasoning: str, min_tokens: int = 6, thr: float = 0.8) -> str:
    """Drop sentences of case_fact that are (near-)verbatim court-reasoning sentences."""
    ref_t = [toks(s) for s in sentences(reference_reasoning, min_tokens)]
    kept_lines = []
    for line in case_fact.split("\n"):
        kept = [s for s in re.split(r"(?<=[.!?;])\s+", line)
                if not (len(toks(s)) >= min_tokens and any(token_f1(toks(s), r) >= thr for r in ref_t))]
        if kept:
            kept_lines.append(" ".join(kept))
    return "\n".join(kept_lines)


# ---------------- Vietnamese verdict labelling (explanation <-> outcome consistency) ----------------
_NEG = re.compile(r"không\s+(?:được\s+)?(?:tòa án\s+)?chấp nhận|bác\s+(?:toàn bộ\s+)?(?:yêu cầu|đơn)|bị đơn thắng", re.I)
_PART = re.compile(r"chấp nhận\s+một\s+phần|một\s+phần\s+yêu\s+cầu|chấp nhận\s+phần", re.I)
_POS = re.compile(r"chấp nhận|nguyên đơn thắng", re.I)
_RESTATE = re.compile(r"hay không|có chấp nhận|whether|đánh giá|xem xét", re.I)
_CUE = re.compile(r"do đó|vì vậy|như vậy|kết luận|tóm lại|therefore|thus", re.I)


def classify_label_vi(text: str) -> Optional[str]:
    sents = [s for s in sentences(text) if _POS.search(s) or _NEG.search(s)]
    sents = [s for s in sents if not _RESTATE.search(s)] or sents
    if not sents:
        return None
    cue = [s for s in sents if _CUE.search(s)]
    s = cue[-1] if cue else sents[-1]
    if _PART.search(s):
        return "PARTIAL_A_WIN"
    if _NEG.search(s):
        return "B_WIN"
    if _POS.search(s):
        return "A_WIN"
    return None
