"""Map consistency score 0–100 to a band label."""

def consistency_band(score: float | None) -> str:
    if score is None:
        return "unknown"
    if score >= 85:
        return "excellent"
    if score >= 65:
        return "solid"
    if score >= 40:
        return "building"
    return "starting"
