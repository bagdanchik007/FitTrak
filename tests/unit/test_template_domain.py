from datetime import datetime, timezone
from uuid import uuid4

from app.domain.template.entities import TemplateItem, WorkoutTemplate
from app.domain.template.services import sorted_items, total_target_sets


def _template() -> WorkoutTemplate:
    tid = uuid4()
    now = datetime.now(timezone.utc)
    items = [
        TemplateItem(uuid4(), tid, uuid4(), 3, 10, 1),
        TemplateItem(uuid4(), tid, uuid4(), 4, 8, 0),
    ]
    return WorkoutTemplate(tid, uuid4(), "Push", None, now, now, items=items)


def test_total_target_sets():
    assert total_target_sets(_template()) == 7


def test_sorted_items():
    items = sorted_items(_template())
    assert items[0].sort_order == 0
    assert items[1].sort_order == 1
