"""Count workouts per ISO week from performed dates."""

from collections import Counter
from datetime import date

from app.domain.calendar.week import iso_week_key

def counts_by_week(dates: list[date]) -> dict[str, int]:
    return dict(Counter(iso_week_key(d) for d in dates))
