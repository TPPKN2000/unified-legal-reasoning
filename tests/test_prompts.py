"""Prompts must match the paper's Appendix A/B wording (whitespace-normalised)."""
import re

from ulr import examples as ex
from ulr import prompts
from ulr.components import Outcome


def n(s):
    return re.sub(r"\s+", " ", s).strip()


def test_A1_rule_based():
    expected = (
        "Considering the following facts: 1. The plaintiff was fishing with a net in an open sea. "
        "2. While the net was almost closed, the defendant rowed his boat, entered the net, caught the fish, "
        "and rowed his boat out of the net with the fish. Considering the following rules: A person is guilty "
        "of theft if: 1. the person committed an action to take away the object, 2. the object belonged to "
        "another person, 3. the person knew that the object belonged to the other person, and 4. the person "
        "had an intention to take away the object The rule is not applicable if the purpose of taking away is "
        "to prevent dangers. According to the given rules, please evaluate whether the defendant is guilty of theft."
    )
    assert n(prompts.rule_based(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, ex.ISSUE)) == expected


def test_A2_abductive():
    p = n(prompts.abductive(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, Outcome(ex.ISSUE, False)))
    assert p.endswith("Please suggest hypotheses to support why the outcome of the case might be the defendant is not guilty of theft.")


def test_A3_with_hypothesis():
    p = n(prompts.rule_based(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, ex.ISSUE, [ex.A3_HYPOTHESIS]))
    assert "Assuming these hypotheses are true in this case: The fish were still in the common resource" in p
    assert p.endswith("According to the given rules and hypotheses, please evaluate whether the defendant is guilty of theft.")


def test_B1_case_based_plaintiff():
    p = n(prompts.case_based(ex.YOUNG_V_HITCHENS, ex.KEEBLE_V_HICKERINGILL, ex.ISSUE))
    assert "Considering the precedent case: 1. The plaintiff owned land containing a pond" in p
    assert "The precedent case has the following outcome: the defendant is guilty of theft Please answer why" in p
    assert p.endswith("A person is typically guilty of theft if the following conditions hold: 1. ... 2. ...")
