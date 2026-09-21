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
