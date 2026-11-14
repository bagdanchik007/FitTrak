"""Approximate MET values for common training modes (portfolio demo)."""

MET_BY_ACTIVITY: dict[str, float] = {
    "walking": 3.5,
    "jogging": 7.0,
    "running": 9.8,
    "cycling": 6.8,
    "strength": 5.0,
    "hiit": 8.0,
    "yoga": 3.0,
    "rowing": 7.0,
    "swimming": 8.0,
    "general": 5.0,
}


def met_for(activity: str | None) -> float:
    key = (activity or "general").strip().lower()
    return MET_BY_ACTIVITY.get(key, MET_BY_ACTIVITY["general"])
