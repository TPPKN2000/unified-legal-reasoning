"""The four components of the unified framework (paper §4.1, Fig. 2).

Fact        - context of the case
Theory      - defeasible rules derived from statutes or precedent cases
Hypothesis  - hypothetical facts/rules derived from context (e.g. intentions)
Outcome     - decision on a specific issue (e.g. guilty / not guilty)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


def numbered(items: List[str]) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


@dataclass(frozen=True)
class Issue:
    """The proposition at stake, e.g. 'the defendant is guilty of theft'."""

    claim: str
    negated_claim: str
    theory_head: str = "A person is typically guilty of theft if the following conditions hold:"
    positive_pattern: str = r"\bguilty\b"
    negative_pattern: str = r"\b(?:not|never)\s+(?:\w+\s+){0,2}guilty\b|\binnocent\b"


@dataclass
class Fact:
    statements: List[str]
    name: str = ""

    def render(self) -> str:
        return numbered(self.statements)


@dataclass
class Theory:
    head: str
    conditions: List[str]
    exception: Optional[str] = None

    def render(self) -> str:
        s = self.head + "\n" + numbered(self.conditions)
        if self.exception:
            s += "\n" + self.exception
        return s


@dataclass
class Hypothesis:
    statement: str
    title: str = ""
    argument: str = ""
    source: str = "abductive"  # abductive | case_based | judge
    side: Optional[str] = None  # plaintiff | defendant

    @property
    def full_text(self) -> str:
        return " ".join(x for x in (self.title, self.argument, self.statement) if x)


@dataclass
class Outcome:
    issue: Issue
    holds: Optional[bool] = None  # True: claim holds; False: negated claim; None: undetermined

    @property
    def text(self) -> str:
        if self.holds is None:
            return "undetermined"
        return self.issue.claim if self.holds else self.issue.negated_claim


@dataclass
class Precedent:
    name: str
    fact: Fact
    outcome: Outcome
