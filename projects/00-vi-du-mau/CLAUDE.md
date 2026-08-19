# CLAUDE.md — todo-cli (00-vi-du-mau)

Đây là project con thuộc bộ khung quy trình phát triển phần mềm. Quy trình đầy đủ tham khảo tại `../../docs/quy-trinh-phat-trien-phan-mem.md` (nguồn sự thật). Project này dùng để chạy thử toàn bộ quy trình từ đầu đến cuối (xem `docs/requirements/todo-cli.md`, `docs/adr/001-todo-cli.md`, `docs/tasks/todo-cli.md`).

## Stack
Python 3 (chỉ thư viện chuẩn: `argparse`, `json`) + `pytest` cho test. Không dùng framework/database ngoài.

## Version
- File khai báo version: `todo_cli/__init__.py` (`__version__`) — project không dùng packaging (pyproject.toml/setup.py).
- Tag release dùng format `todo-cli-v<version>` (vd `todo-cli-v0.1.0`).

## Lệnh thường dùng
- Cài đặt: `pip install -r requirements-dev.txt`
- Chạy app: `python -m todo_cli <add|list|done|delete> ...`
- Chạy test: `pytest`
- Lint: (chưa thiết lập — project demo nhỏ, bỏ qua)

## Cấu trúc thư mục
```
00-vi-du-mau/
├── docs/
│   ├── requirements/   # output của /requirements
│   ├── adr/             # output của /design
│   ├── tasks/            # output của /plan-task
│   ├── pr/                # output của /pr
│   └── retro/            # output của /retro
├── todo_cli/
│   ├── __init__.py
│   ├── storage.py         # I/O JSON thuần (load/save)
│   ├── todo.py             # logic nghiệp vụ thuần (add/done/delete)
│   ├── cli.py               # argparse, nối storage + todo
│   └── __main__.py          # entrypoint `python -m todo_cli`
├── tests/
├── requirements-dev.txt
└── CHANGELOG.md
```

## Quy ước code
- Tách I/O (storage.py) khỏi logic nghiệp vụ (todo.py) để test không cần mock file — xem ADR 001.
- Không hardcode secret/API key — project này không có secret nào.
- Id của item tự tăng, không tái sử dụng id đã xóa.

## Quy trình làm việc (theo thứ tự)
1. `/requirements` — nếu tính năng mới chưa có user story
2. `/design` — nếu cần quyết định kiến trúc
3. `/plan-task` — chia nhỏ thành task, chờ duyệt
4. `/new-feature` — code + test theo từng task
5. `/code-review` (và `/security-review` nếu cần) — bắt buộc trước khi PR
6. `/pr` — soạn commit + PR, không tự push
7. `/release <slug> <version>` — khi gộp đủ tính năng cho một bản phát hành

## Ghi chú riêng của project này
Đây là project mẫu (00-vi-du-mau) dùng để verify khung quy trình — không phải sản phẩm thật cần duy trì lâu dài.
