Làm rõ yêu cầu cho: $ARGUMENTS

Đây là giai đoạn 1 của quy trình (docs/quy-trinh-phat-trien-phan-mem.md). Mục tiêu là biến một ý tưởng thô thành user story rõ ràng — KHÔNG code ở bước này.

Việc cần làm:
1. Xác định slug (tên ngắn, kebab-case) cho tính năng/project này. Nếu chưa rõ project nào trong `projects/`, hỏi người dùng trước khi tạo mới.
2. Hỏi lại các điểm còn mơ hồ: mục tiêu thật sự, phạm vi (trong/ngoài), người dùng mục tiêu, ràng buộc kỹ thuật hoặc thời gian. Đừng tự đoán nếu có thể hỏi.
3. Viết acceptance criteria dạng Given/When/Then — đủ cụ thể để sau này biết khi nào tính năng "xong".
4. Ghi vào `projects/<slug>/docs/requirements/<slug>.md`, dựa theo `templates/user-story.md`.

Ràng buộc:
- Không tự chuyển sang thiết kế kiến trúc hay viết code.
- Nếu ý tưởng quá rộng, đề nghị chia nhỏ thành nhiều user story thay vì nhồi hết vào một file.

Kết thúc: tóm tắt nội dung đã ghi, hỏi người dùng có đồng ý để chuyển sang `/design` không.
