"""Timezone helpers (UTC-first)."""

from datetime import datetime, timezone


def ensure_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def utc_iso(dt: datetime) -> str:
    return ensure_utc(dt).isoformat()
