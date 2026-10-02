from datetime import date

from app.application.services.recovery_service import recovery_snapshot
from app.domain.streak.services import rest_days_since


def test_rest_days_since():
    assert rest_days_since(date(2026, 10, 1), date(2026, 10, 4)) == 3
    assert rest_days_since(None, date(2026, 10, 4)) is None


def test_recovery_snapshot_resting():
    snap = recovery_snapshot(date(2026, 10, 1), today=date(2026, 10, 3))
    assert snap["status"] == "resting"
    assert snap["rest_days"] == 2
