"""Deterministic offline backend: lets the whole framework flow be tested without a GPU/API.

The canned answers are in the style of the paper's appendices (own wording, shortened).
"""
from __future__ import annotations

import json
from typing import Optional

from .base import LLMBackend

_GUILTY = (
    "Let's analyze the situation based on the provided rules.\n"
    "1. The defendant took the fish. 2. The fish were in the plaintiff's net. "
    "3. The defendant saw the net. 4. The defendant entered the net intentionally.\n"
    "Based on the provided rules, the defendant appears to be guilty of theft. "
    "No danger-prevention exception applies."
)
_NOT_GUILTY = (
    "Based on the provided rules and hypotheses, the defendant is not guilty of theft. "
    "The element that the object belonged to another person is missing, because the fish were not yet "
    "the plaintiff's property."
)
_HYP_NOT_GUILTY = (
    "Several hypotheses could support a finding of not guilty:\n\n"
    "Hypothesis 1: Lack of Knowledge of Ownership (Condition 3)\n"
    "Argument: The defendant may have believed the fish were free for anyone to take, since the net was "
    "not clearly marked.\n\n"
    "Hypothesis 2: Ambiguity of Possession (Condition 2)\n"
    "Argument: The fish were still in the open sea, a common resource, until the net was fully closed, "
    "so they were not yet the plaintiff's property.\n"
)
_HYP_GUILTY = (
    "Several hypotheses could support a finding of guilt:\n\n"
    "Hypothesis 1: Deliberate Appropriation (Condition 4)\n"
    "Argument: The defendant rowed straight into a visible net and removed the fish, which shows intent "
    "to take them.\n\n"
    "Hypothesis 2: Possession Through Effort (Condition 2)\n"
    "Argument: The plaintiff's almost-closed net already gave him effective control over the fish.\n"
)
_CASE_GUILTY = (
    "A person is typically guilty of theft if the following conditions hold:\n"
    "1. They intentionally and without consent take property under another person's control.\n"
    "2. That property has economic value to the owner.\n\n"
    "Rule-Based Explanation:\n"
    "Both cases involve interference with property that the plaintiff was in the process of acquiring "
    "for profit, so the current case may share the precedent's outcome."
)
_CASE_NOT_GUILTY = (
    "A person is typically guilty of theft if the following conditions hold:\n"
    "1. They unlawfully appropriate property belonging to another.\n"
    "2. That property has been reduced to possession by the owner.\n\n"
    "Rule-Based Explanation:\n"
    "Both cases concern wild animals that the claimant had not yet reduced to possession, so the "
    "property was not 'belonging to another' when it was taken."
)


class MockBackend(LLMBackend):
    def __init__(self, name: str = "mock", **_):
        self.name = name

    def generate(self, prompt: str, system: Optional[str] = None, max_new_tokens=None, temperature=None) -> str:
        p = prompt
        if "You are a legal expert evaluating AI model responses" in p:
            resp = p.split("RESPONSE TO EVALUATE:")[1].split("EVALUATION CRITERIA:")[0]
            base = 3 + (len(resp) % 3)  # 3..5, deterministic
            crit = ["reasonableness", "completeness", "clarity", "logical_structure", "framework_adherence"]
            out = {c: {"score": min(5, base + (i % 2)), "explanation": "mock"} for i, c in enumerate(crit)}
            out["overall_score"] = sum(v["score"] for v in out.values()) / 5
            out["overall_comment"] = "mock judge"
            return json.dumps(out)
        if p.startswith("Given the following legal analysis"):
            analysis = p.split("Analysis:", 1)[1].lower()
            return "NO" if "not guilty" in analysis else "YES"
        if "You are presiding over a court" in p:
            return "1"
        if "Please suggest hypotheses" in p:
            return _HYP_NOT_GUILTY if "might be the defendant is not guilty" in p else _HYP_GUILTY
        if "Please answer why the current case might have the same outcome" in p:
            return _CASE_GUILTY if "following outcome: the defendant is guilty of theft" in p else _CASE_NOT_GUILTY
        if "Assuming these hypotheses are true" in p:
            h = p.split("Assuming these hypotheses are true in this case:")[1].lower()
            if any(k in h for k in ("not yet", "common resource", "unowned", "not in the plaintiff")):
                return _NOT_GUILTY
            return _GUILTY
        if "please evaluate whether" in p:
            return _GUILTY
        return "OK"
