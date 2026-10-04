"""Derived workout metrics for API responses."""

from app.domain.workout.services import (
    calculate_session_volume,
    count_completed_sets,
    density_band,
    estimate_1rm,
    sets_per_minute,
)


def session_metrics(sets, duration_minutes: int | None) -> dict:
    completed = count_completed_sets(sets)
    heaviest_1rm = None
    for s in sets:
        w = getattr(s, "weight_kg", None)
        r = getattr(s, "reps", None)
        if w is not None and r is not None and r > 0:
            est = estimate_1rm(float(w), int(r))
            if est is not None and (heaviest_1rm is None or est > heaviest_1rm):
                heaviest_1rm = est
    return {
        "total_volume_kg": calculate_session_volume(sets),
        "completed_sets": completed,
        "sets_per_minute": sets_per_minute(completed, duration_minutes),
        "estimated_peak_1rm_kg": heaviest_1rm,
        "density_band": density_band(sets_per_minute(completed, duration_minutes)),
    }
