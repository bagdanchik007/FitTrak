from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.workout.entities import Workout, WorkoutSet
from app.domain.workout.repositories import WorkoutRepository
from app.infrastructure.database.models.workout import WorkoutModel, WorkoutSetModel


class SQLAlchemyWorkoutRepository(WorkoutRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_entity(self, model: WorkoutModel) -> Workout:
        sets = [
            WorkoutSet(
                id=s.id,
                workout_id=s.workout_id,
                exercise_id=s.exercise_id,
                set_number=s.set_number,
                reps=s.reps,
                weight_kg=s.weight_kg,
                rpe=s.rpe,
                notes=s.notes,
            )
            for s in (model.sets or [])
        ]
        return Workout(
            id=model.id,
            user_id=model.user_id,
            title=model.title,
            notes=model.notes,
            performed_at=model.performed_at,
            duration_minutes=model.duration_minutes,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            sets=sets,
        )

    async def get_by_id(self, workout_id: UUID, user_id: UUID) -> Workout | None:
        stmt = (
            select(WorkoutModel)
            .options(selectinload(WorkoutModel.sets))
            .where(
                WorkoutModel.id == workout_id,
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
            )
        )
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def list_by_user(
        self,
        user_id: UUID,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Workout]:
        stmt = (
            select(WorkoutModel)
            .options(selectinload(WorkoutModel.sets))
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
            )
            .order_by(WorkoutModel.performed_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars().all()]

    async def create(self, workout: Workout) -> Workout:
        model = WorkoutModel(
            id=workout.id,
            user_id=workout.user_id,
            title=workout.title,
            notes=workout.notes,
            performed_at=workout.performed_at,
            duration_minutes=workout.duration_minutes,
        )
        self._session.add(model)
        await self._session.flush()

        for s in workout.sets:
            set_model = WorkoutSetModel(
                id=s.id or uuid4(),
                workout_id=model.id,
                exercise_id=s.exercise_id,
                set_number=s.set_number,
                reps=s.reps,
                weight_kg=s.weight_kg,
                rpe=s.rpe,
                notes=s.notes,
            )
            self._session.add(set_model)

        await self._session.flush()
        return await self.get_by_id(model.id, workout.user_id)  # type: ignore

    async def soft_delete(self, workout_id: UUID, user_id: UUID) -> bool:
        stmt = select(WorkoutModel).where(
            WorkoutModel.id == workout_id,
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
        )
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        if not model:
            return False
        model.deleted_at = datetime.now(timezone.utc)
        await self._session.flush()
        return True
