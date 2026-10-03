from ulr.examples import ISSUE
from ulr.parsing import extract_json, parse_case_based, parse_hypotheses, parse_verdict

GUILTY = "Let's analyze.\n1. ok\nBased on the provided rules, the defendant appears to be guilty of theft. All four conditions are met."
NOT = "Based on the provided rules and hypotheses, the defendant is likely not guilty of theft.\nThe crucial point is..."


def test_verdict():
    assert parse_verdict(GUILTY, ISSUE) is True
    assert parse_verdict(NOT, ISSUE) is False
    assert parse_verdict("no conclusion here", ISSUE) is None


def test_hypotheses_headed():
    t = ("Hypothesis 1: Lack of Knowledge of Ownership (Condition 3)\nArgument: He did not know. More text.\n\n"
         "Hypothesis 2: Ambiguity of Possession (Condition 2)\nArgument: Fish were in a common resource.\n")
    hs = parse_hypotheses(t)
    assert len(hs) == 2 and hs[1].statement.startswith("Ambiguity of Possession: Fish were")


def test_hypotheses_inline_label():
    hs = parse_hypotheses("Hypothesis 1a (Direct Intention): The defendant intentionally entered the net.\nHypothesis 1b (Reckless Disregard): He was reckless.")
    assert [h.title for h in hs] == ["Direct Intention", "Reckless Disregard"]


def test_hypotheses_numbered_bold():
    hs = parse_hypotheses("1. **The fish were not yet in the plaintiff's possession**: The net was incomplete.\n2. **The plaintiff lacked control over the fish**: Open sea.")
    assert len(hs) == 2 and "possession" in hs[0].statement


def test_case_based():
    t = ("A person is typically guilty of theft if the following conditions hold:\n1. They take property.\n2. It had value.\n\n"
         "Rule-Based Explanation:\nBoth cases involve X.")
    th, h = parse_case_based(t, ISSUE)
    assert th.conditions == ["They take property.", "It had value."] and h.statement == "Both cases involve X."


def test_json():
    assert extract_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert extract_json("nope") is None
