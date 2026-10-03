"""Synthetic training records for the scorer (§4.2: 'training examples with appropriate input sequences
and label information', covering rule-based, abductive and case-based scenarios). torch-free.

Record schema (jsonl):
{id, mode, scenario, fact:[...], theory:{head,conditions,exception}, hypothesis: str|null, outcome: str, label: 0|1}
label = 1 iff the (F, T, H, O) quadruple is plausible/consistent.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .components import Fact, Hypothesis, Issue, Outcome, Theory
from .encoding import encode
from .examples import CIVIL_THEORY, ISSUE

# contested element -> hypotheses: (statement, makes_claim_true)
RULE_SCENARIOS = [
    dict(id="fish", facts=["The plaintiff was fishing with a net in an open sea.",
                           "While the net was almost closed, the defendant rowed his boat, entered the net, caught the fish, and rowed his boat out of the net with the fish."],
         hyps=[("The fish were still in the common resource of the open sea until the net was fully closed, so they were not yet the plaintiff's property.", False),
               ("The fish were already confined in the plaintiff's net and under his effective control, so they belonged to the plaintiff.", True)]),
    dict(id="purse", facts=["Bob picked up a purse from a cafe table and walked out with it.", "The purse had Alice's name and phone number written on it."],
         hyps=[("Bob believed the purse was his own because it looked identical to the one he had left there.", False),
               ("Bob read Alice's name on the purse before taking it.", True)]),
    dict(id="bicycle", facts=["Chen rode away on a bicycle that was parked outside a shop.", "The bicycle belonged to Dao."],
         hyps=[("Chen did not intend to take the bicycle away from Dao and meant to leave it where he found it.", False),
               ("Chen planned to sell the bicycle and keep the money.", True)]),
    dict(id="knife", facts=["Minh grabbed a knife from Long's hand.", "Long had been shouting that he would stab a neighbour.", "Minh kept the knife."],
         hyps=[("Minh took the knife only to stop Long from injuring the neighbour.", False),
               ("Minh took the knife because he wanted it for his own collection.", True)]),
    dict(id="phone", facts=["Hoa found a phone on a bus seat and put it in her bag.", "She did not contact anyone about it."],
         hyps=[("The phone was switched off and had no identifying marks, so Hoa could not tell that it belonged to someone.", False),
               ("The lock screen showed the owner's name, which Hoa read before pocketing the phone.", True)]),
    dict(id="coat", holdout=True, facts=["Tuan took a coat from a cloakroom rack and wore it home.", "The cloakroom attendant had tagged the coat as Lan's."],
         hyps=[("Tuan mistook the coat for his own because the two coats were the same model and colour.", False),
               ("Tuan noticed Lan's tag and ignored it.", True)]),
]

# case-based: (present facts, precedent facts, precedent outcome holds, analogy, analogy valid)
CASE_SCENARIOS = [
    dict(id="laptop", present=["Bob took Alice's laptop from her desk while she was away."], prec=["Carl took Dana's phone from her desk while she was away."],
         prec_holds=True, analogy="Both cases involve knowingly taking a portable electronic device that belonged to another person.", valid=True),
    dict(id="laptop-bad", present=["Bob took Alice's laptop from her desk while she was away."], prec=["Carl planted tomatoes in a garden that Dana had left unused."],
         prec_holds=False, analogy="Both cases are about gardening.", valid=False),
    dict(id="deer", holdout=True, present=["Eva shot a deer on land that she had been leasing."], prec=["Finn shot a rabbit on land that he had been leasing."],
         prec_holds=False, analogy="Both cases involve hunting wild animals on land the hunter was entitled to use.", valid=True),
]


def _theory_dict(t: Theory) -> dict:
    return {"head": t.head, "conditions": t.conditions, "exception": t.exception}


def build_records() -> List[Dict]:
    recs: List[Dict] = []
    for s in RULE_SCENARIOS:
        for j, (h, makes_true) in enumerate(s["hyps"]):
            for holds in (True, False):
                recs.append(dict(
                    id=f"{s['id']}-h{j}-{'g' if holds else 'ng'}", mode="rule_based" if j == 0 else "abductive",
                    scenario=s["id"], holdout=bool(s.get("holdout")), fact=s["facts"], theory=_theory_dict(CIVIL_THEORY),
                    hypothesis=h, outcome=(ISSUE.claim if holds else ISSUE.negated_claim),
                    label=int(makes_true == holds)))
    for s in CASE_SCENARIOS:
        flipped = ISSUE.negated_claim if s["prec_holds"] else ISSUE.claim
        same = ISSUE.claim if s["prec_holds"] else ISSUE.negated_claim
        facts = s["present"] + [f"(precedent) {p}" for p in s["prec"]]
        for out, lab in ((same, int(s["valid"])), (flipped, 0)):
            recs.append(dict(
                id=f"{s['id']}-{'same' if out == same else 'flip'}", mode="case_based", scenario=s["id"],
                holdout=bool(s.get("holdout")), fact=facts, theory=_theory_dict(CIVIL_THEORY),
                hypothesis=s["analogy"], outcome=out, label=lab))
    return recs


def record_to_text(r: Dict) -> str:
    t = r["theory"]
    theory = Theory(t["head"], t["conditions"], t.get("exception"))
    hyps = [Hypothesis(statement=r["hypothesis"])] if r.get("hypothesis") else []
    # outcome text -> Outcome with matching holds flag
    holds = r["outcome"] == ISSUE.claim
    return encode(Fact(r["fact"]), theory, hyps, Outcome(ISSUE, holds))


def load_jsonl(path: str) -> List[Dict]:
    return [json.loads(l) for l in Path(path).read_text().splitlines() if l.strip()]


def write_splits(out_dir: str) -> Dict[str, int]:
    recs = build_records()
    p = Path(out_dir)
    p.mkdir(parents=True, exist_ok=True)
    train = [r for r in recs if not r["holdout"]]
    ev = [r for r in recs if r["holdout"]]
    for name, rows in (("train", train), ("eval", ev)):
        (p / f"{name}.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    return {"train": len(train), "eval": len(ev)}
