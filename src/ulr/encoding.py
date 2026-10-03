"""S = Encode(F, T, H, O)  (paper §4.2, fine-tuning approach). torch-free."""
from __future__ import annotations

from typing import Sequence

from .components import Fact, Hypothesis, Outcome, Theory


def encode(fact: Fact, theory: Theory, hypotheses: Sequence[Hypothesis], outcome: Outcome) -> str:
    h = " ".join(x.statement for x in hypotheses) if hypotheses else "None"
    return (
        f"[FACT]\n{fact.render()}\n"
        f"[THEORY]\n{theory.render()}\n"
        f"[HYPOTHESIS]\n{h}\n"
        f"[OUTCOME]\n{outcome.text}"
    )
