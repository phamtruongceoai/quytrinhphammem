import pytest

from todo_cli import todo


def test_add_item_assigns_incrementing_id():
    items = todo.add_item([], "Mua sữa")
    items = todo.add_item(items, "Đi chợ")

    assert [item["id"] for item in items] == [1, 2]
    assert items[0]["text"] == "Mua sữa"
    assert items[0]["done"] is False


def test_mark_done_updates_only_target_item():
    items = todo.add_item([], "Mua sữa")
    items = todo.add_item(items, "Đi chợ")

    items = todo.mark_done(items, 1)

    assert items[0]["done"] is True
    assert items[1]["done"] is False


def test_delete_item_removes_target_and_does_not_reuse_id():
    items = todo.add_item([], "Mua sữa")
    items = todo.add_item(items, "Đi chợ")

    items = todo.delete_item(items, 1)
    items = todo.add_item(items, "Nấu cơm")

    assert [item["id"] for item in items] == [2, 3]


def test_mark_done_unknown_id_raises_value_error():
    with pytest.raises(ValueError):
        todo.mark_done([], 99)


def test_delete_item_unknown_id_raises_value_error():
    with pytest.raises(ValueError):
        todo.delete_item([], 99)
