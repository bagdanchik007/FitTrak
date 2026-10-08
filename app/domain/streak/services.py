"""Calendar-day streak calculations (pure)."""

from datetime import date, timedelta


def compute_current_streak(workout_days: list[date], today: date | None = None) -> int:
    if not workout_days:
        return 0
    today = today or date.today()
    days = sorted(set(workout_days), reverse=True)
    if days[0] < today - timedelta(days=1):
        return 0
    streak = 0
    expected = days[0]
    for d in days:
        if d == expected:
            streak += 1
            expected = d - timedelta(days=1)
        elif d < expected:
            break
    return streak


def compute_longest_streak(workout_days: list[date]) -> int:
    if not workout_days:
        return 0
    asc = sorted(set(workout_days))
    longest = run = 1
    for i in range(1, len(asc)):
        if asc[i] == asc[i - 1] + timedelta(days=1):
            run += 1
            longest = max(longest, run)
        else:
            run = 1
    return longest


def rest_days_since(last_workout, today) -> int | None:
    """Whole days since last workout date; None if never trained."""
    if last_workout is None:
        return None
    delta = (today - last_workout).days
    return max(0, delta)


def consistency_score(workout_days: int, window_days: int = 28) -> float:
    """Share of days trained in a window, clamped to [0, 1]."""
    if window_days <= 0:
        return 0.0
    return round(min(1.0, max(0.0, workout_days / window_days)), 3)


def longest_gap_days(sorted_dates: list) -> int | None:
    """Largest gap in days between consecutive workout dates; None if <2 dates."""
    if len(sorted_dates) < 2:
        return None
    gaps = []
    for i in range(1, len(sorted_dates)):
        gaps.append((sorted_dates[i] - sorted_dates[i - 1]).days)
    return max(gaps) if gaps else None
