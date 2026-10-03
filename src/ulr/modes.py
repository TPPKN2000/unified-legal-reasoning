"""The three reasoning modes and their input/output contract (paper §4.1, Fig. 2)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Mode(str, Enum):
    RULE_BASED = "rule_based"
    ABDUCTIVE = "abductive"
    CASE_BASED = "case_based"


@dataclass(frozen=True)
class ModeSpec:
    required: frozenset
    optional: frozenset
    produces: Tuple[str, ...]


MODE_SPECS = {
    # Fact + Theory (+ Hypothesis accepted by the user) -> plausibility of Outcome
    Mode.RULE_BASED: ModeSpec(frozenset({"fact", "theory"}), frozenset({"hypothesis"}), ("outcome",)),
    # Fact + Theory + Outcome -> plausibility of Hypothesis as explanation
    Mode.ABDUCTIVE: ModeSpec(frozenset({"fact", "theory", "outcome"}), frozenset(), ("hypothesis",)),
    # Fact(precedent) + Fact(present) + Outcome -> Theory + Hypothesis (analogy)
    Mode.CASE_BASED: ModeSpec(
        frozenset({"fact_precedent", "fact_present", "outcome"}), frozenset(), ("theory", "hypothesis")
    ),
}


def check_inputs(mode: Mode, **provided) -> None:
    spec = MODE_SPECS[mode]
    missing = sorted(k for k in spec.required if provided.get(k) is None)
    extra = sorted(k for k, v in provided.items() if v is not None and k not in spec.required | spec.optional)
    if missing:
        raise ValueError(f"{mode.value}: missing required inputs {missing}")
    if extra:
        raise ValueError(f"{mode.value}: inputs not used by this mode: {extra}")
