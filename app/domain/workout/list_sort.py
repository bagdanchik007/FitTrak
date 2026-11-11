"""Sort workout dicts by performed_at descending."""

from datetime import date

from app.domain.workout.sort_key import performed_sort_key
from app.domain.datetime_util.format_date import parse_iso_date


def sort_workouts_desc(items: list[dict]) -> list[dict]:
    def key(item: dict):
        raw = item.get("performed_at")
        if isinstance(raw, date):
            return performed_sort_key(raw)
        return performed_sort_key(parse_iso_date(str(raw) if raw else None))

    return sorted(items, key=key, reverse=True)
