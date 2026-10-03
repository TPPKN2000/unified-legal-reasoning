"""Resumable evaluation pipeline: generate -> judge -> report. Every step checkpoints to JSON so an
interrupted Colab session (or an exhausted quota) can continue where it stopped."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from ..llm import build_backend, spec_name
from .judge import LLMJudgeScorer
from .tasks import EvalTask


def _load(path: Path) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def _save(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
    tmp.replace(path)


def generate_all(candidates: List[Dict[str, Any]], tasks: List[EvalTask], out_dir: str, log=print) -> dict:
    """responses.json: {model: {task_id: response}} — models are loaded one at a time (T4 memory)."""
    path = Path(out_dir) / "responses.json"
    results = _load(path)
    for spec in candidates:
        name = spec_name(spec)
        done = results.setdefault(name, {})
        todo = [t for t in tasks if t.id not in done]
        if not todo:
            log(f"[generate] {name}: already complete")
            continue
        log(f"[generate] {name}: {len(todo)} task(s)")
        llm = build_backend(spec)
        try:
            for t in todo:
                done[t.id] = llm.generate(t.prompt)
                _save(path, results)
        finally:
            llm.close()
    return results


def judge_all(judges: List[Dict[str, Any]], tasks: List[EvalTask], out_dir: str, log=print) -> dict:
    """scores.json: {judge: {model: {task_id: {criterion: score, overall: mean}}}}"""
    rpath, spath = Path(out_dir) / "responses.json", Path(out_dir) / "scores.json"
    responses, scores = _load(rpath), _load(spath)
    prompts = {t.id: t.prompt for t in tasks}
    for spec in judges:
        jname = spec_name(spec)
        jscores = scores.setdefault(jname, {})
        pending = [(m, tid) for m, r in responses.items() for tid in r if tid not in jscores.get(m, {})]
        if not pending:
            log(f"[judge] {jname}: already complete")
            continue
        log(f"[judge] {jname}: {len(pending)} response(s)")
        llm = build_backend(spec)
        scorer = LLMJudgeScorer(llm)
        try:
            for m, tid in pending:
                s = scorer.score(prompts[tid], responses[m][tid])
                if s is None:
                    log(f"  ! could not parse judge output for {m}/{tid} (skipped)")
                    continue
                jscores.setdefault(m, {})[tid] = s
                _save(spath, scores)
        finally:
            llm.close()
    return scores
