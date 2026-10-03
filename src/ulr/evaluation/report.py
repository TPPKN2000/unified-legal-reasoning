"""Aggregation + figures: Fig. 4 (overall ranking) and Fig. 5 (model x criterion heatmap)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .judge import CRITERIA

HEATMAP_ORDER = sorted(CRITERIA)  # clarity, completeness, framework_adherence, logical_structure, reasonableness


def aggregate(scores: dict) -> Dict[str, Dict[str, float]]:
    """-> {model: {criterion: mean over tasks & judges, 'overall': mean of criteria}}"""
    acc: Dict[str, Dict[str, List[float]]] = {}
    for judge_scores in scores.values():
        for model, tasks in judge_scores.items():
            for s in tasks.values():
                for c in CRITERIA:
                    acc.setdefault(model, {}).setdefault(c, []).append(s[c])
    out = {}
    for m, d in acc.items():
        out[m] = {c: sum(v) / len(v) for c, v in d.items()}
        out[m]["overall"] = sum(out[m][c] for c in CRITERIA) / len(CRITERIA)
    return out


def by_mode(scores: dict, task_modes: Dict[str, str]) -> Dict[str, Dict[str, float]]:
    acc: Dict[str, Dict[str, List[float]]] = {}
    for js in scores.values():
        for model, tasks in js.items():
            for tid, s in tasks.items():
                acc.setdefault(model, {}).setdefault(task_modes[tid], []).append(s["overall"])
    return {m: {k: sum(v) / len(v) for k, v in d.items()} for m, d in acc.items()}


def make_report(out_dir: str, task_modes: Dict[str, str]) -> str:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    out = Path(out_dir)
    scores = json.loads((out / "scores.json").read_text())
    agg = aggregate(scores)
    if not agg:
        raise RuntimeError("no scores to report")
    ranking = sorted(agg.items(), key=lambda kv: kv[1]["overall"])  # ascending -> best on top in barh

    # Fig. 4
    fig, ax = plt.subplots(figsize=(8, 0.7 * len(ranking) + 1.5))
    names = [m for m, _ in ranking]
    vals = [d["overall"] for _, d in ranking]
    bars = ax.barh(names, vals, color=plt.cm.viridis(np.linspace(0.2, 0.9, len(vals))))
    for b, v in zip(bars, vals):
        ax.text(v + 0.03, b.get_y() + b.get_height() / 2, f"{v:.2f}", va="center", fontsize=9)
    ax.set_xlim(0, 5.3)
    ax.set_xlabel("Average Score")
    ax.set_title("Model Performance Ranking")
    fig.tight_layout()
    fig.savefig(out / "fig4_ranking.png", dpi=150)
    plt.close(fig)

    # Fig. 5
    mat = np.array([[agg[m][c] for c in HEATMAP_ORDER] for m in reversed(names)])
    fig, ax = plt.subplots(figsize=(9, 0.7 * len(names) + 2.5))
    im = ax.imshow(mat, cmap="YlGnBu", vmin=3.0, vmax=5.0, aspect="auto")
    ax.set_xticks(range(len(HEATMAP_ORDER)), HEATMAP_ORDER, rotation=90)
    ax.set_yticks(range(len(names)), list(reversed(names)))
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f"{mat[i, j]:.2f}", ha="center", va="center", fontsize=8)
    fig.colorbar(im, label="Average Score")
    ax.set_title("LLM Performance Across Legal Reasoning Criteria")
    fig.tight_layout()
    fig.savefig(out / "fig5_heatmap.png", dpi=150)
    plt.close(fig)

    # markdown summary
    bm = by_mode(scores, task_modes)
    lines = ["| model | overall | " + " | ".join(HEATMAP_ORDER) + " | rule | abductive | case |", "|---|---|" + "---|" * (len(HEATMAP_ORDER) + 3)]
    for m, d in reversed(ranking):
        row = [f"{d['overall']:.2f}"] + [f"{d[c]:.2f}" for c in HEATMAP_ORDER]
        row += [f"{bm.get(m, {}).get(k, float('nan')):.2f}" for k in ("rule_based", "abductive", "case_based")]
        lines.append(f"| {m} | " + " | ".join(row) + " |")
    md = "\n".join(lines)
    (out / "results.md").write_text(md + "\n")
    return md
