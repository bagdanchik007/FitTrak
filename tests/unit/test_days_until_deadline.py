from datetime import date
from app.domain.goal.progress import days_until_deadline

def test_days_until_deadline():
    assert days_until_deadline(date(2026, 11, 10), date(2026, 11, 1)) == 9
    assert days_until_deadline(None, date.today()) is None
