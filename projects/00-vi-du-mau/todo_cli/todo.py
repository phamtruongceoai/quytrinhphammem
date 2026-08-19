def _find(items: list[dict], item_id: int) -> dict:
    for item in items:
        if item["id"] == item_id:
            return item
    raise ValueError(f"Không tìm thấy việc với id {item_id}")


def add_item(items: list[dict], text: str) -> list[dict]:
    next_id = max((item["id"] for item in items), default=0) + 1
    return items + [{"id": next_id, "text": text, "done": False}]


def mark_done(items: list[dict], item_id: int) -> list[dict]:
    _find(items, item_id)
    return [
        {**item, "done": True} if item["id"] == item_id else item
        for item in items
    ]


def delete_item(items: list[dict], item_id: int) -> list[dict]:
    _find(items, item_id)
    return [item for item in items if item["id"] != item_id]
