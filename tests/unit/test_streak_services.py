from datetime import date, timedelta

from app.domain.streak.services import compute_current_streak, compute_longest_streak


def test_current_streak():
    today = date(2026, 10, 12)
    days = [today, today - timedelta(days=1), today - timedelta(days=2)]
    assert compute_current_streak(days, today=today) == 3


def test_longest_streak():
    days = [
        date(2026, 1, 1),
        date(2026, 1, 2),
        date(2026, 1, 3),
        date(2026, 1, 10),
    ]
    assert compute_longest_streak(days) == 3
