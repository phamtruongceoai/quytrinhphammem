# ADR 001: Cấu trúc module cho todo-cli

**Trạng thái:** Đề xuất
**Ngày:** 2026-08-19
**Liên quan:** requirements/todo-cli.md

## Bối cảnh
todo-cli cần 4 thao tác (add/list/done/delete), lưu vào file JSON, chỉ dùng thư viện chuẩn Python. Theo Definition of Done của quy trình, mỗi task cần có test — nên cấu trúc code phải cho phép test logic nghiệp vụ (thêm/xóa/đánh dấu xong) mà không cần chạy toàn bộ CLI qua subprocess.

## Các phương án đã cân nhắc

### Phương án A: Một file duy nhất `todo.py`
Toàn bộ argparse, đọc/ghi JSON, và logic add/list/done/delete gộp trong một file.
- Ưu điểm: nhanh viết nhất, dễ đọc cho demo nhỏ, không cần quyết định cấu trúc thư mục.
- Nhược điểm: logic nghiệp vụ trộn lẫn với I/O và argparse — muốn test hàm `add`/`done`/`delete` phải mock stdin/stdout hoặc chạy subprocess, chậm và khó viết assertion chính xác.

### Phương án B: Package nhỏ 3 module (`storage.py`, `todo.py`, `cli.py`)
- `storage.py`: đọc/ghi file JSON, trả về/nhận list dict thuần.
- `todo.py`: hàm nghiệp vụ thuần (`add_item`, `mark_done`, `delete_item`) nhận/trả về list, không đụng I/O.
- `cli.py`: argparse, gọi `storage` để load/save, gọi `todo.py` để xử lý, in kết quả ra terminal.
- Ưu điểm: test logic nghiệp vụ trực tiếp bằng pytest (truyền list Python, assert list trả về) — nhanh, rõ ràng, đúng DoD "có test, test pass". Vẫn chỉ dùng thư viện chuẩn, không tăng độ phức tạp vận hành.
- Nhược điểm: nhiều file hơn một chút so với quy mô rất nhỏ của tính năng.

## Quyết định
Chọn **Phương án B**. Lý do: chi phí thêm (2 file thay vì 1) rất nhỏ, trong khi lợi ích về khả năng test là đáng kể và đúng với yêu cầu DoD của quy trình (mỗi task phải có test thật, không phải giả định). Đây cũng là structure tối thiểu thể hiện được nguyên tắc tách I/O khỏi logic nghiệp vụ — hữu ích để học quy trình dù project rất nhỏ.

## Hệ quả
- Task breakdown ở giai đoạn 3 sẽ chia theo: (1) storage, (2) logic nghiệp vụ + test, (3) CLI wiring.
- Test (`pytest`) sẽ tập trung vào `todo.py` (logic thuần), có thể thêm 1-2 test tích hợp gọi qua `cli.py` nếu cần.
- Không cần cài thư viện ngoài; `pytest` là dev-dependency duy nhất.

## Trạng thái
- [x] Đã duyệt để sang giai đoạn lập kế hoạch
