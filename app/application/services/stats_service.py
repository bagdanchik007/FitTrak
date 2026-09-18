"""Aggregated stats for dashboard-style endpoints."""

from uuid import UUID

from app.domain.progress.repositories import ProgressRepository
from app.domain.workout.repositories import WorkoutRepository
from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_workouts: int
    total_sets: int
    total_volume_kg: float
    workouts_last_7_days: int


class StatsService:
    def __init__(
        self,
        progress_repo: ProgressRepository,
        workout_repo: WorkoutRepository,
    ) -> None:
        self._progress_repo = progress_repo
        self._workout_repo = workout_repo

    async def dashboard(self, user_id: UUID) -> DashboardStats:
        summary = await self._progress_repo.get_summary(user_id)
        recent = await self._workout_repo.list_by_user(user_id, skip=0, limit=50)
        from datetime import date, timedelta

        cutoff = date.today() - timedelta(days=7)
        last_7 = sum(1 for w in recent if w.performed_at >= cutoff)
        return DashboardStats(
            total_workouts=summary.total_workouts,
            total_sets=summary.total_sets,
            total_volume_kg=summary.total_volume_kg,
            workouts_last_7_days=last_7,
        )
