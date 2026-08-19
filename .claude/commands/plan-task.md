Lập kế hoạch task cho: $ARGUMENTS

Đây là giai đoạn 3 (docs/quy-trinh-phat-trien-phan-mem.md). Input là requirements + ADR đã duyệt. Nếu thiếu một trong hai, dừng lại và đề nghị chạy `/requirements` hoặc `/design` trước — không tự suy diễn.

Việc cần làm:
1. Đọc requirements và ADR liên quan trong `projects/<slug>/docs/`.
2. Chia thành các task nhỏ, mỗi task làm được trong một phiên code (không quá lớn). Với mỗi task ghi rõ: mục tiêu, file liên quan, Definition of Done, mức rủi ro.
3. Đề xuất thứ tự thực hiện hợp lý (task nền tảng trước, task phụ thuộc sau).
4. Ghi vào `projects/<slug>/docs/tasks/<slug>.md`, dựa theo `templates/task-breakdown.md`.
5. Nếu công cụ theo dõi task (TodoWrite) khả dụng trong phiên làm việc, tạo danh sách tương ứng để theo dõi tiến độ — không bắt buộc nếu môi trường không hỗ trợ.

Ràng buộc:
- KHÔNG code ở bước này.
- Nếu phát hiện requirements/ADR có lỗ hổng khi chia task, báo lại thay vì tự vá bằng giả định.

Kết thúc: hiện toàn bộ danh sách task, dừng lại chờ người dùng duyệt trước khi bắt đầu `/new-feature`.
