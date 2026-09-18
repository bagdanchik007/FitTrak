from datetime import date, timedelta

from app.core.datetime_utils import days_ago, is_within_last_days, today


def test_days_ago():
    assert days_ago(0) == today()
    assert days_ago(1) == today() - timedelta(days=1)


def test_is_within_last_days():
    assert is_within_last_days(today(), 7) is True
    assert is_within_last_days(today() - timedelta(days=30), 7) is False
