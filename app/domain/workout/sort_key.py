"""Sort key for workouts by performed date descending."""

from datetime import date

def performed_sort_key(performed_at: date | None) -> date:
    return performed_at or date.min
