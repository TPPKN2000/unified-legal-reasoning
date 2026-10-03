import pytest

from ulr import examples as ex
from ulr.components import Outcome
from ulr.court import CivilLawSimulator, CommonLawSimulator
from ulr.modes import Mode, check_inputs
from ulr.runtime import build_components


def test_mode_contract():
    check_inputs(Mode.RULE_BASED, fact=1, theory=1)
    check_inputs(Mode.RULE_BASED, fact=1, theory=1, hypothesis=[1])
    with pytest.raises(ValueError):
        check_inputs(Mode.ABDUCTIVE, fact=1, theory=1)  # outcome missing
    with pytest.raises(ValueError):
        check_inputs(Mode.CASE_BASED, fact_present=1, fact_precedent=1, outcome=1, theory=1)  # theory is an output


def test_civil_flow_matches_appendix_A():
    _, rule, abd, case, judge = build_components({"type": "mock"}, None, "paper")
    r = CivilLawSimulator(rule, abd, judge).run(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, ex.ISSUE)
    steps = [s.step for s in r.trace]
    assert steps[:4] == ["A.1", "A.2#1", "judge#1", "A.3#1"]  # A.1 -> A.2 -> judge -> A.3
    assert r.trace[0].parsed["outcome"] == "the defendant is guilty of theft"
    assert r.outcome.holds is False and r.converged and len(r.hypotheses) == 1


def test_civil_judge_rejects_all_keeps_outcome():
    _, rule, abd, case, judge = build_components({"type": "mock"}, None, "reject")
    r = CivilLawSimulator(rule, abd, judge).run(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, ex.ISSUE)
    assert r.outcome.holds is True and r.converged and r.hypotheses == []


def test_common_flow_matches_appendix_B():
    _, rule, abd, case, judge = build_components({"type": "mock"}, None, "paper")
    r = CommonLawSimulator(rule, abd, case, judge).run(ex.YOUNG_V_HITCHENS, ex.ISSUE, ex.PRECEDENTS)
    steps = [s.step for s in r.trace]
    assert steps == ["B.1", "B.1", "B.2", "B.2", "judge", "B.3", "B.3"]
    assert r.converged and r.outcome.holds is False


def test_scorer_hook_called():
    class S:
        def score(self, *a):
            return 1.5

    _, rule, abd, case, judge = build_components({"type": "mock"}, None, "paper")
    rule.scorer = S()
    assert rule.run(ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY, ex.ISSUE).score == 1.5
