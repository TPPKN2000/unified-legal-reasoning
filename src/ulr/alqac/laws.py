"""Resolve provisions ('Bộ luật dân sự năm 2015 | Điều 584') to article text, and BM25 retrieval over articles."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from ..retrieval import BM25, _tok
from .schema import AlqacCase, LawArticle, Provision


def norm_law(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w/\-]+", " ", s.lower())).strip()


def load_aliases(path: Optional[str | Path]) -> Dict[str, str]:
    if not path or not Path(path).exists():
        return {}
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return {norm_law(k): v for k, v in raw.items() if not k.startswith("_")}


class LawIndex:
    def __init__(self, articles: Sequence[LawArticle], aliases: Optional[Dict[str, str]] = None):
        self.articles = list(articles)
        self.aliases = aliases or {}
        self.by_key = {(a.law_id, a.article_no): a for a in self.articles if a.article_no is not None}

    def law_id(self, law_name: str) -> Optional[str]:
        return self.aliases.get(norm_law(law_name))

    def resolve(self, p: Provision) -> Optional[LawArticle]:
        lid = self.law_id(p.law)
        if lid is None or p.article is None:
            return None
        return self.by_key.get((lid, p.article))

    def coverage(self, cases: Sequence[AlqacCase]) -> Tuple[int, int, int]:
        """(resolvable provisions, provisions with article number, all provisions)"""
        ok = num = tot = 0
        for c in cases:
            for p in c.provisions:
                tot += 1
                num += p.article is not None
                ok += self.resolve(p) is not None
        return ok, num, tot


def vi_tokens(s: str) -> List[str]:
    t = _tok(s)
    return t + [f"{a}_{b}" for a, b in zip(t, t[1:])]  # unigrams + bigrams (Vietnamese words are multi-syllable)


class LawRetriever:
    def __init__(self, articles: Sequence[LawArticle]):
        self.articles = list(articles)
        self.index = BM25([a.text for a in self.articles], tokenizer=vi_tokens)

    def search(self, query: str, k: int = 5) -> List[LawArticle]:
        sc = self.index.scores(query)
        ranked = sorted(zip(sc, self.articles), key=lambda x: -x[0])
        return [a for s, a in ranked if s > 0][:k]
