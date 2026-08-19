Chuẩn bị PR cho: $ARGUMENTS

Đây là giai đoạn 7 (docs/quy-trinh-phat-trien-phan-mem.md).

Việc cần làm:
1. Xác nhận đã chạy `/code-review` cho thay đổi này (và `/security-review` nếu đụng auth/dữ liệu người dùng/input bên ngoài). Nếu chưa, dừng lại và đề nghị chạy trước — không tự bỏ qua bước review.
2. Xem diff thật (`git diff`/`git status`) để điền checklist chính xác, không đoán.
3. Ghi vào `projects/<slug>/docs/pr/<slug>-<mô-tả-ngắn>.md`, dựa theo `templates/pr-checklist.md`. Một PR không nhất thiết ứng với 1 task — có thể gộp nhiều task, đặt tên theo nội dung PR.
4. Soạn commit message theo Conventional Commits (type(scope): mô tả ngắn).
5. Soạn PR description (Summary / Changes / Test plan) nếu sẽ push lên GitHub thật.

Ràng buộc:
- KHÔNG tự ý `git push` hoặc tạo PR thật. Chỉ soạn nội dung và hiện ra để người dùng xác nhận, việc push/tạo PR do người dùng quyết định thực hiện.
- Nếu có finding chưa xử lý từ `/code-review`/`/security-review`, liệt kê rõ và hỏi người dùng có chấp nhận bỏ qua không, đừng tự ý ẩn đi.

Kết thúc: hiện checklist + commit message + PR description, chờ xác nhận của người dùng.
