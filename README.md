# Unified Legal Reasoning Framework (rule-based + abductive + case-based) with LLMs

Reference implementation of **Nguyen et al., "LLMs for legal reasoning: A unified framework and future perspectives"**,
*Computer Law & Security Review* 58 (2025) 106165. Runs on a **Google Colab T4 (free tier)**.

> Tiếng Việt: mở `notebooks/colab_demo.ipynb` trên Colab (runtime T4), upload `unified-legal-reasoning.zip`, chạy lần lượt các cell.
> Kế hoạch: `PLAN.md`; tiến độ/resume: `PROGRESS.md`.

## The framework (paper §4)
Four components — **Fact**, **Theory**, **Hypothesis**, **Outcome** — and three modes defined by which components are inputs:

| Mode | Input → Output | Class |
|---|---|---|
| Rule-based | Fact + Theory (+ accepted Hypothesis) → plausibility of Outcome | `RuleBasedReasoner` |
| Abductive | Fact + Theory + Outcome → Hypothesis | `AbductiveReasoner` |
| Case-based | Fact(precedent) + Fact(present) + Outcome → Theory + Hypothesis | `CaseBasedReasoner` |

`ulr/modes.py` enforces this input/output contract at run time.

**Court simulation (§4.3)**
- *Civil law* (`CivilLawSimulator`): A.1 rule-based → A.2 abductive (dissatisfied side) → **judge** → A.3 rule-based + accepted hypothesis → repeat from the opposing side.
- *Common law* (`CommonLawSimulator`): B.1 case-based (each side + its precedent) → B.2 challenge (own case-based hypothesis or new abductive hypothesis against the opponent's theory) → **judge** → B.3 rule-based from each side's perspective.
- Judges (`ulr/judges.py`): `paper` (reproduces the paper: accepts the defendant's hypothesis), `auto`, `reject`, `llm`, `interactive`, `keyword:<k>`.

**LLM integration (§4.2)** — all three approaches are implemented
1. Pre-trained LLM: `ulr/llm/` (local HF, OpenAI, Anthropic, Gemini, mock).
2. RAG: `ulr/retrieval.py` (BM25 over `data/corpus/`: statutes → Theory, cases → Precedents). Use `--rag`.
3. Fine-tuning: `ulr/scoring.py`, `S = Encode(F,T,H,O)`, `Logit = Agg(O(S))` (LoRA + pooling of final-layer activations + linear head). Train with `scripts/train_logit.py`; pass `--scorer <dir>` to attach a logit to every rule-based step.

**Evaluation (§4.4)** — `ulr/evaluation/`: 8 prompts (3 rule-based = A.1/A.3/B.3, 3 abductive = A.2/B.2.1/B.2.2, 2 case-based = B.1), LLM-as-a-Judge with the paper's judge prompt, 5 criteria scored 1–5, overall = mean; produces Fig. 4 (ranking) and Fig. 5 (heatmap) analogues.

## Quick start
```bash
pip install -e .                       # + transformers accelerate bitsandbytes peft on GPU
python scripts/run_civil.py  --backend mock          # offline dry run of the whole flow
python scripts/run_common.py --backend mock --rag
python scripts/run_eval.py   --config configs/mock.yaml
pytest                                               # 20 tests, no GPU needed

# Colab T4 (real models, configs/colab_t4.yaml)
python scripts/run_civil.py  --judge paper --out outputs/civil.json
python scripts/run_common.py --judge paper --out outputs/common.json
python scripts/train_logit.py && python scripts/run_civil.py --scorer outputs/logit_scorer
python scripts/run_eval.py --stage generate && python scripts/run_eval.py --stage judge && python scripts/run_eval.py --stage report
```
`run_eval.py` is **resumable**: responses and scores are checkpointed after every item (point `outputs/` to Google Drive in the notebook).

## Layout
```
src/ulr/{components,modes,prompts,examples,parsing,reasoners,judges,court,retrieval,encoding,scoring,synthetic,runtime}.py
src/ulr/llm/        backends        src/ulr/evaluation/  tasks, judge, runner, report
configs/            mock | colab_t4 | api       data/corpus, data/logit      scripts/      notebooks/colab_demo.ipynb      tests/
```

## Fidelity notes & deliberate deviations (please read)
- Prompts in `prompts.py` are verbatim from Appendix A/B (guarded by `tests/test_prompts.py`).
- The paper used GPT / Claude 3.5 / Gemini 1.5. Those are API models (several retired); for a free T4 the defaults are open models (Qwen2.5 0.5B/1.5B/3B, Phi-3.5-mini; Qwen2.5-7B 4-bit as judge). `configs/api.yaml` is the closest to the paper — edit model names to currently available ones. **Absolute scores are therefore not comparable with the paper's Fig. 4/5**, and a small judge is noisier than GPT-4o; self-judging (a model scoring itself) is biased.
- Free-text → component parsing (verdict, hypotheses, B.1 theory) is heuristic (`parsing.py`); if the verdict cannot be parsed, a one-word LLM classifier call is used as fallback (not part of the paper).
- The paper does not specify the scalar head/aggregation for `Agg`; this repo uses last-token | mean | max pooling of the final hidden states + a linear head, trained with BCE. The shipped synthetic set (`data/logit`, 30 records) is a **smoke-test scale** dataset — build a real one before drawing conclusions. Case-based quadruples use a simple concatenation of present + precedent facts.
- Paper §6 (policy-based, principled, cultural reasoning, hallucination/over-reliance) is discussed there as open issues and is **not** implemented; LLM outputs here are decision *support*, not legal advice.
- Verified in the build sandbox (no GPU / no model downloads): prompts, parsing, both court flows, judges, RAG, evaluation pipeline and report (mock backend), 20 unit tests. **Not verified there**: HF local backends and `scoring.py` (need torch/transformers/peft and model weights) — run the notebook's smoke cells on Colab first.
