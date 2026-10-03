"""Common-law simulation (paper §4.3 / Appendix B): case-based -> challenge -> judge -> rule-based."""
from _common import ROOT, base_parser, llm_spec, save

from ulr import examples as ex
from ulr.court import CommonLawSimulator
from ulr.retrieval import Retriever
from ulr.runtime import build_components

p = base_parser(__doc__)
args = p.parse_args()

llm, rule, abd, case, judge = build_components(llm_spec(args), args.scorer, args.judge)
precedents = ex.PRECEDENTS
if args.rag:
    found = Retriever(ROOT / "data" / "corpus").suggest_precedents(ex.YOUNG_V_HITCHENS, ex.ISSUE, k=4)
    by_out = {True: [x for x in found if x.outcome.holds], False: [x for x in found if x.outcome.holds is False]}
    if by_out[True] and by_out[False]:
        precedents = {"plaintiff": by_out[True][0], "defendant": by_out[False][0]}
    print("RAG precedents:", {k: v.name for k, v in precedents.items()})

result = CommonLawSimulator(rule, abd, case, judge).run(ex.YOUNG_V_HITCHENS, ex.ISSUE, precedents)
for s in result.trace:
    print(f"[{s.step}] {s.mode} {s.side or ''}")
print(f"\nOUTCOME: {result.outcome.text} | converged={result.converged} | per side: {result.extra['side_outcomes']}")
for h in result.hypotheses:
    print(" accepted hypothesis:", h.statement)
save(result, args.out)
llm.close()
