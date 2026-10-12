"""Notification pure helpers."""


def notification_priority(kind: str) -> int:
    order = {"security": 1, "goal": 2, "streak": 3, "tip": 4}
    return order.get(kind, 5)


def sort_notifications(items: list[dict]) -> list[dict]:
    return sorted(
        items,
        key=lambda x: (notification_priority(str(x.get("kind") or "")), x.get("created_at") or ""),
    )
