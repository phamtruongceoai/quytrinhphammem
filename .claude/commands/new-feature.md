Code task: $ARGUMENTS

Đây là giai đoạn 4-5 (docs/quy-trinh-phat-trien-phan-mem.md). Input là một task cụ thể đã duyệt trong `projects/<slug>/docs/tasks/<slug>.md`.

Việc cần làm:
1. Đọc CLAUDE.md của project con (`projects/<slug>/CLAUDE.md`) để biết stack, lệnh test/lint, quy ước code. Nếu project con chưa có CLAUDE.md, dừng lại và đề nghị chạy skill `/init` trong thư mục project con trước, rồi đối chiếu với `templates/CLAUDE.md.template`.
2. Đọc đúng task cần làm trong file task breakdown — chỉ làm đúng phạm vi task đó, không lan sang task khác.
3. Code bám theo pattern đã có trong project, không thêm thư viện/abstraction không cần thiết.
4. Viết test theo Definition of Done của task. Chạy test thật, dán kết quả — không giả định là pass.
5. Không hardcode secret/API key.
6. Cập nhật trạng thái task (đánh dấu hoàn thành) trong file task breakdown.

Kiểm chứng (bắt buộc):
- Chạy test/lint theo lệnh khai báo trong CLAUDE.md của project con, dán output thật.
- Nếu tính năng có thể chạy thử được (app/CLI), dùng skill `run` để xác nhận hoạt động thật, không chỉ dựa vào test.

Kết thúc: tóm tắt file đã đổi, nhắc bước tiếp theo là `/code-review` (và `/security-review` nếu task đụng auth/dữ liệu người dùng).
