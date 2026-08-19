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

## Vòng 6 — Retro (`/retro`) cho cả cụm việc vòng 3-5 + tạo tài liệu hướng dẫn

Đây là lần đầu `/retro` được dùng cho việc **không thuộc một project con nào** (khác todo-cli ở Vòng 1) — bản thân việc này đã lộ ra `/retro` mặc định giả định luôn có `<project-slug>`, chưa tính tới trường hợp rút kinh nghiệm cho chính khung quy trình. Ghi tạm vào đây, không sửa command trong vòng này (chưa đủ dữ liệu để biết có cần một biến thể riêng hay không).

**Bài học cụ thể:**

1. **Để dồn nhiều vòng sửa chưa commit là rủi ro thật, không chỉ lý thuyết.** Vòng 3 và Vòng 4 đều để lại thay đổi trên đĩa chưa commit; phải tới khi làm Vòng 5 mới thực sự chốt. Nếu phiên làm việc bị ngắt giữa chừng ở Vòng 3 hoặc 4, toàn bộ phát hiện có nguy cơ mất trắng. Áp dụng: sau khi xong **mỗi vòng sửa nhỏ** (không phải mỗi cụm nhiều vòng), nên chủ động đề nghị commit ngay, thay vì gộp chờ đến khi được hỏi.

2. **Đưa ra khuyến nghị "nên dừng" một lần là chưa đủ để thực sự dừng.** Vòng 4 đã khuyến nghị rõ ràng dừng rà soát vì thiếu dữ liệu thực tế thứ hai — nhưng người dùng vẫn yêu cầu thêm Vòng 5. Cách xử lý đúng (đã làm ở Vòng 5) là hỏi thẳng bằng câu hỏi lựa chọn thay vì lặng lẽ làm thêm một vòng review nữa cho có — nên áp dụng ngay từ lần khuyến nghị đầu tiên bị bỏ qua, không đợi tới lần thứ hai.

3. **Yêu cầu tài liệu mới không nói rõ định dạng dễ bị suy đoán sai theo thói quen.** Khi nhận yêu cầu "viết hướng dẫn sử dụng chi tiết", mặc định lập kế hoạch thêm 1 file Markdown vào `docs/` (theo đúng pattern có sẵn của repo) mà không hỏi trước — trong khi người dùng thực ra muốn một định dạng khác hẳn (slide trình chiếu, đứng ngoài khung quy trình, không commit). Phải dừng kế hoạch giữa chừng và làm lại. Áp dụng: với yêu cầu tạo tài liệu/artefact mới mà chưa rõ định dạng đầu ra, hỏi rõ (file gì, có nằm trong repo không) **trước khi** viết kế hoạch, thay vì suy đoán theo pattern quen thuộc.

4. **Ngược lại, hỏi kỹ trước khi làm giúp thực thi suôn sẻ.** Một khi định dạng (trang trình chiếu dạng Artifact, không phải .pptx) và vị trí lưu đã được hỏi rõ qua câu hỏi trắc nghiệm, việc dựng 21 slide hoàn chỉnh diễn ra trong một lần, không phải sửa lại — xác nhận cách làm này hiệu quả, nên tiếp tục.

**Không đề xuất sửa command/tài liệu nào trong vòng này** — bài học chủ yếu là về cách tôi (Claude) vận hành phiên làm việc, không phải lỗ hổng trong nội dung quy trình 9 giai đoạn.
