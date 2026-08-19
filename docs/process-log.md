# Process log — lịch sử thay đổi của khung quy trình

Khác `CHANGELOG.md` của từng project con (theo version phần mềm), file này ghi lại lịch sử **quyết định về chính bộ khung quy trình**: mỗi lần rà soát/sửa tài liệu, command, template — phát hiện gì, quyết định gì, vì sao. Mục đích: không để các phát hiện chỉ tồn tại trong plan file cục bộ rồi mất đi khi phiên làm việc kết thúc (bài học từ vòng 5 dưới đây).

## Vòng 1 — Khởi tạo (2026-08-19)
Xây khung quy trình 9 giai đoạn, template, 7 slash command. Verify toàn bộ pipeline qua project mẫu `todo-cli` (`projects/00-vi-du-mau/`) từ `/requirements` đến `/release` + `/retro`. `/code-review` phát hiện và sửa 1 lỗi thật (JSON hỏng làm crash CLI). Retro sau vòng này đề xuất 3 cải tiến (tag gắn slug, ghi chú version khi không packaging, hướng dẫn gộp/tách review theo rủi ro) — đã áp dụng, commit `d8ab9af`.

## Vòng 2 — Rà soát lệch tài liệu
Phát hiện 6 điểm: cú pháp `/release <version>` cũ còn sót sau khi đã đổi; README trỏ tới "plan gốc" — thực chất là file plan cục bộ của Claude Code, không nằm trong repo, không ai đọc lại được; `/new-feature` chặn cứng đòi chạy `/init` trước dù project chưa có code để phân tích; tên file PR ép theo 1 task, không khớp PR gộp nhiều task; thiếu checklist môi trường (git identity, `gh auth`) trước khi bắt đầu; TodoWrite được nhắc như bắt buộc dù không phải môi trường nào cũng có. Đã sửa cả 6, commit `7d60bbf`.

## Vòng 3 — Vấn đề cấu trúc/logic
Phát hiện 6 điểm sâu hơn (không chỉ câu chữ):
- `<slug>` bị dùng chồng lấn vai trò thư mục project và tên file tính năng — vỡ khi 1 project có tính năng thứ hai. Sửa: tách `<project-slug>`/`<feature-slug>`.
- Đường dẫn output của release notes chưa từng được định nghĩa — đã gây lưu sai chỗ thật (`docs/pr/release-notes-0.1.0.md` thay vì đáng lẽ có `docs/release/`). Sửa: thêm `docs/release/<version>.md`.
- Quy trình viết tuyến tính 1→9, không có hướng dẫn khi nào nên quay lại giai đoạn trước. Sửa: thêm mục "Vòng lặp, không phải đường thẳng".
- Đánh dấu rủi ro Cao ở task breakdown không nối với hành động thực tế lúc code. Sửa: thêm nhắc vào `/new-feature`.
- Cùng một trình tự lệnh bị lặp lại ở 4 nơi, đã tự chứng minh lệch 2 lần. Sửa: rút gọn `ban-do-cong-cu.md` và `CLAUDE.md.template` chỉ còn tên lệnh, trỏ về nguồn sự thật.
- "3 giai đoạn đầu luôn dừng lại chờ duyệt" không có ngoại lệ cho thay đổi rất nhỏ, mâu thuẫn nhẹ với template. Sửa: thêm câu ngoại lệ vào Nguyên tắc chung.

## Vòng 4 — Process QA (đánh giá meta)
Nhận định chính: cả 3 vòng trước đều dựa trên **một** project mẫu duy nhất, quy mô nhỏ, chỉ 1 tính năng — các cơ chế vừa sửa (project-slug/feature-slug, docs/release/) chưa từng được thử nghiệm thật. Rủi ro: tiếp tục tinh chỉnh dựa trên suy đoán thay vì dữ liệu thực tế (over-engineering). Đề xuất dừng sửa tài liệu, chạy project thứ hai (có tính năng thứ hai nối tiếp) trước khi rà soát tiếp. Ngoài ra: thêm bước tự-kiểm-tra (Grep cú pháp cũ) trước khi coi một lần sửa quy trình là xong; làm rõ cách xác định NNN cho ADR (liệt kê thư mục).

## Vòng 5 — QA Engineer (chốt lại, dừng rà soát thêm)
Phát hiện: chính log của 4 vòng QA trước chỉ tồn tại trong plan file cục bộ (`C:\Users\...\.claude\plans\...`), không nằm trong repo — lặp lại đúng loại lỗi đã bắt ở vòng 2 (tài liệu trỏ tới thứ không ai đọc lại được), chỉ khác là lần này là toàn bộ lịch sử rà soát chứ không phải 1 dòng README. Quyết định: tạo file này để chốt lại, dừng rà soát tài liệu thêm ở đây — chưa có dữ liệu thực tế thứ hai để đánh giá tiếp có ý nghĩa, tiếp tục đọc lại văn bản nhiều khả năng chỉ tạo thêm ý kiến chủ quan.

**Bước tiếp theo (chưa làm):** chạy một project thứ hai qua toàn bộ quy trình — ưu tiên có ít nhất 2 tính năng nối tiếp trong cùng project, để kiểm chứng thật cơ chế `<project-slug>`/`<feature-slug>` — rồi mới rà soát tiếp dựa trên bằng chứng thay vì suy đoán.
