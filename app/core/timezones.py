"""Timezone helpers (UTC-first)."""

from datetime import UTC, datetime


def ensure_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def utc_iso(dt: datetime) -> str:
    return ensure_utc(dt).isoformat()
