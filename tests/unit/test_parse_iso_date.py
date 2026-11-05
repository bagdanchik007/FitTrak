from datetime import date
from app.domain.datetime_util.format_date import parse_iso_date

def test_parse():
    assert parse_iso_date("2026-03-01") == date(2026, 3, 1)
