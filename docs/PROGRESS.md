# PROGRESS (cập nhật sau mỗi stage)

- [x] S0 Phân tích paper, lập plan (PLAN.md)
- [x] S1 Skeleton + components + modes + prompts + examples
- [x] S2 LLM backends
- [x] S3 Parsing + reasoners + retrieval
- [x] S4 Court simulators + judges
- [x] S5 Logit scorer + synthetic data
- [x] S6 Evaluation pipeline
- [x] S7 (notebook: xem dòng dưới) Scripts + configs + notebook
- [x] S8 Tests + smoke run (mock)
- [x] S9 README + zip

## Ghi chú
- S5: scoring.py (torch) chỉ kiểm tra cú pháp trong sandbox (không có GPU/HF); cần chạy smoke test trên Colab (notebook cell 'Train scorer').
- S8: 20 pytest pass (mock). Chưa kiểm chứng trong sandbox: HF backend + scoring.py (cần GPU/weights).
- Việc tiếp theo (nếu tiếp tục): chạy notebook trên Colab T4, sửa lỗi môi trường nếu có; mở rộng data/logit; thêm model/judge API.
