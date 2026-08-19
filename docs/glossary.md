# Giải thích thuật ngữ

**SDLC (Software Development Life Cycle):** Vòng đời phát triển phần mềm — chuỗi giai đoạn từ ý tưởng đến bảo trì.

**User story:** Mô tả một yêu cầu từ góc nhìn người dùng, kèm tiêu chí chấp nhận để biết khi nào coi là "xong".

**Acceptance criteria:** Điều kiện cụ thể để xác nhận một tính năng đáp ứng đúng yêu cầu, thường viết dạng Given/When/Then.

**ADR (Architecture Decision Record):** Bản ghi lại một quyết định kiến trúc — bối cảnh, các phương án đã cân nhắc, lý do chọn, hệ quả. Giúp người sau (hoặc chính mình sau này) hiểu vì sao hệ thống được thiết kế như vậy.

**DoD (Definition of Done):** Danh sách điều kiện để coi một task là hoàn thành (vd: có test, test pass, không hardcode secret).

**PR (Pull Request):** Đề xuất gộp thay đổi từ một nhánh vào nhánh chính, kèm mô tả để người khác (hoặc chính mình) review trước khi merge.

**Conventional Commits:** Quy ước đặt tên commit dạng `type(scope): mô tả`, ví dụ `feat(auth): thêm đăng nhập Google`, `fix(api): sửa lỗi timeout`.

**CI/CD (Continuous Integration/Continuous Deployment):** Tự động chạy test/build (CI) và tự động triển khai (CD) mỗi khi có thay đổi code, thường qua pipeline như GitHub Actions.

**Semver (Semantic Versioning):** Cách đặt số version dạng MAJOR.MINOR.PATCH — MAJOR khi thay đổi phá vỡ tương thích ngược, MINOR khi thêm tính năng mới tương thích ngược, PATCH khi chỉ sửa lỗi.

**Changelog:** File ghi lại lịch sử thay đổi của phần mềm theo từng version, giúp người dùng biết version mới có gì khác.

**Retro (Retrospective):** Buổi nhìn lại một vòng làm việc để rút kinh nghiệm — cái gì hiệu quả, cái gì nên cải thiện.
