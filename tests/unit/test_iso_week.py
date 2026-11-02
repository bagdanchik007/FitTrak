from datetime import date
from app.domain.calendar.week import iso_week_key

def test_key():
    assert iso_week_key(date(2026, 1, 5)).startswith("2026-W")
