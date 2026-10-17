import json
from pathlib import Path

import pytest

from ulr.alqac import metrics as M
from ulr.alqac.adapter import build_fact, build_issue, build_outcome, build_theory, clean_query
from ulr.alqac.laws import LawIndex, LawRetriever, load_aliases
from ulr.alqac.schema import FORBIDDEN_INPUT_FIELDS, load_cases, load_corpus, parse_provisions
from ulr.alqac.xai import XAIConfig, run_all
from ulr.llm import build_backend
from ulr.parsing import parse_hypotheses
from ulr.reasoners import AbductiveReasoner, RuleBasedReasoner

D = Path("data/alqac")


@pytest.fixture(scope="module")
def cases():
    return load_cases(D / "ALQAC_public_test_sample.json")


def test_load_sample(cases):
    assert [c.case_id for c in cases] == ["case_4704", "case_4101", "case_950", "case_4557"]
    assert {c.verdict_label for c in cases} == {"A_WIN", "PARTIAL_A_WIN", "B_WIN"}


def test_bad_label_rejected(tmp_path):
    p = tmp_path / "x.json"
    p.write_text(json.dumps([{"case_id": "c", "case_fact": "f", "case_query": "q", "verdict_label": "MAYBE"}]))
    with pytest.raises(ValueError, match="verdict_label"):
        load_cases(p)


def test_parse_provisions(cases):
    p = cases[0].provisions
    assert len(p) == 11 and p[0].article == 26 and p[-1].article is None  # Pháp lệnh về án phí: no article
    assert parse_provisions("Luật Xây dựng năm 2014| Điều 138\nLuật Xây dựng năm 2014| Điều 138")[0].law == "Luật Xây dựng năm 2014"


def test_corpus_aid_is_not_article_number():
    arts = load_corpus(D / "corpus_law_pub_sample.json")
    assert [a.aid for a in arts] == [270, 57130] and all(a.article_no is None for a in arts)


def test_inputs_never_contain_reference_fields(cases):
    """court_reasoning / court_verdict / judgment_text must never reach a prompt (they are scoring references)."""
    raw = json.loads((D / "ALQAC_public_test_sample.json").read_text())
    c, r = cases[1], raw[1]
    fact, _ = build_fact(c)
    theory, _ = build_theory(c, "oracle")
    blob = fact.render() + theory.render() + build_outcome(c).text
    for f in FORBIDDEN_INPUT_FIELDS:
        probe = r[f].strip()[:120]
        assert probe not in blob


def test_query_instruction_removed(cases):
    assert "Agent" not in clean_query(cases[0].case_query)


def test_outcome_text_and_graded_label(cases):
    assert "một phần" in build_outcome(cases[1]).text
    assert "không chấp nhận" in build_outcome(cases[2]).text and build_outcome(cases[2]).holds is False


def test_oracle_theory_falls_back_to_labels(cases):
    idx = LawIndex(load_corpus(D / "corpus_law_pub_sample.json"), load_aliases(D / "law_aliases.json"))
    th, meta = build_theory(cases[1], "oracle", idx)
    assert meta["n_with_text"] == 0 and th.conditions[0].endswith("Điều 584")


def test_rag_theory_uses_corpus(cases):
    arts = load_corpus(D / "corpus_law_pub_sample.json")
    fact, _ = build_fact(cases[0])
    th, meta = build_theory(cases[0], "rag", None, LawRetriever(arts), fact)
    assert th.conditions and meta["source"] == "rag"


def test_vietnamese_hypothesis_headings():
    hs = parse_hypotheses("Giả thuyết 1: Thiếu chứng cứ (Điều 91)\nLập luận: Nguyên đơn chưa chứng minh được thiệt hại.\n")
    assert len(hs) == 1 and "Nguyên đơn chưa chứng minh" in hs[0].statement + hs[0].argument


def test_metrics():
    assert M.cited_articles("Điều 584, Điều 558, 590 và Điều 603") == {584, 558, 590, 603}
    assert M.prf({1, 2}, {2, 3})["p"] == 0.5
    u = M.unsupported_numbers("Bồi thường 3.437.500đ và 9.999.000đ vào ngày 22/9/2017", ["3.437.500đ, 22/9/2017"])
    assert u["unsupported"] == ["9999000"]
    assert M.classify_label_vi("Tòa án có chấp nhận hay không? Do đó, chấp nhận một phần yêu cầu.") == "PARTIAL_A_WIN"
    assert M.classify_label_vi("Như vậy yêu cầu của nguyên đơn không được chấp nhận.") == "B_WIN"
    assert M.classify_label_vi("không liên quan") is None


def test_leakage_and_decontaminate():
    fact = "Cụ A chết năm 1984 và cụ B chết năm 2005, hàng thừa kế thứ nhất gồm bốn người con.\nNguyên đơn khởi kiện chia di sản."
    ref = "Cụ A chết năm 1984 và cụ B chết năm 2005, hàng thừa kế thứ nhất gồm bốn người con."
    assert M.leakage(fact, ref)["n_leaked"] == 1
    assert "hàng thừa kế" not in M.decontaminate(fact, ref) and "khởi kiện" in M.decontaminate(fact, ref)


def test_pipeline_mock_resumable(cases, tmp_path):
    llm = build_backend({"type": "mock"})
    rule, abd = RuleBasedReasoner(llm, classifier_fallback=False), AbductiveReasoner(llm)
    cfg = XAIConfig(out_dir=str(tmp_path), top_k_hypotheses=2)
    idx = LawIndex(load_corpus(D / "corpus_law_pub_sample.json"))
    r1 = run_all(cases[:2], rule, abd, cfg, idx, None, log=lambda *_: None)
    assert r1[0]["metrics"]["n_hypotheses"] == 2 and "citation" in r1[0]["metrics"]
    assert "abductive" in r1[0] and r1[0]["given_outcome"] == "A_WIN"
    lines = (tmp_path / "oracle" / "records.jsonl").read_text().splitlines()
    run_all(cases[:2], rule, abd, cfg, idx, None, log=lambda *_: None)  # nothing re-run
    assert (tmp_path / "oracle" / "records.jsonl").read_text().splitlines() == lines
