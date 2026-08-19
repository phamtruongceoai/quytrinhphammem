# CLAUDE.md — Khung quy trình làm phần mềm

Thư mục này là nơi lưu **quy trình phát triển phần mềm** (SDLC) áp dụng Claude Code, phục vụ mục đích cá nhân học tập. Đây **không phải** nơi chứa code app thật.

## Quy tắc quan trọng nhất

- **Nguồn sự thật của quy trình** là [docs/quy-trinh-phat-trien-phan-mem.md](docs/quy-trinh-phat-trien-phan-mem.md). Khi có mâu thuẫn giữa command và tài liệu này, tài liệu thắng — sửa tài liệu trước, sync lại command sau.
- **Mọi việc code cụ thể phải nằm trong `projects/<project-slug>/`**, mỗi project con có `CLAUDE.md` riêng (copy từ [templates/CLAUDE.md.template](templates/CLAUDE.md.template) và điền placeholder). Không code trực tiếp ở thư mục gốc này. Một project con có thể có nhiều tính năng (`<feature-slug>`) theo thời gian — xem quy ước 2 loại định danh trong nguồn sự thật.
- Khi làm việc trong repo này (không phải trong một project con), ưu tiên dùng slash command tương ứng giai đoạn (`/requirements`, `/design`, `/plan-task`, `/new-feature`, `/pr`, `/release`, `/retro`) thay vì code tự do, và tận dụng skill có sẵn (`/init`, `/code-review`, `/security-review`, `/simplify`) thay vì tự chế lại.
- 3 giai đoạn đầu (yêu cầu, thiết kế, lập kế hoạch) luôn dừng lại chờ người dùng duyệt trước khi đi tiếp.
- Không tự ý `git push`, tạo PR thật, hay tạo git tag — luôn hỏi xác nhận trước các hành động khó đảo ngược.

## Ngôn ngữ
Giao tiếp và tài liệu bằng tiếng Việt. Code/comment trong từng project con theo quy ước riêng của project đó (thường tiếng Anh cho code, có thể tiếng Việt cho comment nếu phù hợp).

## Cấu trúc thư mục
```
.
├── docs/                                    # tài liệu quy trình gốc
├── templates/                               # mẫu dùng chung cho mọi project con
├── .claude/commands/                        # slash command triển khai quy trình
└── projects/<project-slug>/                 # từng project cụ thể, có CLAUDE.md riêng
```

## Tham khảo nhanh
- Bản đồ giai đoạn ↔ công cụ: [docs/ban-do-cong-cu.md](docs/ban-do-cong-cu.md)
- Giải thích thuật ngữ: [docs/glossary.md](docs/glossary.md)

## Trước khi sửa quy trình
Cú pháp một lệnh/đường dẫn output thường được nhắc lại ở nhiều nơi (doc nguồn, `ban-do-cong-cu.md`, `CLAUDE.md.template`, từng `CLAUDE.md` project con). Sau khi đổi cú pháp hoặc đường dẫn của một lệnh, chạy Grep tìm cú pháp/đường dẫn cũ trên toàn repo trước khi coi là xong — đừng chỉ dựa vào trí nhớ của phiên làm việc hiện tại.
