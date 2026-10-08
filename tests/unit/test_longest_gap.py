from datetime import date
from app.domain.streak.services import longest_gap_days

def test_longest_gap_days():
    d = [date(2026, 1, 1), date(2026, 1, 3), date(2026, 1, 10)]
    assert longest_gap_days(d) == 7
    assert longest_gap_days([date(2026, 1, 1)]) is None
