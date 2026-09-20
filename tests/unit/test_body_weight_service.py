from datetime import date, datetime, timezone
from uuid import uuid4

from app.application.services.body_weight_service import delta_kg
from app.domain.body_weight.entities import BodyWeightEntry


def test_delta_kg():
    uid = uuid4()
    now = datetime.now(timezone.utc)
    entries = [
        BodyWeightEntry(uuid4(), uid, date(2026, 1, 1), 80.0, None, now),
        BodyWeightEntry(uuid4(), uid, date(2026, 2, 1), 78.5, None, now),
    ]
    assert delta_kg(entries) == -1.5
    assert delta_kg(entries[:1]) is None
