"""Aggregate + markdown report for the ALQAC explainability experiment."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def _f(x, d=2):
    return "n/a" if x is None else (f"{x:.{d}f}" if isinstance(x, float) else str(x))


def flat(rec: Dict[str, Any]) -> Dict[str, Optional[float]]:
    m = rec["metrics"]
    j = m.get("llm_judge") or {}
    return {
        "cite_P": m["citation"]["p"], "cite_R": m["citation"]["r"], "cite_F1": m["citation"]["f"],
        "ungiven_cite": m["ungiven_citation_rate"],
        "rougeL_F": m["rouge_l_vs_court"]["f"], "rougeL_R": m["rouge_l_vs_court"]["r"],
        "cov_mean": m["coverage_full"]["mean"], "cov_hyp_only": m["coverage_hyp_only"]["mean"],
        "unsup_num": m["unsupported_numbers"]["rate"],
        "consist_H": None if m["consistency_with_h"] is None else float(m["consistency_with_h"]),
        "consist_base": None if m["consistency_baseline"] is None else float(m["consistency_baseline"]),
        "emb_cov": m.get("embedding_coverage"), "judge": j.get("overall"),
        "leak": rec["leakage"]["ratio"],
    }


COLS = ["cite_P", "cite_R", "cite_F1", "ungiven_cite", "rougeL_F", "cov_mean", "cov_hyp_only", "unsup_num",
        "consist_H", "consist_base", "emb_cov", "judge", "leak"]


def summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows = {r["case_id"]: flat(r) for r in records}
    agg = {c: _mean([v[c] for v in rows.values()]) for c in COLS}
    lift = None
    if agg["consist_H"] is not None and agg["consist_base"] is not None:
        lift = agg["consist_H"] - agg["consist_base"]
    return {"n_cases": len(records), "per_case": rows, "mean": agg, "consistency_lift": lift}


def write_report(records: List[Dict[str, Any]], out_dir: str, run_name: str) -> str:
    s = summarize(records)
    lines = [
        f"# ALQAC-XAI report — run `{run_name}`", "",
        "> **Đây là đánh giá khả năng GIẢI THÍCH.** Outcome được đưa sẵn cho mô hình ở bước abductive; "
        "các chỉ số `consist_*` đo mức giải thích dẫn lại đúng Outcome, không phải độ chính xác dự đoán.", "",
        f"Số vụ: {s['n_cases']}", "",
        "| case | given outcome | " + " | ".join(COLS) + " |", "|---|---|" + "---|" * len(COLS)]
    for r in records:
        f = s["per_case"][r["case_id"]]
        lines.append(f"| {r['case_id']} | {r['given_outcome']} | " + " | ".join(_f(f[c]) for c in COLS) + " |")
    lines.append("| **mean** | | " + " | ".join(_f(s["mean"][c]) for c in COLS) + " |")
    lines += ["", f"Consistency lift (F,T,H so với F,T): {_f(s['consistency_lift'])}", "",
              "Chú giải: cite_* = trích dẫn số điều so với `related_law_provisions`; ungiven_cite = tỉ lệ điều được trích "
              "nhưng không có trong Theory cấp cho mô hình; rougeL_F / cov_* = độ phủ so với `court_reasoning`; "
              "unsup_num = tỉ lệ số liệu không có trong dữ kiện (proxy ảo giác); leak = tỉ lệ câu court_reasoning "
              "đã nằm sẵn trong case_fact (cao ⇒ điểm bị thổi phồng).", "",
              "## Giới hạn", "- Chỉ số từ vựng (ROUGE/độ phủ bigram) là proxy thô; dùng `embed_model`/LLM-judge để bổ sung.",
              "- Ít vụ ⇒ chỉ mang tính mô tả, không có ý nghĩa thống kê.",
              "- Oracle theory dùng điều luật mà tòa đã viện dẫn (rò rỉ có chủ đích); so sánh với `rag`."]
    out = Path(out_dir) / run_name
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")
    md = "\n".join(lines)
    (out / "report.md").write_text(md, encoding="utf-8")
    return md
