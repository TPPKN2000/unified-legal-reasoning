"""Sanity-check ALQAC-format data before running anything: schema, sizes, provision resolvability, leakage."""
import argparse

from _common import ROOT

from ulr.alqac.laws import LawIndex, load_aliases
from ulr.alqac.metrics import leakage
from ulr.alqac.schema import load_cases, load_corpus

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--cases", default=str(ROOT / "data/alqac/ALQAC_public_test_sample.json"))
p.add_argument("--corpus", default=str(ROOT / "data/alqac/corpus_law_pub_sample.json"))
p.add_argument("--aliases", default=str(ROOT / "data/alqac/law_aliases.json"))
a = p.parse_args()

cases, arts = load_cases(a.cases), load_corpus(a.corpus)
idx = LawIndex(arts, load_aliases(a.aliases))
print(f"{len(cases)} cases | {len(arts)} law articles in corpus ({len({x.law_id for x in arts})} laws, "
      f"{sum(x.article_no is not None for x in arts)} with a parsable article number)")
print(f"{'case':<10}{'label':<15}{'fact_chars':>11}{'provisions':>11}{'resolvable':>11}{'leakage':>9}")
for c in cases:
    ok, num, tot = idx.coverage([c])
    lk = leakage(c.case_fact, c.reference_reasoning)
    print(f"{c.case_id:<10}{c.verdict_label:<15}{len(c.case_fact):>11}{tot:>11}{ok:>11}{lk['ratio']:>9.2f}")
ok, num, tot = idx.coverage(cases)
print(f"\nprovisions resolvable to article text: {ok}/{tot} (with article number: {num}).")
if ok == 0:
    print("-> theory_source=oracle will use citation LABELS only (no article text); "
          "provide a corpus whose articles expose 'Điều N' (or an article_no field) and extend law_aliases.json.")
