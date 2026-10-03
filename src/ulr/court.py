"""Court-procedure simulators of the unified framework (paper §4.3, Appendices A and B).

Civil law  : A.1 rule-based -> A.2 abductive (challenge) -> judge -> A.3 rule-based (+hypothesis) -> repeat
Common law : B.1 case-based (both sides) -> B.2 challenge (own case-based hypothesis | abductive)
             -> judge -> B.3 rule-based (+hypothesis) from each side's perspective
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from .components import Fact, Hypothesis, Issue, Outcome, Precedent, Theory
from .judges import Judge
from .reasoners import AbductiveReasoner, CaseBasedReasoner, RuleBasedReasoner


@dataclass
class TraceStep:
    step: str  # e.g. "A.1", "B.2"
    mode: str
    side: Optional[str]
    prompt: str
    response: str
    parsed: Any = None


@dataclass
class CourtResult:
    system: str  # civil | common
    fact: Fact
    theory: Any  # Theory (civil) | {side: Theory} (common)
    hypotheses: List[Hypothesis]  # accepted by the judge
    outcome: Outcome
    converged: bool
    trace: List[TraceStep] = field(default_factory=list)
    extra: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False, default=str)

    def to_markdown(self) -> str:
        lines = [f"# {self.system.title()} law simulation", ""]
        for s in self.trace:
            lines += [f"## {s.step} — {s.mode}" + (f" ({s.side})" if s.side else ""), "", "**Prompt**", "```", s.prompt, "```", "**Response**", "```", s.response, "```", ""]
        lines += [
            "## Result",
            f"- outcome: **{self.outcome.text}**",
            f"- converged: {self.converged}",
            "- accepted hypotheses:",
            *[f"  - {h.statement}" for h in self.hypotheses],
        ]
        return "\n".join(lines)


class CivilLawSimulator:
    """Starts in rule-based mode; the dissatisfied side re-prompts in abductive mode (§4.3)."""

    def __init__(self, rule: RuleBasedReasoner, abductive: AbductiveReasoner, judge: Judge, max_rounds: int = 2):
        self.rule, self.abd, self.judge, self.max_rounds = rule, abductive, judge, max_rounds

    def run(self, fact: Fact, theory: Theory, issue: Issue) -> CourtResult:
        trace: List[TraceStep] = []
        r = self.rule.run(fact, theory, issue)
        trace.append(TraceStep("A.1", "rule_based", None, r.prompt, r.response, {"outcome": r.outcome.text, "score": r.score}))
        outcome, accepted, converged = r.outcome, [], False
        if outcome.holds is None:
            return CourtResult("civil", fact, theory, accepted, outcome, False, trace)

        for rnd in range(1, self.max_rounds + 1):
            challenger = "defendant" if outcome.holds else "plaintiff"  # the side not satisfied
            target = Outcome(issue, holds=not outcome.holds)
            ab = self.abd.run(fact, theory, target, side=challenger)
            trace.append(TraceStep(f"A.2#{rnd}", "abductive", challenger, ab.prompt, ab.response, [h.statement for h in ab.hypotheses]))

            d = self.judge.decide(ab.hypotheses, fact=fact, theory=theory, issue=issue, side=challenger)
            revised = bool(d.facts or d.theory)
            fact, theory = d.facts or fact, d.theory or theory
            new_h = [h for h in d.accepted if h not in accepted]
            trace.append(TraceStep(f"judge#{rnd}", "judge", None, "", d.note, [h.statement for h in new_h]))
            if not new_h and not revised:
                converged = True  # judge rejected the challenge: current outcome stands
                break
            accepted += new_h

            rr = self.rule.run(fact, theory, issue, accepted)
            trace.append(TraceStep(f"A.3#{rnd}", "rule_based", challenger, rr.prompt, rr.response, {"outcome": rr.outcome.text, "score": rr.score}))
            stable = rr.outcome.holds == outcome.holds
            outcome = rr.outcome
            if outcome.holds is None:
                break
            if stable:
                converged = True
                break
        return CourtResult("civil", fact, theory, accepted, outcome, converged, trace)


class CommonLawSimulator:
    """Starts in case-based mode with one precedent per side (§4.3)."""

    SIDES = ("plaintiff", "defendant")

    def __init__(self, rule: RuleBasedReasoner, abductive: AbductiveReasoner, case: CaseBasedReasoner, judge: Judge):
        self.rule, self.abd, self.case, self.judge = rule, abductive, case, judge

    def run(self, fact: Fact, issue: Issue, precedents: Dict[str, Precedent]) -> CourtResult:
        trace: List[TraceStep] = []
        theories: Dict[str, Theory] = {}
        own_hyp: Dict[str, Hypothesis] = {}

        # B.1 — each side builds a theory + explanatory hypothesis from its precedent
        for side in self.SIDES:
            c = self.case.run(fact, precedents[side], issue, side=side)
            theories[side], own_hyp[side] = c.theory, c.hypothesis
            trace.append(TraceStep("B.1", "case_based", side, c.prompt, c.response, {"theory": c.theory.conditions}))

        # B.2 — each side challenges the opponent's theory: (1) own case-based hypothesis, (2) new abductive hypotheses
        candidates: List[Hypothesis] = []
        for challenger, opponent in (("defendant", "plaintiff"), ("plaintiff", "defendant")):
            target = Outcome(issue, holds=(challenger == "plaintiff"))
            ab = self.abd.run(fact, theories[opponent], target, side=challenger)
            trace.append(TraceStep("B.2", "abductive", challenger, ab.prompt, ab.response, [h.statement for h in ab.hypotheses]))
            candidates += [own_hyp[challenger]] + ab.hypotheses

        d = self.judge.decide(candidates, fact=fact, theory=theories["plaintiff"], issue=issue, side=None)
        accepted = list(d.accepted)
        trace.append(TraceStep("judge", "judge", None, "", d.note, [h.statement for h in accepted]))
        fact = d.facts or fact

        # B.3 — re-assess the outcome from each side's perspective with the accepted hypotheses
        outcomes: Dict[str, Outcome] = {}
        for side in self.SIDES:
            rr = self.rule.run(fact, d.theory or theories[side], issue, accepted)
            outcomes[side] = rr.outcome
            trace.append(TraceStep("B.3", "rule_based", side, rr.prompt, rr.response, {"outcome": rr.outcome.text, "score": rr.score}))

        o_p, o_d = outcomes["plaintiff"], outcomes["defendant"]
        converged = o_p.holds is not None and o_p.holds == o_d.holds
        final = o_p if converged else Outcome(issue, None)
        return CourtResult(
            "common", fact, theories, accepted, final, converged, trace,
            extra={"side_outcomes": {k: v.text for k, v in outcomes.items()}},
        )
