"""The 8 evaluation prompts of §4.4: 3 rule-based, 3 abductive, 2 case-based (Appendices A and B)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .. import prompts
from ..components import Outcome
from ..examples import (A3_HYPOTHESIS, B3_HYPOTHESIS, CIVIL_THEORY, DEFENDANT_THEORY, ISSUE, KEEBLE_V_HICKERINGILL,
                        PIERSON_V_POST, PLAINTIFF_THEORY, YOUNG_V_HITCHENS)


@dataclass(frozen=True)
class EvalTask:
    id: str
    mode: str
    source: str  # appendix reference
    prompt: str


def build_tasks() -> List[EvalTask]:
    F, I = YOUNG_V_HITCHENS, ISSUE
    return [
        EvalTask("rule_A.1", "rule_based", "A.1", prompts.rule_based(F, CIVIL_THEORY, I)),
        EvalTask("rule_A.3", "rule_based", "A.3", prompts.rule_based(F, CIVIL_THEORY, I, [A3_HYPOTHESIS])),
        EvalTask("rule_B.3", "rule_based", "B.3", prompts.rule_based(F, PLAINTIFF_THEORY, I, [B3_HYPOTHESIS])),
        EvalTask("abd_A.2", "abductive", "A.2", prompts.abductive(F, CIVIL_THEORY, Outcome(I, False))),
        EvalTask("abd_B.2.1", "abductive", "B.2.1", prompts.abductive(F, PLAINTIFF_THEORY, Outcome(I, False))),
        EvalTask("abd_B.2.2", "abductive", "B.2.2", prompts.abductive(F, DEFENDANT_THEORY, Outcome(I, True))),
        EvalTask("case_B.1.plaintiff", "case_based", "B.1", prompts.case_based(F, KEEBLE_V_HICKERINGILL, I)),
        EvalTask("case_B.1.defendant", "case_based", "B.1", prompts.case_based(F, PIERSON_V_POST, I)),
    ]
