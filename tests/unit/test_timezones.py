from datetime import datetime, timezone

from app.core.timezones import ensure_utc, utc_iso


def test_ensure_utc_naive():
    dt = datetime(2026, 1, 1, 12, 0, 0)
    assert ensure_utc(dt).tzinfo == timezone.utc


def test_utc_iso():
    dt = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    assert "2026-01-01" in utc_iso(dt)
