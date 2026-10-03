"""Judge strategies: the judge 'has the discretion to accept or reject hypotheses, refine the facts,
or revise the theory' (paper §4.3)."""
from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable, List, Optional, Sequence

from . import prompts
from .components import Fact, Hypothesis, Issue, Theory


@dataclass
class JudgeDecision:
    accepted: List[Hypothesis] = field(default_factory=list)
    facts: Optional[Fact] = None  # refined facts (optional)
    theory: Optional[Theory] = None  # revised theory (optional)
    note: str = ""


class Judge(ABC):
    @abstractmethod
    def decide(
        self,
        candidates: Sequence[Hypothesis],
        *,
        fact: Fact,
        theory: Theory,
        issue: Issue,
        side: Optional[str] = None,
    ) -> JudgeDecision: ...


class AutoJudge(Judge):
    """Accepts the first candidate (useful for quick demos)."""

    def decide(self, candidates, **_):
        return JudgeDecision(accepted=list(candidates[:1]), note="auto: first candidate")


class RejectJudge(Judge):
    def decide(self, candidates, **_):
        return JudgeDecision(note="reject all")


class KeywordJudge(Judge):
    """Scripted judge: accepts the first candidate containing a keyword (optionally from given sides only).
    `KeywordJudge(PAPER_JUDGE_KEYWORDS, sides={'defendant'})` reproduces the paper's choice."""

    def __init__(self, keywords: Iterable[str], sides: Optional[Iterable[str]] = None):
        self.keywords = [k.lower() for k in keywords]
        self.sides = set(sides) if sides else None

    def decide(self, candidates, *, side=None, **_):
        for h in candidates:
            s = h.side or side
            if self.sides and s not in self.sides:
                continue
            if any(k in h.full_text.lower() for k in self.keywords):
                return JudgeDecision(accepted=[h], note=f"keyword match ({s})")
        return JudgeDecision(note="no keyword match")


class InteractiveJudge(Judge):
    """You are the judge: pick hypotheses by number (comma separated) or 0 to reject all."""

    def decide(self, candidates, *, side=None, **_):
        print(f"\n--- Judge decision (challenger: {side}) ---")
        for i, h in enumerate(candidates, 1):
            print(f"[{i}] ({h.side or side}, {h.source}) {h.statement}")
        raw = input("Accept which? (e.g. 1,3 | 0 = none): ").strip()
        idx = [int(x) for x in re.findall(r"\d+", raw)]
        return JudgeDecision(accepted=[candidates[i - 1] for i in idx if 1 <= i <= len(candidates)], note="interactive")


class LLMJudge(Judge):
    """Lets an LLM play the judge (selects at most one hypothesis)."""

    def __init__(self, llm):
        self.llm = llm

    def decide(self, candidates, *, side=None, **_):
        if not candidates:
            return JudgeDecision(note="no candidates")
        listing = "\n".join(f"{i}. {h.statement}" for i, h in enumerate(candidates, 1))
        ans = self.llm.generate(prompts.LLM_JUDGE_SELECT.format(side=side or "party", candidates=listing))
        m = re.search(r"\d+", ans)
        i = int(m.group()) if m else 0
        if 1 <= i <= len(candidates):
            return JudgeDecision(accepted=[candidates[i - 1]], note="llm judge")
        return JudgeDecision(note="llm judge rejected all")


def build_judge(kind: str, llm=None) -> Judge:
    from .examples import PAPER_JUDGE_KEYWORDS

    if kind == "auto":
        return AutoJudge()
    if kind == "reject":
        return RejectJudge()
    if kind == "paper":
        return KeywordJudge(PAPER_JUDGE_KEYWORDS, sides={"defendant"})
    if kind == "interactive":
        return InteractiveJudge()
    if kind == "llm":
        if llm is None:
            raise ValueError("llm judge needs an LLM backend")
        return LLMJudge(llm)
    if kind.startswith("keyword:"):
        return KeywordJudge([k for k in kind.split(":", 1)[1].split(",") if k])
    raise ValueError(f"unknown judge: {kind}")
