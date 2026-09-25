"""Weekly summary application helpers."""

from app.domain.summary.services import SessionStats, average_volume_per_workout, merge_session_stats


def build_weekly_totals(parts: list[SessionStats], workout_count: int) -> dict:
    merged = merge_session_stats(parts)
    return {
        "workouts": workout_count,
        "total_sets": merged.sets,
        "total_volume_kg": merged.volume_kg,
        "total_duration_minutes": merged.duration_minutes,
        "avg_volume_per_workout": average_volume_per_workout(merged.volume_kg, workout_count),
    }
