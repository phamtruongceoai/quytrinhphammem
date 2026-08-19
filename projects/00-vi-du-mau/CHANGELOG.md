# Changelog

Định dạng dựa theo [Keep a Changelog](https://keepachangelog.com/), version theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-08-19
### Added
- CLI todo (`todo_cli`): thêm/xem/đánh dấu xong/xóa việc cần làm, lưu vào file JSON local.
- Tách logic nghiệp vụ (`todo.py`) khỏi I/O (`storage.py`) để dễ test (ADR 001).
- 10 test tự động (unit cho storage/todo, tích hợp cho CLI), bao gồm xử lý lỗi id không tồn tại và file dữ liệu JSON hỏng mà không crash.
