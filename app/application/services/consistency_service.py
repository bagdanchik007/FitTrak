"""Training consistency helpers."""

from app.domain.streak.services import consistency_score


def consistency_report(workout_days: int, window_days: int = 28) -> dict:
    score = consistency_score(workout_days, window_days)
    if score >= 0.75:
        band = "high"
    elif score >= 0.4:
        band = "medium"
    else:
        band = "low"
    return {
        "workout_days": workout_days,
        "window_days": window_days,
        "score": score,
        "band": band,
    }
