"""Prompt templates reproduced from the paper's Appendix A and B (verbatim wording)."""
from __future__ import annotations

from typing import Sequence

from .components import Fact, Hypothesis, Issue, Outcome, Precedent, Theory


def rule_based(fact: Fact, theory: Theory, issue: Issue, hypotheses: Sequence[Hypothesis] = ()) -> str:
    """Appendix A.1 (no hypothesis), A.3 / B.3 (with accepted hypotheses)."""
    parts = [
        "Considering the following facts:",
        fact.render(),
        f"Considering the following rules: {theory.render()}",
    ]
    if hypotheses:
        parts.append("Assuming these hypotheses are true in this case:")
        parts.extend(h.statement for h in hypotheses)
        tail = f"According to the given rules and hypotheses, please evaluate whether {issue.claim}."
    else:
        tail = f"According to the given rules, please evaluate whether {issue.claim}."
    return "\n".join(parts + [tail])


def abductive(fact: Fact, theory: Theory, outcome: Outcome) -> str:
    """Appendix A.2 / B.2."""
    return "\n".join(
        [
            "Considering the following facts:",
            fact.render(),
            f"Considering the following rules: {theory.render()}",
            f"Please suggest hypotheses to support why the outcome of the case might be {outcome.text}.",
        ]
    )


def case_based(present: Fact, precedent: Precedent, issue: Issue) -> str:
    """Appendix B.1."""
    return "\n".join(
        [
            "Considering the current case:",
            present.render(),
            "Considering the precedent case:",
            precedent.fact.render(),
            f"The precedent case has the following outcome: {precedent.outcome.text}",
            "Please answer why the current case might have the same outcome in the following "
            "form and make a rule-based explanation between the current case and the rule of that form:",
            issue.theory_head,
            "1. ...",
            "2. ...",
        ]
    )


# --- helper prompts (NOT part of the paper's framework; parsing / judge aids) ---
VERDICT_CLASSIFIER = (
    "Given the following legal analysis, answer with exactly one word: "
    "YES if it concludes that {claim}, NO if it concludes that {negated}, UNKNOWN otherwise.\n\n"
    "Analysis:\n{text}"
)

LLM_JUDGE_SELECT = (
    "You are presiding over a court as the judge. Below are candidate hypotheses put forward by the "
    "{side} to challenge the current legal theory.\n\n{candidates}\n\n"
    "Which hypothesis, if any, should the court accept? Answer with the number of the single most "
    "legally persuasive hypothesis, or 0 to reject all of them. Answer with a number only."
)
