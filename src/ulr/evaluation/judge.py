"""LLM-as-a-Judge (paper §4.4, [84]): five criteria, each 1-5, overall = average."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from ..parsing import extract_json

CRITERIA = ["reasonableness", "completeness", "clarity", "logical_structure", "framework_adherence"]

JUDGE_PROMPT = """You are a legal expert evaluating AI model responses for legal reasoning quality.

ORIGINAL PROMPT: {original_prompt}

RESPONSE TO EVALUATE: {response_to_evaluate}

EVALUATION CRITERIA:
1. Reasonableness: Logic and soundness of legal reasoning
2. Completeness: Addresses all relevant factors and conditions
3. Clarity: Clear and understandable presentation
4. Logical Structure: Coherent chain of reasoning
5. Framework Adherence: Follows required legal reasoning framework

RESPONSE FORMAT: Respond only in JSON format:
{
 "reasonableness": {"score": [1-5], "explanation": "Brief explanation"},
 "completeness": {"score": [1-5], "explanation": "Brief explanation"},
 "clarity": {"score": [1-5], "explanation": "Brief explanation"},
 "logical_structure": {"score": [1-5], "explanation": "Brief explanation"},
 "framework_adherence": {"score": [1-5], "explanation": "Brief explanation"},
 "overall_score": [average score],
 "overall_comment": "Overall assessment of the response"
}"""


def build_judge_prompt(original_prompt: str, response: str) -> str:
    return JUDGE_PROMPT.replace("{original_prompt}", original_prompt).replace("{response_to_evaluate}", response)


def parse_scores(text: str) -> Optional[Dict[str, float]]:
    """Return {criterion: score, ..., overall: mean} or None if unparsable."""
    data = extract_json(text)
    if not isinstance(data, dict):
        return None
    scores: Dict[str, float] = {}
    for c in CRITERIA:
        v = data.get(c)
        s = v.get("score") if isinstance(v, dict) else v
        try:
            s = float(s)
        except (TypeError, ValueError):
            return None
        if not 1 <= s <= 5:
            return None
        scores[c] = s
    scores["overall"] = sum(scores[c] for c in CRITERIA) / len(CRITERIA)  # recomputed: do not trust the judge's own mean
    return scores


class LLMJudgeScorer:
    def __init__(self, llm, retries: int = 2):
        self.llm, self.retries = llm, retries

    def score(self, original_prompt: str, response: str) -> Optional[Dict[str, float]]:
        p = build_judge_prompt(original_prompt, response)
        for attempt in range(self.retries + 1):
            out = self.llm.generate(p, temperature=0.0 if attempt == 0 else 0.3, max_new_tokens=700)
            s = parse_scores(out)
            if s:
                return s
        return None
