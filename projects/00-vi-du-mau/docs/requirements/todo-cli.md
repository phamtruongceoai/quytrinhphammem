# User Story: CLI quản lý việc cần làm (todo-cli)

## Mục tiêu
Cung cấp một công cụ dòng lệnh (CLI) đơn giản để quản lý danh sách việc cần làm, dùng làm project mẫu (00-vi-du-mau) để chạy thử toàn bộ quy trình phát triển phần mềm từ đầu đến cuối.

## Phạm vi
**Trong phạm vi:**
- Thêm một việc cần làm mới (add).
- Xem danh sách việc cần làm (list).
- Đánh dấu một việc đã hoàn thành (done).
- Xóa một việc khỏi danh sách (delete).
- Lưu dữ liệu vào một file JSON cục bộ trong thư mục project.

**Ngoài phạm vi (không làm ở lần này):**
- Không có giao diện đồ họa hay web.
- Không có nhiều danh sách/dự án con, không có deadline, không có mức ưu tiên.
- Không đồng bộ nhiều máy, không cần đăng nhập/người dùng.
- Không dùng database (SQLite, v.v.) — chỉ file JSON.

## Người dùng mục tiêu
Một người dùng cá nhân, thao tác qua terminal, không cần cài đặt phức tạp (chỉ cần Python).

## Tiêu chí chấp nhận (Acceptance Criteria)
- Given danh sách rỗng, When chạy lệnh `add "Mua sữa"`, Then việc "Mua sữa" xuất hiện trong danh sách với trạng thái chưa hoàn thành.
- Given danh sách có việc, When chạy lệnh `list`, Then in ra tất cả việc kèm trạng thái (xong/chưa xong) và số thứ tự (id).
- Given một việc có id hợp lệ, When chạy lệnh `done <id>`, Then việc đó được đánh dấu hoàn thành và giữ nguyên trong danh sách.
- Given một việc có id hợp lệ, When chạy lệnh `delete <id>`, Then việc đó bị xóa khỏi danh sách và không còn xuất hiện khi `list`.
- Given id không tồn tại, When chạy `done <id>` hoặc `delete <id>`, Then chương trình báo lỗi rõ ràng, không crash.
- Given chương trình được chạy lại (đóng rồi mở terminal mới), When chạy `list`, Then dữ liệu vẫn còn đúng như lần trước (đã lưu vào file JSON).

## Ràng buộc / lưu ý
- Chỉ dùng Python thư viện chuẩn (argparse, json) — không cần cài thêm package ngoài để giữ demo đơn giản.
- File dữ liệu JSON nằm trong `projects/00-vi-du-mau/` (không ghi ra ngoài phạm vi project).

## Trạng thái
- [x] Đã duyệt để sang giai đoạn thiết kế
