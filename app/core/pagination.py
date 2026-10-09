"""Pagination clamp helpers."""

from app.core.limits import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


def clamp_limit(limit: int | None, default: int = DEFAULT_PAGE_SIZE) -> int:
    if limit is None:
        return default
    return max(1, min(int(limit), MAX_PAGE_SIZE))


def clamp_skip(skip: int | None) -> int:
    if skip is None or skip < 0:
        return 0
    return int(skip)
