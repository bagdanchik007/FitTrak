from datetime import date

from pydantic import BaseModel


class WeeklySummary(BaseModel):
    from_date: date
    to_date: date
    workouts: int
    total_sets: int
    total_volume_kg: float
    total_duration_minutes: int
