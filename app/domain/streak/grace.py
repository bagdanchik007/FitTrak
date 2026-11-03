"""Whether a missed day can still keep a streak with a one-day grace."""

def streak_survives_grace(*, days_missed: int, grace_days: int = 1) -> bool:
    return 0 <= days_missed <= grace_days
