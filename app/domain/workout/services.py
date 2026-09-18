"""Domain service helpers for workouts (pure logic)."""

from app.domain.workout.entities import Workout, WorkoutSet


def calculate_session_volume(sets: list[WorkoutSet]) -> float:
    total = 0.0
    for s in sets:
        if s.weight_kg is not None and s.reps is not None:
            total += s.weight_kg * s.reps
    return round(total, 2)


def count_sets(workout: Workout) -> int:
    return len(workout.sets)


def estimate_1rm(weight_kg: float, reps: int) -> float | None:
    """Epley approximation."""
    if reps <= 0 or weight_kg <= 0:
        return None
    return round(weight_kg * (1 + reps / 30), 1)
