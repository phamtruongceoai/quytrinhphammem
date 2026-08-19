# Quy trình phát triển phần mềm với Claude Code

Đây là nguồn sự thật (source of truth) cho toàn bộ quy trình. Mọi slash command trong `.claude/commands/` đều bám theo tài liệu này. Nếu quy trình thay đổi, sửa ở đây trước, rồi mới sửa command.

## Hai loại định danh: project-slug và feature-slug

Tài liệu này dùng 2 ký hiệu khác nhau, đừng nhầm lẫn:
- **`<project-slug>`**: tên thư mục project, cố định suốt vòng đời — `projects/<project-slug>/`. Một project có thể có **nhiều tính năng** theo thời gian.
- **`<feature-slug>`**: tên ngắn của một tính năng cụ thể đang làm trong project đó, dùng để đặt tên file trong `docs/requirements/`, `docs/tasks/`, và tiếp đầu ngữ ADR trong `docs/adr/`. Mỗi tính năng mới trong cùng một project dùng một `<feature-slug>` khác nhau — không dùng lại `<project-slug>` làm tên file, vì sẽ ghi đè tính năng trước đó.

Ví dụ: project `projects/blog/` có thể lần lượt có `docs/requirements/dang-bai.md`, rồi sau này `docs/requirements/binh-luan.md` — cùng một `<project-slug>` là `blog`, khác `<feature-slug>`.

## Nguyên tắc chung

- **Mỗi project cụ thể nằm trong `projects/<project-slug>/`**, có `CLAUDE.md` riêng (copy từ `templates/CLAUDE.md.template`). Không code trực tiếp ở thư mục gốc.
- **3 giai đoạn đầu (Yêu cầu, Thiết kế, Lập kế hoạch) luôn dừng lại chờ người duyệt** trước khi sang giai đoạn kế tiếp — Claude không tự ý code khi chưa có yêu cầu/thiết kế/kế hoạch được chốt. Quy tắc này áp dụng khi thực sự chạy qua các giai đoạn đó — **với thay đổi rất nhỏ** (một dòng, một cấu hình, không ảnh hưởng logic), có thể bỏ qua cả 3 giai đoạn đầu và làm thẳng qua `/new-feature` hoặc skill cá nhân có sẵn (`sua-loi`), không bắt buộc phải chạy đủ pipeline cho mọi thay đổi dù nhỏ.
- **Dùng skill có sẵn của Claude Code khi có thể**, không tự tạo command trùng chức năng:
  - `/init` — làm giàu CLAUDE.md dựa trên code đã có (tuỳ chọn, chạy sau khi project đã có code thật — không hữu ích khi project còn trống)
  - `/code-review` — review chất lượng code (bug, đơn giản hoá, hiệu năng)
  - `/security-review` — review bảo mật khi đụng auth/dữ liệu người dùng/input từ bên ngoài
  - `/simplify` — dọn code trước khi PR
  - `run` — chạy thử app thật trong trình duyệt/terminal để xác nhận tính năng hoạt động
  - Plan Mode — dùng khi thảo luận kiến trúc mà chưa muốn sửa code
- **Mọi hành động khó đảo ngược** (git push, tạo PR thật, tag release, xoá dữ liệu) đều phải có bước dừng lại xin xác nhận rõ ràng.

## Bản đồ 9 giai đoạn

| # | Giai đoạn | Command/Skill | Dừng chờ duyệt? |
|---|-----------|----------------|------------------|
| 1 | Ý tưởng & yêu cầu | `/requirements` | Có |
| 2 | Thiết kế kiến trúc | `/design` | Có |
| 3 | Lập kế hoạch/breakdown task | `/plan-task` | Có |
| 4 | Coding | `/new-feature` (+ `/init` tuỳ chọn sau khi có code) | Không (nhưng báo cáo file đã đổi) |
| 5 | Testing | Tích hợp trong `/new-feature` + skill `run` | Không |
| 6 | Code review | `/code-review`, `/security-review`, `/simplify` | Có (đọc kết quả trước khi sang PR) |
| 7 | Commit/PR | `/pr` | Có (không tự push) |
| 8 | CI/CD & Release | `/release <project-slug> <version>` | Có (chỉ tag khi xác nhận) |
| 9 | Bảo trì/changelog | `/retro`, tái dùng `/new-feature` cho bugfix | Không bắt buộc |

### Vòng lặp, không phải đường thẳng

9 giai đoạn trên được đánh số để dễ theo dõi, nhưng phần mềm thực tế hiếm khi đi thẳng 1→9. Quay lại giai đoạn trước là bình thường, không phải thất bại:
- `/code-review` phát hiện quyết định kiến trúc sai → quay lại `/design`, cập nhật hoặc thêm ADR mới, rồi làm lại `/plan-task` cho phần bị ảnh hưởng.
- Viết test ở giai đoạn 5 lộ ra một acceptance criteria bị thiếu → quay lại `/requirements`, bổ sung, rồi kiểm tra lại task breakdown có cần đổi không.
- `/retro` sau một vòng release phát hiện task breakdown ước lượng sai quy mô → điều chỉnh cách chia task ở `/plan-task` cho vòng sau, không cần sửa code đã xong.

---

## Giai đoạn 1 — Ý tưởng & yêu cầu

**Input:** Ý tưởng thô, một câu mô tả vấn đề cần giải quyết.

**Output:** `projects/<project-slug>/docs/requirements/<feature-slug>.md` (điền theo `templates/user-story.md`) — gồm mục tiêu, phạm vi (trong/ngoài), người dùng mục tiêu, tiêu chí chấp nhận (acceptance criteria) dạng Given/When/Then.

**Cách dùng Claude Code:** `/requirements <mô tả ngắn>`. Claude sẽ hỏi lại các điểm chưa rõ (phạm vi, ràng buộc, ưu tiên) thay vì tự đoán, xác định `<feature-slug>` phù hợp rồi ghi file. Dừng lại, không tự chuyển sang thiết kế.

## Giai đoạn 2 — Thiết kế kiến trúc

**Input:** File requirements đã duyệt ở giai đoạn 1.

**Output:** `projects/<project-slug>/docs/adr/NNN-<feature-slug>.md` (điền theo `templates/adr-template.md`) — ghi lại 2-3 phương án đã cân nhắc, lý do chọn, trade-off, hệ quả. NNN tăng dần theo file lớn nhất đã có trong `docs/adr/` của project đó.

**Cách dùng Claude Code:** `/design <feature-slug>`. Nên bật **Plan Mode** khi thảo luận để Claude không sửa code trong lúc chỉ đang bàn kiến trúc. Dừng lại chờ duyệt ADR trước khi lập kế hoạch task.

## Giai đoạn 3 — Lập kế hoạch / breakdown task

**Input:** Requirements + ADR đã duyệt.

**Output:** `projects/<project-slug>/docs/tasks/<feature-slug>.md` (điền theo `templates/task-breakdown.md`) — danh sách task nhỏ, mỗi task có mục tiêu, file liên quan, Definition of Done (DoD), đánh dấu task rủi ro cao. Nếu công cụ theo dõi task (TodoWrite) khả dụng trong phiên làm việc, tạo thêm danh sách tương ứng — không bắt buộc nếu môi trường không hỗ trợ.

**Cách dùng Claude Code:** `/plan-task <feature-slug>`. Nếu thiếu requirements/ADR, Claude sẽ đề nghị chạy `/requirements`/`/design` trước thay vì tự suy diễn. Dừng lại, **không code**, chờ duyệt danh sách task.

## Giai đoạn 4 — Coding

**Input:** Task đã duyệt (một task cụ thể trong danh sách).

**Output:** Code + test tương ứng, nằm trong `projects/<project-slug>/`.

**Cách dùng Claude Code:**
- Nếu là project hoàn toàn mới (chưa có CLAUDE.md): tạo CLAUDE.md trực tiếp từ `templates/CLAUDE.md.template` (dựa trên requirements/ADR đã có), không cần chờ có code mới tạo. `/init` (skill có sẵn) chỉ nên chạy **sau khi đã có code thật** như bước tuỳ chọn để làm giàu thêm CLAUDE.md — chạy `/init` khi project còn trống gần như không có gì để phân tích.
- Với từng task: `/new-feature <mô tả task hoặc số thứ tự task>`. Claude đọc CLAUDE.md của project con + task đã duyệt, code đúng phạm vi, viết test theo DoD, không hardcode secret, bám theo pattern code đã có. Nếu task đang làm được đánh dấu rủi ro Cao trong task breakdown, chạy `/code-review` ngay sau khi xong task đó, trước khi sang task tiếp theo (xem giai đoạn 6).

## Giai đoạn 5 — Testing

**Input:** Code vừa viết ở giai đoạn 4.

**Output:** Kết quả test pass thật (không phải giả định).

**Cách dùng Claude Code:** Test được viết ngay trong `/new-feature` nếu DoD yêu cầu. Để xác nhận tính năng chạy được trong thực tế (không chỉ qua test), dùng skill `run` để khởi động và thao tác thử app.

## Giai đoạn 6 — Code review

**Input:** Diff của code vừa hoàn thành một task hoặc một nhóm task.

**Output:** Danh sách phát hiện (nếu có) đã được xử lý hoặc ghi nhận có chủ đích bỏ qua.

**Cách dùng Claude Code:**
- `/code-review` (effort `medium` là đủ cho học một mình; tăng lên `high`/`ultra` nếu thay đổi lớn/nhạy cảm).
- `/security-review` nếu task đụng đến auth, dữ liệu người dùng, input từ bên ngoài, hoặc gọi API bên thứ ba.
- `/simplify` (tuỳ chọn) để dọn code trước khi tạo PR, miễn không phá test.

Đọc kỹ kết quả trước khi sang giai đoạn PR — không bỏ qua finding mà không có lý do.

Có thể gộp review sau nhiều task nhỏ, rủi ro thấp (đỡ tốn thời gian chạy lặp lại); **nên review riêng ngay sau từng task nếu task đó được đánh dấu rủi ro Cao** trong task breakdown (xem nhắc ở giai đoạn 4) — gộp review ở nhóm task rủi ro cao dễ làm bug tích tụ, khó truy về đúng task gây lỗi.

## Giai đoạn 7 — Commit / PR

**Input:** Code đã qua review ở giai đoạn 6.

**Output:** `projects/<project-slug>/docs/pr/<feature-slug>-<mô-tả-ngắn>.md` (điền theo `templates/pr-checklist.md`) + commit message soạn sẵn. Một PR không nhất thiết ứng với 1 task — có thể gộp nhiều task nhỏ, đặt tên theo nội dung PR chứ không ép theo tên task.

**Cách dùng Claude Code:** `/pr <mô tả>`. Claude xác nhận đã chạy `/code-review` (và `/security-review` nếu cần) trước khi cho phép tiếp tục, điền checklist dựa trên diff thật, soạn commit message theo Conventional Commits và PR description (Summary/Changes/Test plan). **Không tự ý `git push` hay tạo PR thật** — luôn đưa ra để người dùng xác nhận.

## Giai đoạn 8 — CI/CD & Release

**Input:** Các commit đã gộp vào nhánh chính kể từ lần release trước.

**Output:**
- `CHANGELOG.md` ở gốc project con (`projects/<project-slug>/CHANGELOG.md`) — cập nhật định dạng Keep a Changelog.
- Version bump theo semver ở đúng file khai báo version.
- `projects/<project-slug>/docs/release/<version>.md` (điền theo `templates/release-notes-template.md`) — release notes cho version mới.

**Cách dùng Claude Code:** `/release <project-slug> <version>`. Claude liệt kê commit từ tag gần nhất, xác nhận test pass, chuyển mục "Unreleased" sang version mới, bump version ở đúng file khai báo (package.json/pyproject.toml/`<package>/__init__.py` nếu project không có packaging/...), viết release notes vào `docs/release/<version>.md`. **Chỉ tạo git tag khi được xác nhận rõ ràng.**

**Đặt tên tag:** repo này chứa nhiều project con (`projects/<project-slug>/`) dùng chung một lịch sử git — tag phải gắn `<project-slug>` để không đụng nhau giữa các project, dạng `<project-slug>-v<version>` (vd `todo-cli-v0.1.0`), thay vì `v<version>` trần. Version áp dụng cho toàn bộ project con (không phải riêng từng tính năng), vì CHANGELOG/file khai báo version cũng ở cấp project con.

Về CI/CD thật (GitHub Actions, v.v.): vì quy trình này không gắn cứng vào một stack, việc thiết lập pipeline CI cụ thể (lint/test/build tự động khi push) nên làm ở giai đoạn 4 của từng project con, dựa theo stack thực tế của project đó — tham khảo cấu trúc `.github/workflows/` chuẩn nếu deploy lên GitHub.

## Giai đoạn 9 — Bảo trì / changelog

**Input:** Phản hồi, bug phát sinh sau release, hoặc ý tưởng cải tiến.

**Output:** `projects/<project-slug>/docs/retro/<ngày>.md` (bài học rút ra); bugfix mới đi qua lại `/new-feature` (hoặc skill cá nhân có sẵn) rồi quay lại giai đoạn 6-8.

**Cách dùng Claude Code:** `/retro` sau mỗi vòng release để ghi lại: cái gì hiệu quả, cái gì nên làm khác đi, có nên chỉnh sửa command/tài liệu quy trình này không.
