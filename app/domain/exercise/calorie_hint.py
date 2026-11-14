"""Suggest activity key for calorie estimates from exercise muscle group / name."""

def activity_key_from_exercise(*, name: str | None = None, muscle_group: str | None = None) -> str:
    text = f"{name or ''} {muscle_group or ''}".lower()
    if any(w in text for w in ("run", "jog", "sprint")):
        return "running"
    if "walk" in text:
        return "walking"
    if any(w in text for w in ("bike", "cycl")):
        return "cycling"
    if "swim" in text:
        return "swimming"
    if "yoga" in text:
        return "yoga"
    if any(w in text for w in ("hiit", "circuit")):
        return "hiit"
    return "strength"
