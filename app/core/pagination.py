"""Pagination helpers."""

from dataclasses import dataclass

from app.core.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


@dataclass(slots=True)
class PageParams:
    skip: int = 0
    limit: int = DEFAULT_PAGE_SIZE

    def __post_init__(self) -> None:
        self.skip = max(0, self.skip)
        self.limit = min(max(1, self.limit), MAX_PAGE_SIZE)


def clamp_limit(limit: int, default: int = DEFAULT_PAGE_SIZE, maximum: int = MAX_PAGE_SIZE) -> int:
    if limit < 1:
        return default
    return min(limit, maximum)
