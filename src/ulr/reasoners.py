"""The three reasoning modes of the unified framework, each driven by an LLM (paper §4.1)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence

from . import prompts
from .components import Fact, Hypothesis, Issue, Outcome, Precedent, Theory
from .modes import Mode, check_inputs
from .parsing import parse_case_based, parse_hypotheses, parse_verdict


@dataclass
class RuleResult:
    prompt: str
    response: str
    outcome: Outcome
    score: Optional[float] = None  # logit from the fine-tuned scorer (§4.2), if provided


@dataclass
class AbductiveResult:
    prompt: str
    response: str
    hypotheses: List[Hypothesis]


@dataclass
class CaseResult:
    prompt: str
    response: str
    theory: Theory
    hypothesis: Hypothesis


class _Base:
    def __init__(self, llm, gen: Optional[Dict[str, Any]] = None):
        self.llm = llm
        self.gen = gen or {}

    def _ask(self, prompt: str) -> str:
        return self.llm.generate(prompt, **self.gen)


class RuleBasedReasoner(_Base):
    """Fact + Theory (+ accepted Hypothesis) -> plausibility of Outcome."""

    mode = Mode.RULE_BASED

    def __init__(self, llm, scorer=None, classifier_fallback: bool = True, gen=None):
        super().__init__(llm, gen)
        self.scorer = scorer
        self.classifier_fallback = classifier_fallback

    def _classify(self, text: str, issue: Issue) -> Optional[bool]:
        ans = self._ask(
            prompts.VERDICT_CLASSIFIER.format(claim=issue.claim, negated=issue.negated_claim, text=text)
        ).strip().upper()
        if ans.startswith("YES"):
            return True
        if ans.startswith("NO"):
            return False
        return None

    def run(self, fact: Fact, theory: Theory, issue: Issue, hypotheses: Sequence[Hypothesis] = ()) -> RuleResult:
        check_inputs(self.mode, fact=fact, theory=theory, hypothesis=list(hypotheses) or None)
        prompt = prompts.rule_based(fact, theory, issue, hypotheses)
        resp = self._ask(prompt)
        holds = parse_verdict(resp, issue)
        if holds is None and self.classifier_fallback:
            holds = self._classify(resp, issue)
        outcome = Outcome(issue, holds)
        score = None
        if self.scorer is not None and holds is not None:
            score = self.scorer.score(fact, theory, list(hypotheses), outcome)
        return RuleResult(prompt, resp, outcome, score)


class AbductiveReasoner(_Base):
    """Fact + Theory + Outcome -> candidate Hypotheses explaining the outcome."""

    mode = Mode.ABDUCTIVE

    def run(self, fact: Fact, theory: Theory, outcome: Outcome, side: Optional[str] = None) -> AbductiveResult:
        check_inputs(self.mode, fact=fact, theory=theory, outcome=outcome)
        prompt = prompts.abductive(fact, theory, outcome)
        resp = self._ask(prompt)
        return AbductiveResult(prompt, resp, parse_hypotheses(resp, "abductive", side))


class CaseBasedReasoner(_Base):
    """Fact(present) + Fact(precedent) + Outcome -> Theory + analogical Hypothesis."""

    mode = Mode.CASE_BASED

    def run(self, present: Fact, precedent: Precedent, issue: Issue, side: Optional[str] = None) -> CaseResult:
        check_inputs(
            self.mode, fact_present=present, fact_precedent=precedent.fact, outcome=precedent.outcome
        )
        prompt = prompts.case_based(present, precedent, issue)
        resp = self._ask(prompt)
        theory, hyp = parse_case_based(resp, issue, side)
        return CaseResult(prompt, resp, theory, hyp)
