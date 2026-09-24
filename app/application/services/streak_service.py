"""Application wrapper around streak domain logic."""

from datetime import date

from app.domain.streak.services import compute_current_streak, compute_longest_streak


class StreakService:
    def summarize(self, workout_days: list[date], today: date | None = None) -> dict:
        return {
            "current_streak_days": compute_current_streak(workout_days, today=today),
            "longest_streak_days": compute_longest_streak(workout_days),
            "total_workout_days": len(set(workout_days)),
            "last_workout_date": max(workout_days) if workout_days else None,
        }
