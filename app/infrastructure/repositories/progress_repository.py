from datetime import date, timedelta
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.progress.entities import PersonalRecord, ProgressSummary, VolumeEntry
from app.domain.progress.repositories import ProgressRepository
from app.infrastructure.database.models.exercise import ExerciseModel
from app.infrastructure.database.models.workout import WorkoutModel, WorkoutSetModel


class SQLAlchemyProgressRepository(ProgressRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_summary(self, user_id: UUID) -> ProgressSummary:
        # Total workouts
        workout_count_stmt = select(func.count(WorkoutModel.id)).where(
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
        )
        total_workouts = (await self._session.execute(workout_count_stmt)).scalar() or 0

        # Total sets + volume
        volume_stmt = (
            select(
                func.count(WorkoutSetModel.id),
                func.coalesce(
                    func.sum(
                        func.coalesce(WorkoutSetModel.weight_kg, 0)
                        * func.coalesce(WorkoutSetModel.reps, 0)
                    ),
                    0,
                ),
            )
            .join(WorkoutModel, WorkoutSetModel.workout_id == WorkoutModel.id)
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
            )
        )
        result = await self._session.execute(volume_stmt)
        total_sets, total_volume = result.one()
        total_sets = total_sets or 0
        total_volume = float(total_volume or 0)

        # Personal records (max weight per exercise)
        pr_stmt = (
            select(
                ExerciseModel.id,
                ExerciseModel.name,
                func.max(WorkoutSetModel.weight_kg),
                func.max(WorkoutSetModel.reps),
            )
            .join(WorkoutSetModel, WorkoutSetModel.exercise_id == ExerciseModel.id)
            .join(WorkoutModel, WorkoutSetModel.workout_id == WorkoutModel.id)
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
            )
            .group_by(ExerciseModel.id, ExerciseModel.name)
        )
        pr_result = await self._session.execute(pr_stmt)
        personal_records = []
        for row in pr_result.all():
            exercise_id, name, max_w, max_r = row
            estimated_1rm = None
            if max_w and max_r and max_r > 0:
                # Epley formula approximation
                estimated_1rm = round(max_w * (1 + max_r / 30), 1)
            personal_records.append(
                PersonalRecord(
                    exercise_id=exercise_id,
                    exercise_name=name,
                    max_weight_kg=float(max_w) if max_w else None,
                    max_reps=int(max_r) if max_r else None,
                    estimated_1rm=estimated_1rm,
                    achieved_at=None,
                )
            )

        # Volume last 30 days
        thirty_days_ago = date.today() - timedelta(days=30)
        daily_stmt = (
            select(
                WorkoutModel.performed_at,
                func.coalesce(
                    func.sum(
                        func.coalesce(WorkoutSetModel.weight_kg, 0)
                        * func.coalesce(WorkoutSetModel.reps, 0)
                    ),
                    0,
                ),
                func.count(WorkoutSetModel.id),
                func.coalesce(func.sum(WorkoutSetModel.reps), 0),
            )
            .join(WorkoutSetModel, WorkoutSetModel.workout_id == WorkoutModel.id)
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
                WorkoutModel.performed_at >= thirty_days_ago,
            )
            .group_by(WorkoutModel.performed_at)
            .order_by(WorkoutModel.performed_at)
        )
        daily_result = await self._session.execute(daily_stmt)
        volume_last_30_days = [
            VolumeEntry(
                date=row[0],
                total_volume_kg=float(row[1] or 0),
                total_sets=int(row[2] or 0),
                total_reps=int(row[3] or 0),
            )
            for row in daily_result.all()
        ]

        return ProgressSummary(
            total_workouts=total_workouts,
            total_sets=total_sets,
            total_volume_kg=total_volume,
            personal_records=personal_records,
            volume_last_30_days=volume_last_30_days,
        )
