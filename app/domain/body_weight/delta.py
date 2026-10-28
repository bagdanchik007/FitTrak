"""Body-weight delta helpers."""

def week_delta_kg(latest: float | None, prior: float | None) -> float | None:
    if latest is None or prior is None:
        return None
    return round(latest - prior, 2)

def trend_direction(delta: float | None) -> str:
    if delta is None:
        return "flat"
    if delta > 0.05:
        return "up"
    if delta < -0.05:
        return "down"
    return "flat"
