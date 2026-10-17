"""OPTIONAL LLM-as-a-Judge with an explanation-specific rubric (extension, not in the paper; gated behind a flag).
The court's reasoning is given to the judge as reference."""
from __future__ import annotations

from typing import Dict, Optional

from ..parsing import extract_json

XAI_CRITERIA = ["faithfulness_to_facts", "legal_grounding", "coverage_of_court_reasoning", "logical_structure", "clarity"]

XAI_JUDGE_PROMPT = """You are a legal expert evaluating how well an AI model EXPLAINS a known court outcome. The model was GIVEN the outcome; do not judge whether the outcome is right, judge the explanation.

CASE FACTS (as given to the model): {facts}

GIVEN OUTCOME: {outcome}

REFERENCE COURT REASONING (for comparison only): {reference}

EXPLANATION TO EVALUATE: {explanation}

EVALUATION CRITERIA (score each 1-5):
1. Faithfulness to facts: every factual claim is supported by the case facts; no invented facts, parties or amounts
2. Legal grounding: relies on appropriate legal provisions/principles and cites them correctly
3. Coverage of court reasoning: addresses the main points of the reference court reasoning
4. Logical structure: coherent chain from facts and rules to the given outcome
5. Clarity: clear and understandable presentation

RESPONSE FORMAT: Respond only in JSON format:
{
 "faithfulness_to_facts": {"score": [1-5], "explanation": "Brief explanation"},
 "legal_grounding": {"score": [1-5], "explanation": "Brief explanation"},
 "coverage_of_court_reasoning": {"score": [1-5], "explanation": "Brief explanation"},
 "logical_structure": {"score": [1-5], "explanation": "Brief explanation"},
 "clarity": {"score": [1-5], "explanation": "Brief explanation"},
 "overall_comment": "Overall assessment"
}"""


def build_xai_prompt(facts: str, outcome: str, reference: str, explanation: str,
                     max_facts: int = 6000, max_ref: int = 6000) -> str:
    return (XAI_JUDGE_PROMPT.replace("{facts}", facts[:max_facts]).replace("{outcome}", outcome)
            .replace("{reference}", reference[:max_ref]).replace("{explanation}", explanation))


def parse_xai_scores(text: str) -> Optional[Dict[str, float]]:
    data = extract_json(text)
    if not isinstance(data, dict):
        return None
    out: Dict[str, float] = {}
    for c in XAI_CRITERIA:
        v = data.get(c)
        s = v.get("score") if isinstance(v, dict) else v
        try:
            s = float(s)
        except (TypeError, ValueError):
            return None
        if not 1 <= s <= 5:
            return None
        out[c] = s
    out["overall"] = sum(out[c] for c in XAI_CRITERIA) / len(XAI_CRITERIA)
    return out


class XAIJudge:
    def __init__(self, llm, retries: int = 2):
        self.llm, self.retries = llm, retries

    def score(self, facts: str, outcome: str, reference: str, explanation: str) -> Optional[Dict[str, float]]:
        p = build_xai_prompt(facts, outcome, reference, explanation)
        for i in range(self.retries + 1):
            s = parse_xai_scores(self.llm.generate(p, temperature=0.0 if i == 0 else 0.3, max_new_tokens=700))
            if s:
                return s
        return None


class EmbeddingScorer:
    """OPTIONAL semantic coverage: mean over reference sentences of the best cosine similarity with the explanation's
    sentences. Needs sentence-transformers (e.g. AITeamVN/Vietnamese_Embedding)."""

    def __init__(self, model_name: str):
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(model_name)

    def coverage(self, reference_sents, candidate_sents) -> Optional[float]:
        if not reference_sents or not candidate_sents:
            return None
        import numpy as np

        r = self.model.encode(list(reference_sents), normalize_embeddings=True)
        c = self.model.encode(list(candidate_sents), normalize_embeddings=True)
        return float((r @ c.T).max(axis=1).mean())
