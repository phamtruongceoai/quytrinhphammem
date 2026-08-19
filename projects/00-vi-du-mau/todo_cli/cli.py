import argparse
from pathlib import Path

from todo_cli import storage, todo

DATA_FILE = Path(__file__).resolve().parent.parent / "todos.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo_cli")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add", help="Thêm một việc cần làm")
    add_parser.add_argument("text")

    sub.add_parser("list", help="Xem danh sách việc cần làm")

    done_parser = sub.add_parser("done", help="Đánh dấu một việc đã hoàn thành")
    done_parser.add_argument("id", type=int)

    delete_parser = sub.add_parser("delete", help="Xóa một việc")
    delete_parser.add_argument("id", type=int)

    return parser


def _format_item(item: dict) -> str:
    mark = "x" if item["done"] else " "
    return f"[{mark}] {item['id']}: {item['text']}"


def main(argv: list[str] | None = None, data_file: Path = DATA_FILE) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        items = storage.load(data_file)

        if args.command == "add":
            items = todo.add_item(items, args.text)
            storage.save(data_file, items)
            print(f"Đã thêm: {args.text}")
        elif args.command == "list":
            if not items:
                print("Danh sách trống.")
            for item in items:
                print(_format_item(item))
        elif args.command == "done":
            items = todo.mark_done(items, args.id)
            storage.save(data_file, items)
            print(f"Đã đánh dấu hoàn thành: {args.id}")
        elif args.command == "delete":
            items = todo.delete_item(items, args.id)
            storage.save(data_file, items)
            print(f"Đã xóa: {args.id}")
    except ValueError as exc:
        print(f"Lỗi: {exc}")
        return 1

    return 0
