# Bản đồ giai đoạn ↔ công cụ

Tra nhanh khi không nhớ nên chạy lệnh gì. Cú pháp tham số đầy đủ (dùng `<project-slug>`/`<feature-slug>` ra sao) xem [quy-trinh-phat-trien-phan-mem.md](quy-trinh-phat-trien-phan-mem.md) — bảng này chỉ liệt kê tên lệnh để tránh lệch khi cú pháp đổi.

| Muốn làm gì | Chạy | Loại |
|---|---|---|
| Biến ý tưởng thành yêu cầu rõ ràng | `/requirements` | Command mới |
| Quyết định kiến trúc/kỹ thuật | `/design` | Command mới |
| Chia tính năng thành task nhỏ | `/plan-task` | Command mới |
| Làm giàu CLAUDE.md dựa trên code đã có (sau khi có code, không phải lúc bắt đầu) | `/init` | Skill có sẵn |
| Code một task cụ thể | `/new-feature` | Command mới |
| Chạy thử app để xác nhận hoạt động thật | skill `run` | Skill có sẵn |
| Review chất lượng code (bug, đơn giản hoá) | `/code-review` | Skill có sẵn |
| Review bảo mật (auth, dữ liệu người dùng) | `/security-review` | Skill có sẵn |
| Dọn code trước khi PR | `/simplify` | Skill có sẵn |
| Soạn commit + PR | `/pr` | Command mới |
| Phát hành version mới | `/release` | Command mới |
| Rút kinh nghiệm sau vòng làm việc | `/retro` | Command mới |
| Bàn kiến trúc mà chưa muốn sửa code | Plan Mode | Tính năng có sẵn |
| Sửa bug nhanh (bugfix nhỏ ngoài quy trình đầy đủ) | skill cá nhân `sua-loi` | Skill cá nhân |
