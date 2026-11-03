"""Estimate weekly pace needed to hit a goal by deadline."""

def required_weekly_pace(*, remaining: float, weeks_left: float) -> float | None:
    if weeks_left <= 0:
        return None
    return round(remaining / weeks_left, 2)
