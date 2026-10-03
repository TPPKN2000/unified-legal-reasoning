# PLAN — Unified Legal Reasoning Framework (Nguyen et al., 2025)

Paper: *LLMs for legal reasoning: A unified framework and future perspectives*, Computer Law & Security Review 58 (2025) 106165.

## 1. Mục tiêu
Repo tái hiện **đúng cấu trúc & flow** của framework trong paper, chạy được trên Colab T4 free (16 GB VRAM, ~12 GB RAM).

## 2. Ánh xạ Paper → Code (nguồn sự thật cho cấu trúc)
| Paper | Nội dung | Module |
|---|---|---|
| §4.1, Fig.2 | 4 thành phần Fact / Theory / Hypothesis / Outcome | `ulr/components.py` |
| §4.1 (1)(2)(3) | 3 mode: rule-based (F,T[,H]→O), abductive (F,T,O→H), case-based (F_prec,F_pres,O→T,H) | `ulr/modes.py`, `ulr/reasoners.py` |
| App. A/B prompts | Prompt template nguyên văn | `ulr/prompts.py` |
| §2, Fig.3 | Ví dụ Young v. Hitchens, Keeble, Pierson | `ulr/examples.py` |
| §4.2 (1) Pre-trained LLM | HF local / API backends | `ulr/llm/*` |
| §4.2 (2) RAG | BM25 retrieval statutes + precedents | `ulr/retrieval.py`, `data/corpus/` |
| §4.2 (3) Fine-tune, `S=Encode(F,T,H,O)`, `Logit=Agg(O(S))` | Scorer LoRA + head | `ulr/encoding.py`, `ulr/scoring.py` |
| §4.3 + App. A (A.1→A.2→judge→A.3) | Mô phỏng Civil Law | `ulr/court.py::CivilLawSimulator` |
| §4.3 + App. B (B.1→B.2→judge→B.3) | Mô phỏng Common Law | `ulr/court.py::CommonLawSimulator` |
| §4.4 | LLM-as-a-Judge, 8 task (3 rule / 3 abductive / 2 case), 5 tiêu chí 1–5 | `ulr/evaluation/*` |
| Fig.4, Fig.5 | Bar ranking + heatmap | `ulr/evaluation/report.py` |
| §6 | Open issues (policy/principled/cultural, hallucination) | `README.md` (không phải code) |

## 3. Ràng buộc Colab T4
- Model sinh mặc định: `Qwen/Qwen2.5-3B-Instruct` fp16 (~7 GB). Judge: Qwen2.5-7B 4-bit (~5.5 GB) hoặc API.
- Scorer: Qwen2.5-0.5B + LoRA, fp32 (T4 không có bf16 tốt).
- Mọi bước eval **resume được** (JSON checkpoint) → an toàn khi bị ngắt/quota.
- `mock` backend để kiểm thử flow không cần GPU.
- Import torch/transformers là lazy.

## 4. Stages (tick khi xong — xem PROGRESS.md)
- [S0] Phân tích paper, lập plan
- [S1] Skeleton + components + modes + prompts + examples
- [S2] LLM backends (HF/OpenAI/Anthropic/Gemini/mock)
- [S3] Parsing + reasoners (3 mode) + retrieval (RAG)
- [S4] Court simulators (civil/common) + judge strategies
- [S5] Logit scorer (§4.2) + synthetic data + train script
- [S6] Evaluation (tasks, LLM-judge, report Fig.4/5)
- [S7] Scripts + configs + Colab notebook
- [S8] Tests (mock) + chạy thử
- [S9] README + zip

## 5. Quy ước checkpoint
Sau mỗi stage cập nhật `PROGRESS.md`. Nếu hết quota: mở `PROGRESS.md`, làm tiếp từ stage đầu tiên chưa tick.
