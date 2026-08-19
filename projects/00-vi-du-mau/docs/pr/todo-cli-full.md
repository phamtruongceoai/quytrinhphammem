# PR: todo-cli — CLI todo mẫu (add/list/done/delete)

## Tóm tắt thay đổi
Hoàn thành project mẫu `00-vi-du-mau`: CLI quản lý việc cần làm bằng Python (add/list/done/delete, lưu file JSON), dùng để verify toàn bộ quy trình phát triển phần mềm của repo này từ đầu đến cuối (requirements → design → task → code → review → PR).

## File đã đổi
- `.gitignore` (mới, ở root — loại `__pycache__/`, `.pytest_cache/`, `todos.json`)
- `projects/00-vi-du-mau/CLAUDE.md` (mới)
- `projects/00-vi-du-mau/docs/requirements/todo-cli.md` (mới)
- `projects/00-vi-du-mau/docs/adr/001-todo-cli.md` (mới)
- `projects/00-vi-du-mau/docs/tasks/todo-cli.md` (mới)
- `projects/00-vi-du-mau/requirements-dev.txt` (mới)
- `projects/00-vi-du-mau/todo_cli/__init__.py`, `storage.py`, `todo.py`, `cli.py`, `__main__.py` (mới)
- `projects/00-vi-du-mau/tests/test_storage.py`, `test_todo.py`, `test_cli.py` (mới)

## Checklist
- [x] Đã chạy `/code-review` (effort medium) — 1 finding thật (storage.load không bắt JSONDecodeError, dữ liệu JSON hỏng làm crash CLI) đã được sửa (đưa `storage.load` vào trong khối `try/except ValueError` ở `cli.py`, vì `json.JSONDecodeError` là subclass của `ValueError`) và thêm test hồi quy `test_corrupted_data_file_reports_error_without_crash`
- [ ] `/security-review` — bỏ qua có chủ đích: không có auth, không có dữ liệu người dùng nhạy cảm, không gọi API bên ngoài, chỉ đọc/ghi 1 file JSON local trong phạm vi project
- [x] Test pass thật: `pytest -q` → `10 passed`
- [x] Không hardcode secret/API key (không có secret nào trong scope)
- [x] Đã cập nhật tài liệu liên quan: CLAUDE.md, requirements, ADR, task breakdown đều đã ghi trong quá trình làm

## Commit message (Conventional Commits)
```
feat(00-vi-du-mau): them CLI todo mau de verify quy trinh

Trien khai project mau todo-cli (add/list/done/delete, luu JSON)
theo dung 4 giai doan requirements/design/plan-task/new-feature cua
quy trinh. Da chay /code-review va sua 1 loi thuc te (JSON hong lam
crash CLI). 10/10 test pass.
```

## PR description
**Summary:** Thêm project mẫu `00-vi-du-mau` — một CLI todo nhỏ (Python, chỉ thư viện chuẩn) — để chạy thử và xác nhận toàn bộ khung quy trình phát triển phần mềm (`docs/quy-trinh-phat-trien-phan-mem.md`) hoạt động đúng thực tế từ requirements đến PR.

**Changes:**
- `docs/requirements/todo-cli.md`, `docs/adr/001-todo-cli.md`, `docs/tasks/todo-cli.md` — kết quả 3 giai đoạn đầu của quy trình.
- `todo_cli/` — code CLI, tách storage (I/O JSON) khỏi logic nghiệp vụ theo ADR 001.
- `tests/` — 10 test (unit cho storage/todo, tích hợp cho CLI), bao gồm 1 test hồi quy cho lỗi tìm thấy qua `/code-review`.
- `.gitignore` ở root — tránh commit cache/dữ liệu runtime.

**Test plan:**
- `pip install -r projects/00-vi-du-mau/requirements-dev.txt && pytest` trong `projects/00-vi-du-mau/` → 10 passed.
- Chạy tay `python -m todo_cli add/list/done/delete` → xác nhận đủ 6 acceptance criteria trong requirements, kể cả trường hợp id không tồn tại và file dữ liệu hỏng đều báo lỗi rõ ràng, không crash.
