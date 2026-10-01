"""Derived workout metrics for API responses."""

from app.domain.workout.services import calculate_session_volume, count_completed_sets, sets_per_minute


def session_metrics(sets, duration_minutes: int | None) -> dict:
    completed = count_completed_sets(sets)
    return {
        "total_volume_kg": calculate_session_volume(sets),
        "completed_sets": completed,
        "sets_per_minute": sets_per_minute(completed, duration_minutes),
    }
