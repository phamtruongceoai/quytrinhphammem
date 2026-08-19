# Quy trình làm phần mềm với Claude Code

Bộ khung quy trình phát triển phần mềm (SDLC) đầy đủ, vận hành thực tế bằng Claude Code — dùng cho mục đích học tập cá nhân, không gắn cứng vào một tech stack.

## Trước khi bắt đầu

Kiểm tra máy đã có git identity và (nếu dùng GitHub) đã đăng nhập GitHub CLI, tránh bị chặn giữa chừng ở commit đầu tiên:
```
git config user.name
git config user.email
gh auth status
```
Nếu trống, tự thiết lập (`git config user.name "..."`, `git config user.email "..."`, `gh auth login`) trước khi tạo project đầu tiên.

## Bắt đầu từ đâu

1. Đọc [docs/quy-trinh-phat-trien-phan-mem.md](docs/quy-trinh-phat-trien-phan-mem.md) — nguồn sự thật của toàn bộ quy trình (9 giai đoạn).
2. Tra nhanh công cụ cho từng giai đoạn: [docs/ban-do-cong-cu.md](docs/ban-do-cong-cu.md).
3. Chưa quen thuật ngữ (ADR, DoD, semver...)? Xem [docs/glossary.md](docs/glossary.md).
4. Bắt đầu một dự án mới: tạo thư mục trong `projects/<project-slug>/`, copy [templates/CLAUDE.md.template](templates/CLAUDE.md.template) thành `projects/<project-slug>/CLAUDE.md` và điền thông tin, rồi chạy `/requirements <ý tưởng>`.
5. Muốn biết chính khung quy trình này đã thay đổi/được rà soát thế nào theo thời gian: [docs/process-log.md](docs/process-log.md).

## Cấu trúc

- `docs/` — tài liệu quy trình
- `templates/` — mẫu dùng chung (user story, ADR, task breakdown, PR checklist, changelog...)
- `.claude/commands/` — slash command triển khai từng giai đoạn
- `projects/` — các dự án cụ thể áp dụng quy trình

## Ví dụ mẫu

`projects/00-vi-du-mau/` (todo-cli) là project nhỏ đã chạy thử toàn bộ quy trình từ đầu đến cuối — requirements ([docs/requirements/todo-cli.md](projects/00-vi-du-mau/docs/requirements/todo-cli.md)) → design ([docs/adr/001-todo-cli.md](projects/00-vi-du-mau/docs/adr/001-todo-cli.md)) → task breakdown ([docs/tasks/todo-cli.md](projects/00-vi-du-mau/docs/tasks/todo-cli.md)) → code (10 test pass) → code review (bắt được 1 lỗi thật, đã sửa) → PR → release `todo-cli-v0.1.0`. Bài học rút ra: [docs/retro/2026-08-19.md](projects/00-vi-du-mau/docs/retro/2026-08-19.md).
