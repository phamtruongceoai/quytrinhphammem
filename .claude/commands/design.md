Thiết kế kiến trúc cho: $ARGUMENTS

Đây là giai đoạn 2 (docs/quy-trinh-phat-trien-phan-mem.md). Input là file requirements đã có ở `projects/<slug>/docs/requirements/`. Nếu chưa có, dừng lại và đề nghị chạy `/requirements` trước.

Việc cần làm:
1. Đọc kỹ requirements liên quan.
2. Đề xuất tối thiểu 2 phương án kiến trúc/kỹ thuật khả thi, nêu rõ ưu/nhược điểm và trade-off của từng phương án (hiệu năng, độ phức tạp, khả năng mở rộng, thời gian làm).
3. Đưa ra khuyến nghị chọn phương án nào và vì sao, nhưng để người dùng quyết định cuối cùng.
4. Ghi ADR vào `projects/<slug>/docs/adr/NNN-<slug>.md` (NNN tăng dần), dựa theo `templates/adr-template.md`.

Ràng buộc:
- Đây là giai đoạn BÀN kiến trúc, không sửa code thật. Nếu có sẵn, ưu tiên dùng Plan Mode trong lúc thảo luận.
- Không chọn công nghệ/thư viện mới ngoài stack đã khai báo trong CLAUDE.md của project con nếu không thật cần thiết — nếu cần, giải thích rõ lý do trong ADR.

Kết thúc: tóm tắt quyết định, hỏi người dùng có đồng ý để chuyển sang `/plan-task` không.
