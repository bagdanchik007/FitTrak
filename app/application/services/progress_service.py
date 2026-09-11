from uuid import UUID

from app.domain.progress.repositories import ProgressRepository
from app.schemas.progress import (
    PersonalRecord,
    ProgressSummary,
    VolumeEntry,
)


class ProgressService:
    def __init__(self, repo: ProgressRepository) -> None:
        self._repo = repo

    async def get_summary(self, user_id: UUID) -> ProgressSummary:
        summary = await self._repo.get_summary(user_id)
        return ProgressSummary(
            total_workouts=summary.total_workouts,
            total_sets=summary.total_sets,
            total_volume_kg=summary.total_volume_kg,
            personal_records=[
                PersonalRecord(
                    exercise_id=pr.exercise_id,
                    exercise_name=pr.exercise_name,
                    max_weight_kg=pr.max_weight_kg,
                    max_reps=pr.max_reps,
                    estimated_1rm=pr.estimated_1rm,
                    achieved_at=pr.achieved_at,
                )
                for pr in summary.personal_records
            ],
            volume_last_30_days=[
                VolumeEntry(
                    date=v.date,
                    total_volume_kg=v.total_volume_kg,
                    total_sets=v.total_sets,
                    total_reps=v.total_reps,
                )
                for v in summary.volume_last_30_days
            ],
        )

# Maps domain ProgressSummary into API response schemas
