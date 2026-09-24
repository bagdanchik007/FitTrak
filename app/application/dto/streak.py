from datetime import date

from pydantic import BaseModel


class StreakSummaryDTO(BaseModel):
    current_streak_days: int
    longest_streak_days: int
    last_workout_date: date | None
    total_workout_days: int
