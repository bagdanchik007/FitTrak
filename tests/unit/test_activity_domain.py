from datetime import date

from app.domain.activity.services import sort_activity_items


def test_sort_activity_items():
    items = [
        {"title": "a", "occurred_on": date(2026, 1, 1)},
        {"title": "b", "occurred_on": date(2026, 2, 1)},
    ]
    sorted_items = sort_activity_items(items, limit=1)
    assert len(sorted_items) == 1
    assert sorted_items[0]["title"] == "b"
