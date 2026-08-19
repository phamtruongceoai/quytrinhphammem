import json

from todo_cli.cli import main


def test_add_list_done_delete_flow(tmp_path, capsys):
    data_file = tmp_path / "todos.json"

    assert main(["add", "Mua sữa"], data_file=data_file) == 0
    assert main(["add", "Đi chợ"], data_file=data_file) == 0

    main(["list"], data_file=data_file)
    out = capsys.readouterr().out
    assert "Mua sữa" in out
    assert "Đi chợ" in out

    assert main(["done", "1"], data_file=data_file) == 0
    items = json.loads(data_file.read_text(encoding="utf-8"))
    assert items[0]["done"] is True

    assert main(["delete", "1"], data_file=data_file) == 0
    items = json.loads(data_file.read_text(encoding="utf-8"))
    assert [item["id"] for item in items] == [2]


def test_done_unknown_id_reports_error_without_crash(tmp_path, capsys):
    data_file = tmp_path / "todos.json"

    exit_code = main(["done", "99"], data_file=data_file)

    assert exit_code == 1
    assert "Lỗi" in capsys.readouterr().out


def test_corrupted_data_file_reports_error_without_crash(tmp_path, capsys):
    data_file = tmp_path / "todos.json"
    data_file.write_text("not valid json {{{", encoding="utf-8")

    exit_code = main(["list"], data_file=data_file)

    assert exit_code == 1
    assert "Lỗi" in capsys.readouterr().out
