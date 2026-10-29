"""Simple recovery day suggestion from recent training days."""

def suggest_rest(*, trained_last_7_days: int) -> dict:
    if trained_last_7_days >= 6:
        return {"rest_recommended": True, "reason": "high_frequency"}
    if trained_last_7_days >= 4:
        return {"rest_recommended": False, "reason": "moderate"}
    return {"rest_recommended": False, "reason": "low_frequency"}
