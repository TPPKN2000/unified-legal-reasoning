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
- [x] S10 ALQAC-XAI: dữ liệu dạng ALQAC + thử nghiệm giải thích (xem docs/ALQAC_XAI.md; X0–X6 đã xong)

## Ghi chú
- S5: scoring.py (torch) chỉ kiểm tra cú pháp trong sandbox (không có GPU/HF); cần chạy smoke test trên Colab (notebook cell 'Train scorer').
- S8: 20 pytest pass (mock). Chưa kiểm chứng trong sandbox: HF backend + scoring.py (cần GPU/weights).
- Sau lần chạy Colab đầu: sửa `parse_verdict` (bỏ câu nhắc lại câu hỏi, lấy câu kết luận cuối) — lỗi làm A.1 bị đọc nhầm "guilty".
- S10: 34 pytest pass (mock). Chưa chạy ALQAC-XAI với model thật trên Colab. Corpus mẫu chỉ có 2 điều của Luật 47/2010/QH12,
  không resolve được điều luật nào trong 48 provisions của 4 vụ mẫu ⇒ `oracle` chỉ có nhãn trích dẫn, `rag` truy xuất ra luật không liên quan.
- Việc tiếp theo: chạy notebook mục 6 trên Colab; nạp corpus đầy đủ (cần số điều); so sánh oracle vs rag vs decontaminate; bật LLM-judge/embedding.
