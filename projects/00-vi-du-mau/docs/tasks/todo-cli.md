# Task breakdown: CLI todo (todo-cli)

Nguồn: requirements/todo-cli.md, adr/001-todo-cli.md

## Task 1: Khởi tạo cấu trúc project
- **Mục tiêu:** Tạo package `todo_cli/` (rỗng, có `__init__.py`), thư mục `tests/`, file `requirements-dev.txt` (chỉ `pytest`).
- **File liên quan:** `todo_cli/__init__.py`, `requirements-dev.txt`
- **Definition of Done:**
  - [ ] `pip install -r requirements-dev.txt` chạy được
  - [ ] `pytest` chạy không lỗi (dù chưa có test nào)
- **Rủi ro:** Thấp

## Task 2: Storage layer
- **Mục tiêu:** `todo_cli/storage.py` với `load(path) -> list[dict]` (trả `[]` nếu file chưa tồn tại) và `save(path, items) -> None`.
- **File liên quan:** `todo_cli/storage.py`, `tests/test_storage.py`
- **Definition of Done:**
  - [ ] Test: file chưa tồn tại → `load` trả `[]`
  - [ ] Test: `save` rồi `load` lại → dữ liệu khớp
  - [ ] Test pass thật (dùng `tmp_path` của pytest)
- **Rủi ro:** Thấp

## Task 3: Business logic
- **Mục tiêu:** `todo_cli/todo.py` với `add_item(items, text)`, `mark_done(items, id)`, `delete_item(items, id)` — đều nhận/trả `list[dict]`, không đụng I/O. Id tự tăng, không tái sử dụng id đã xóa. Raise `ValueError` khi id không tồn tại.
- **File liên quan:** `todo_cli/todo.py`, `tests/test_todo.py`
- **Definition of Done:**
  - [ ] Test `add_item` gán đúng id tăng dần
  - [ ] Test `mark_done` đổi đúng trạng thái, không đổi item khác
  - [ ] Test `delete_item` loại đúng item, không tái dùng id cũ cho item mới
  - [ ] Test `mark_done`/`delete_item` với id không tồn tại → raise `ValueError`
- **Rủi ro:** Trung bình — dễ sai logic id sau khi xóa

## Task 4: CLI wiring
- **Mục tiêu:** `todo_cli/cli.py` (argparse: `add`, `list`, `done`, `delete`) + `todo_cli/__main__.py` làm entrypoint `python -m todo_cli`. Gọi `storage` để load/save, gọi `todo.py` để xử lý, in kết quả ra terminal.
- **File liên quan:** `todo_cli/cli.py`, `todo_cli/__main__.py`, `tests/test_cli.py`
- **Definition of Done:**
  - [ ] Test tích hợp: gọi `main(argv)` cho luồng add → list → done → delete, assert output/state đúng
  - [ ] Chạy thử thật qua skill `run`, xác nhận đủ 6 acceptance criteria trong `requirements/todo-cli.md`
  - [ ] Không hardcode đường dẫn file dữ liệu ra ngoài `projects/00-vi-du-mau/`
- **Rủi ro:** Thấp

## Thứ tự thực hiện đề xuất
1. Task 1 — Khởi tạo cấu trúc project
2. Task 2 — Storage layer
3. Task 3 — Business logic
4. Task 4 — CLI wiring

## Trạng thái
- [x] Đã duyệt để bắt đầu coding
