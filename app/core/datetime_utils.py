"""Datetime helpers."""

from datetime import UTC, date, datetime, timedelta


def utc_now() -> datetime:
    return datetime.now(UTC)


def today() -> date:
    return date.today()


def days_ago(n: int) -> date:
    return date.today() - timedelta(days=n)


def is_within_last_days(d: date, n: int) -> bool:
    return d >= days_ago(n)
