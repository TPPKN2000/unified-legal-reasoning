# ALQAC-XAI — áp dữ liệu dạng ALQAC vào repo để thử nghiệm *khả năng giải thích*

**Mục tiêu thử nghiệm:** đo chất lượng LẬP LUẬN GIẢI THÍCH của mô hình cho một kết quả đã biết, KHÔNG đo độ chính xác dự đoán.
Kết quả vụ án (`verdict_label`) được đưa vào làm **Outcome đầu vào** của mode abductive (F,T,O → H).

## Dữ liệu (định dạng mẫu)
- `data/alqac/ALQAC_public_test_sample.json`: list các vụ. Trường dùng làm đầu vào: `case_fact`, `case_query` (bỏ câu "Agent dự đoán…"),
  `case_type`, `A_role/B_role`, `related_law_provisions` (chỉ ở chế độ `oracle`), `verdict_label` (chỉ làm Outcome cho trước).
- Trường **cấm dùng làm đầu vào**: `judgment_text`, `court_verdict`, `court_reasoning` (chỉ làm *tham chiếu* để chấm). Có test kiểm tra.
- `data/alqac/corpus_law_pub_sample.json`: `[{id, law_id, content:[{aid, content_Article}]}]`. `aid` là id toàn cục, KHÔNG phải số điều.
- `data/alqac/law_aliases.json`: ánh xạ tên luật trong `related_law_provisions` → `law_id` (người dùng bổ sung).

## Ánh xạ vào framework
| ALQAC | Framework |
|---|---|
| `case_fact` (+ tóm tắt `case_query`) | Fact |
| `related_law_provisions` (oracle) hoặc BM25 trên corpus (rag) | Theory |
| `verdict_label` (A_WIN / PARTIAL_A_WIN / B_WIN) | Outcome (cho trước) |
| Đầu ra abductive (top-k) | Hypothesis = lời giải thích |
| Rule-based (F,T,H) | kiểm tra "giải thích có dẫn tới Outcome không" |

## Chỉ số (không có accuracy dự đoán làm chỉ số chính)
1. Trích dẫn điều luật: P/R/F1 theo số điều so với `related_law_provisions`; tỉ lệ trích dẫn ngoài Theory được cấp.
2. Độ phủ lập luận: ROUGE-L và độ phủ theo câu so với `court_reasoning`; (tùy chọn) cosine embedding.
3. Bám sự kiện: tỉ lệ số liệu trong giải thích không có trong Fact/Theory.
4. Nhất quán giải thích–kết quả (rule-based F,T,H có ra đúng Outcome) + baseline không H → "lift".
5. (tùy chọn, cờ) LLM-judge với rubric giải thích.
6. Rò rỉ: tỉ lệ câu `court_reasoning` đã có sẵn trong `case_fact` (`scripts/inspect_alqac.py`).

## Stages
- [X0] Lập plan này, copy dữ liệu mẫu
- [X1] schema + loader + parse_provisions + LawIndex + sửa tokenizer Việt (retrieval/parsing)
- [X2] adapter (Fact/Issue/Outcome/Theory) + decontaminate
- [X3] metrics thuần Python + XAI judge
- [X4] pipeline xai.py (resumable) + report
- [X5] scripts + config + mock Việt + tests
- [X6] chạy thử mock, đo rò rỉ trên mẫu, đóng gói bản vá
