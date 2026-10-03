"""RAG component (paper §4.2): retrieve statutes / precedents from an external corpus (BM25, no deps)."""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional

from .components import Fact, Issue, Outcome, Precedent, Theory

_STOP = set("a an the of to in on and or is was were be by for with as at that this it its from their his her he she".split())


def _tok(s: str) -> List[str]:
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in _STOP]


class BM25:
    def __init__(self, docs: List[str], k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.toks = [_tok(d) for d in docs]
        self.N = len(docs)
        self.avgdl = sum(len(t) for t in self.toks) / max(1, self.N)
        df = Counter(w for t in self.toks for w in set(t))
        self.idf = {w: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for w, n in df.items()}
        self.tf = [Counter(t) for t in self.toks]

    def scores(self, query: str) -> List[float]:
        q = _tok(query)
        out = []
        for tf, toks in zip(self.tf, self.toks):
            s = 0.0
            for w in q:
                if w in tf:
                    f = tf[w]
                    s += self.idf.get(w, 0) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * len(toks) / self.avgdl))
            out.append(s)
        return out


class Retriever:
    """Corpus format (jsonl): {id, type: statute|case, title, text, [conditions, exception, head, facts, outcome_holds]}"""

    def __init__(self, corpus_dir: str | Path):
        self.docs: List[Dict] = []
        for f in sorted(Path(corpus_dir).glob("*.jsonl")):
            for line in f.read_text().splitlines():
                if line.strip():
                    self.docs.append(json.loads(line))
        self.index = BM25([d["title"] + " " + d["text"] for d in self.docs])

    def search(self, query: str, k: int = 3, type: Optional[str] = None) -> List[Dict]:
        sc = self.index.scores(query)
        ranked = sorted(zip(sc, self.docs), key=lambda x: -x[0])
        return [d for s, d in ranked if s > 0 and (type is None or d["type"] == type)][:k]

    # --- helpers that map retrieved documents to framework components ---
    def suggest_theory(self, fact: Fact, issue: Issue) -> Optional[Theory]:
        hits = self.search(" ".join(fact.statements) + " " + issue.claim, k=1, type="statute")
        if not hits:
            return None
        d = hits[0]
        return Theory(head=d.get("head", issue.theory_head), conditions=d["conditions"], exception=d.get("exception"))

    def suggest_precedents(self, fact: Fact, issue: Issue, k: int = 2) -> List[Precedent]:
        out = []
        for d in self.search(" ".join(fact.statements), k=k, type="case"):
            out.append(
                Precedent(d["title"], Fact(d["facts"], name=d["title"]), Outcome(issue, d.get("outcome_holds")))
            )
        return out
