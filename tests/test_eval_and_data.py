import json

from ulr.evaluation import build_tasks
from ulr.evaluation.judge import build_judge_prompt, parse_scores
from ulr.evaluation.report import make_report
from ulr.evaluation.runner import generate_all, judge_all
from ulr.retrieval import Retriever
from ulr.synthetic import build_records, record_to_text
from ulr import examples as ex


def test_eight_tasks_3_3_2():
    t = build_tasks()
    modes = [x.mode for x in t]
    assert len(t) == 8 and modes.count("rule_based") == 3 and modes.count("abductive") == 3 and modes.count("case_based") == 2


def test_judge_prompt_and_parse():
    p = build_judge_prompt("Q?", "A.")
    assert "ORIGINAL PROMPT: Q?" in p and "RESPONSE TO EVALUATE: A." in p and '"framework_adherence"' in p
    ok = {c: {"score": 4, "explanation": "x"} for c in ["reasonableness", "completeness", "clarity", "logical_structure", "framework_adherence"]}
    s = parse_scores("```json\n" + json.dumps(ok) + "\n```")
    assert s["overall"] == 4.0
    ok["clarity"]["score"] = 9
    assert parse_scores(json.dumps(ok)) is None


def test_pipeline_resumable(tmp_path):
    t = build_tasks()
    out = str(tmp_path)
    generate_all([{"type": "mock", "name": "m"}], t, out, log=lambda *_: None)
    r1 = json.loads((tmp_path / "responses.json").read_text())
    r2 = generate_all([{"type": "mock", "name": "m"}], t, out, log=lambda *_: None)  # nothing to redo
    assert r1 == r2
    judge_all([{"type": "mock", "name": "j"}], t, out, log=lambda *_: None)
    md = make_report(out, {x.id: x.mode for x in t})
    assert "| m |" in md and (tmp_path / "fig4_ranking.png").exists() and (tmp_path / "fig5_heatmap.png").exists()


def test_retrieval():
    R = Retriever("data/corpus")
    assert R.suggest_theory(ex.YOUNG_V_HITCHENS, ex.ISSUE).head.startswith("A person is guilty of theft")
    assert {p.name for p in R.suggest_precedents(ex.YOUNG_V_HITCHENS, ex.ISSUE, k=2)} == {"Keeble v. Hickeringill", "Pierson v. Post"}


def test_synthetic_records():
    recs = build_records()
    assert {r["mode"] for r in recs} == {"rule_based", "abductive", "case_based"}
    assert any(r["holdout"] for r in recs) and any(not r["holdout"] for r in recs)
    assert "[FACT]" in record_to_text(recs[0]) and "[OUTCOME]" in record_to_text(recs[0])
