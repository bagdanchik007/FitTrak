"""Sort and limit activity feed items."""

from datetime import date
from typing import Any


def sort_activity_items(items: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    sorted_items = sorted(items, key=lambda x: x.get("occurred_on") or date.min, reverse=True)
    return sorted_items[: max(1, limit)]
