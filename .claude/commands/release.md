Phát hành version: $ARGUMENTS

Đây là giai đoạn 8 (docs/quy-trinh-phat-trien-phan-mem.md). $ARGUMENTS là số version mới (semver, vd 0.2.0).

Việc cần làm:
1. Liệt kê commit từ tag gần nhất đến hiện tại (`git log <tag>..HEAD --oneline`).
2. Xác nhận test của project con đang pass — chạy thật, không giả định.
3. Chuyển nội dung mục "Unreleased" trong `CHANGELOG.md` của project con sang mục version mới (định dạng Keep a Changelog: Added/Changed/Fixed/Removed), dựa theo `templates/changelog-template.md` nếu project chưa có CHANGELOG.
4. Bump version theo semver ở đúng file khai báo version của project (package.json, pyproject.toml, v.v. — xác định đúng file, không đoán bừa).
5. Viết release notes cho version này dựa theo `templates/release-notes-template.md`.

Ràng buộc:
- Semver: MAJOR khi breaking change, MINOR khi thêm tính năng tương thích ngược, PATCH khi chỉ sửa lỗi. Nếu $ARGUMENTS không khớp loại thay đổi thực tế, cảnh báo người dùng trước khi tiếp tục.
- KHÔNG tự tạo git tag hoặc push. Chỉ chuẩn bị thay đổi, hiện toàn bộ ra để người dùng xác nhận.

Kết thúc: hiện CHANGELOG/version/release notes đã soạn, hỏi rõ ràng người dùng có xác nhận để tạo tag `v$ARGUMENTS` không.
