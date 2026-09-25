from datetime import datetime, timezone
from uuid import uuid4

from app.application.services.template_service import template_overview
from app.domain.template.entities import TemplateItem, WorkoutTemplate


def test_template_overview():
    tid = uuid4()
    now = datetime.now(timezone.utc)
    t = WorkoutTemplate(
        tid,
        uuid4(),
        "Legs",
        "heavy",
        now,
        now,
        items=[TemplateItem(uuid4(), tid, uuid4(), 5, 5, 0)],
    )
    overview = template_overview(t)
    assert overview["name"] == "Legs"
    assert overview["item_count"] == 1
    assert overview["total_target_sets"] == 5
