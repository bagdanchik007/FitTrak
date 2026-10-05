from datetime import UTC, datetime

from app.core.timezones import ensure_utc, utc_iso


def test_ensure_utc_naive():
    dt = datetime(2026, 1, 1, 12, 0, 0)
    assert ensure_utc(dt).tzinfo == UTC


def test_utc_iso():
    dt = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)
    assert "2026-01-01" in utc_iso(dt)
