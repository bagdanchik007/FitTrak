from app.domain.workout.duration_band import duration_band

def band_for_minutes(minutes: int | None) -> dict:
    return {"minutes": minutes, "band": duration_band(minutes)}
