"""Regenerate data/logit/{train,eval}.jsonl (synthetic F/T/H/O training records for the §4.2 scorer)."""
from _common import ROOT

from ulr.synthetic import write_splits

print(write_splits(str(ROOT / "data" / "logit")))
