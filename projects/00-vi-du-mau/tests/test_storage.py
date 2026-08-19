from todo_cli import storage


def test_load_missing_file_returns_empty_list(tmp_path):
    path = tmp_path / "todos.json"
    assert storage.load(path) == []


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "todos.json"
    items = [{"id": 1, "text": "Mua sữa", "done": False}]

    storage.save(path, items)

    assert storage.load(path) == items
