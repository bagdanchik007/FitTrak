"""Recovery / rest-day helpers for clients."""

from datetime import date

from app.domain.streak.services import rest_days_since


def recovery_snapshot(last_workout: date | None, today: date | None = None) -> dict:
    today = today or date.today()
    rest = rest_days_since(last_workout, today)
    return {
        "last_workout_date": last_workout,
        "rest_days": rest,
        "status": (
            "never"
            if rest is None
            else "trained_today"
            if rest == 0
            else "resting"
        ),
    }
