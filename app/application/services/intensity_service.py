from app.domain.intensity.zone import intensity_zone

def zone_for_rpe(rpe: float | None) -> dict:
    return {"rpe": rpe, "zone": intensity_zone(rpe)}
