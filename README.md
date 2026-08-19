# Quy trình làm phần mềm với Claude Code

Bộ khung quy trình phát triển phần mềm (SDLC) đầy đủ, vận hành thực tế bằng Claude Code — dùng cho mục đích học tập cá nhân, không gắn cứng vào một tech stack.

## Bắt đầu từ đâu

1. Đọc [docs/quy-trinh-phat-trien-phan-mem.md](docs/quy-trinh-phat-trien-phan-mem.md) — nguồn sự thật của toàn bộ quy trình (9 giai đoạn).
2. Tra nhanh công cụ cho từng giai đoạn: [docs/ban-do-cong-cu.md](docs/ban-do-cong-cu.md).
3. Chưa quen thuật ngữ (ADR, DoD, semver...)? Xem [docs/glossary.md](docs/glossary.md).
4. Bắt đầu một dự án mới: tạo thư mục trong `projects/<slug>/`, copy [templates/CLAUDE.md.template](templates/CLAUDE.md.template) thành `projects/<slug>/CLAUDE.md` và điền thông tin, rồi chạy `/requirements <ý tưởng>`.

## Cấu trúc

- `docs/` — tài liệu quy trình
- `templates/` — mẫu dùng chung (user story, ADR, task breakdown, PR checklist, changelog...)
- `.claude/commands/` — slash command triển khai từng giai đoạn
- `projects/` — các dự án cụ thể áp dụng quy trình

## Ví dụ mẫu

`projects/00-vi-du-mau/` là project nhỏ dùng để chạy thử toàn bộ quy trình từ đầu đến cuối, xem [docs/quy-trinh-phat-trien-phan-mem.md](docs/quy-trinh-phat-trien-phan-mem.md) mục Verification trong plan gốc.
