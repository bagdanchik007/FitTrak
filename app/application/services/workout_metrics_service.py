"""Derived workout metrics for API responses."""

from app.domain.workout.services import (
    duration_band,
    average_working_weight,
    calculate_session_volume,
    count_completed_sets,
    density_band,
    estimate_1rm,
    sets_per_minute,
    average_rpe,
    duration_band,
    volume_load_band,
)


def session_metrics(sets, duration_minutes: int | None) -> dict:
    completed = count_completed_sets(sets)
    volume = calculate_session_volume(sets)
    spm = sets_per_minute(completed, duration_minutes)
    heaviest_1rm = None
    for s in sets:
        w = getattr(s, "weight_kg", None)
        r = getattr(s, "reps", None)
        if w is not None and r is not None and r > 0:
            est = estimate_1rm(float(w), int(r))
            if est is not None and (heaviest_1rm is None or est > heaviest_1rm):
                heaviest_1rm = est
    return {
        "total_volume_kg": volume,
        "completed_sets": completed,
        "sets_per_minute": spm,
        "estimated_peak_1rm_kg": heaviest_1rm,
        "density_band": density_band(spm),
        "average_working_weight_kg": average_working_weight(sets),
        "volume_load_band": volume_load_band(volume),
        "average_rpe": average_rpe(sets),
        "duration_band": duration_band(duration_minutes),
    }
