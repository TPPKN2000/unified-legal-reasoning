"""Civil-law simulation (paper §4.3 / Appendix A): rule-based -> abductive -> judge -> rule-based."""
from _common import ROOT, base_parser, llm_spec, save

from ulr import examples as ex
from ulr.court import CivilLawSimulator
from ulr.retrieval import Retriever
from ulr.runtime import build_components

p = base_parser(__doc__)
p.add_argument("--max-rounds", type=int, default=2)
args = p.parse_args()

llm, rule, abd, case, judge = build_components(llm_spec(args), args.scorer, args.judge)
fact, theory = ex.YOUNG_V_HITCHENS, ex.CIVIL_THEORY
if args.rag:
    theory = Retriever(ROOT / "data" / "corpus").suggest_theory(fact, ex.ISSUE) or theory
    print("RAG theory:\n" + theory.render())

result = CivilLawSimulator(rule, abd, judge, max_rounds=args.max_rounds).run(fact, theory, ex.ISSUE)
for s in result.trace:
    print(f"[{s.step}] {s.mode} {s.side or ''} -> {s.parsed}")
print(f"\nOUTCOME: {result.outcome.text} | converged={result.converged}")
for h in result.hypotheses:
    print(" accepted hypothesis:", h.statement)
save(result, args.out)
llm.close()
