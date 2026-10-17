"""ALQAC case -> framework components (Fact, Theory, Outcome). Only ALLOWED_INPUT_FIELDS are ever used."""
from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

from ..components import Fact, Issue, Outcome, Theory
from .laws import LawIndex, LawRetriever
from .metrics import decontaminate
from .schema import AlqacCase, Provision

THEORY_HEAD = "Các quy định pháp luật được áp dụng:"


def clean_query(q: str) -> str:
    """case_query ends with a task instruction ('Agent dự đoán …?') — remove it: we do not ask for a prediction."""
    return re.sub(r"\s*Agent dự đoán[^?]*\??\s*$", "", q).strip()


def build_issue(case: AlqacCase) -> Issue:
    a = case.A_role.lower()
    return Issue(
        claim=f"Tòa án có chấp nhận yêu cầu khởi kiện của {a} hay không (chấp nhận toàn bộ, chấp nhận một phần hoặc không chấp nhận)",
        negated_claim=f"Tòa án không chấp nhận yêu cầu khởi kiện của {a}",
        theory_head=THEORY_HEAD,
    )


def build_outcome(case: AlqacCase, issue: Optional[Issue] = None) -> Outcome:
    """The GIVEN outcome (ground-truth label used as input to the abductive mode, not predicted)."""
    issue = issue or build_issue(case)
    a = case.A_role.lower()
    return {
        "A_WIN": Outcome(issue, True, f"Tòa án chấp nhận toàn bộ yêu cầu khởi kiện của {a}"),
        "PARTIAL_A_WIN": Outcome(issue, True, f"Tòa án chấp nhận một phần yêu cầu khởi kiện của {a}"),
        "B_WIN": Outcome(issue, False, f"Tòa án không chấp nhận yêu cầu khởi kiện của {a}"),
    }[case.verdict_label]


def build_fact(case: AlqacCase, max_chars: int = 16000, decon: bool = False) -> Tuple[Fact, Dict]:
    text = case.case_fact
    if decon:
        text = decontaminate(text, case.reference_reasoning)
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    summary = clean_query(case.case_query)
    stmts, used, truncated = [f"Tóm tắt tranh chấp: {summary}"], 0, False
    for p in paras:
        if used + len(p) > max_chars:
            truncated = True
            room = max_chars - used
            cut = p[:room]
            end = max(cut.rfind(". "), cut.rfind("; "), cut.rfind("\n"))
            if end > 200:  # keep a sentence-aligned prefix of the paragraph that overflows the budget
                stmts.append(cut[: end + 1] + " [...]")
                used += end + 1
            break
        stmts.append(p)
        used += len(p)
    return Fact(stmts, name=case.case_id), {"truncated": truncated, "chars": used, "decontaminated": decon}


def _provision_label(p: Provision) -> str:
    return f"{p.law}, Điều {p.article}" if p.article is not None else p.law


def build_theory(case: AlqacCase, source: str, index: Optional[LawIndex] = None,
                 retriever: Optional[LawRetriever] = None, fact: Optional[Fact] = None,
                 rag_k: int = 5, max_chars: int = 600) -> Tuple[Theory, Dict]:
    """oracle: the provisions cited by the court (article text when the corpus can resolve it, otherwise the citation
    label only).  rag: BM25 over the law corpus using the dispute summary + facts."""
    meta: Dict = {"source": source}
    if source == "oracle":
        conds, resolved = [], 0
        for p in case.provisions:
            art = index.resolve(p) if index else None
            if art is not None:
                resolved += 1
                conds.append(f"{_provision_label(p)}: {art.text[:max_chars]}")
            else:
                conds.append(_provision_label(p))
        meta.update(n_provisions=len(conds), n_with_text=resolved)
        return Theory(THEORY_HEAD, conds), meta
    if source == "rag":
        if retriever is None:
            raise ValueError("theory_source=rag needs a corpus (alqac.corpus)")
        query = clean_query(case.case_query) + " " + " ".join((fact.statements if fact else [])[:3])
        hits = retriever.search(query, k=rag_k)
        conds = [f"[{a.law_id}, aid {a.aid}] {a.text[:max_chars]}" for a in hits]
        meta.update(retrieved_aids=[a.aid for a in hits], retrieved_law_ids=sorted({a.law_id for a in hits}))
        if index is not None:
            gold = {a.aid for a in (index.resolve(p) for p in case.provisions) if a}
            meta["retrieval_hit"] = (len(gold & set(meta["retrieved_aids"])) / len(gold)) if gold else None
        return Theory(THEORY_HEAD, conds or ["(không truy xuất được quy định liên quan)"]), meta
    raise ValueError(f"unknown theory source {source!r} (oracle | rag)")
