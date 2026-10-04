"""Recovery / rest-day helpers for clients."""

from datetime import date

from app.domain.streak.services import rest_days_since


def recovery_snapshot(last_workout: date | None, today: date | None = None) -> dict:
    today = today or date.today()
    rest = rest_days_since(last_workout, today)
    if rest is None:
        status = "never"
        recommendation = "log_first_workout"
    elif rest == 0:
        status = "trained_today"
        recommendation = "optional_recovery"
    elif rest == 1:
        status = "resting"
        recommendation = "ready_to_train"
    else:
        status = "resting"
        recommendation = "consider_session"
    return {
        "last_workout_date": last_workout.isoformat() if last_workout else None,
        "rest_days": rest,
        "status": status,
        "recommendation": recommendation,
    }
