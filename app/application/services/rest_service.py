"""Rest interval suggestions for training clients."""

from app.domain.workout.services import suggested_rest_seconds


def rest_suggestion(reps: int | None, weight_kg: float | None) -> dict:
    seconds = suggested_rest_seconds(reps=reps, weight_kg=weight_kg)
    return {
        "suggested_rest_seconds": seconds,
        "suggested_rest_minutes": round(seconds / 60, 1),
    }
