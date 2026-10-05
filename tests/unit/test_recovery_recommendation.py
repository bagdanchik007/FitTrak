from datetime import date

from app.application.services.recovery_service import recovery_snapshot


def test_recovery_recommendations():
    assert recovery_snapshot(None, date(2026, 10, 4))["recommendation"] == "log_first_workout"
    assert (
        recovery_snapshot(date(2026, 10, 4), date(2026, 10, 4))["recommendation"]
        == "optional_recovery"
    )
    assert (
        recovery_snapshot(date(2026, 10, 3), date(2026, 10, 4))["recommendation"]
        == "ready_to_train"
    )
