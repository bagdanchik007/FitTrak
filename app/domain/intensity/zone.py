"""Map RPE to a simple intensity zone label."""

def intensity_zone(rpe: float | None) -> str:
    if rpe is None:
        return "unknown"
    if rpe >= 9:
        return "maximal"
    if rpe >= 7:
        return "hard"
    if rpe >= 5:
        return "moderate"
    return "easy"
