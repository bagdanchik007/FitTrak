from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exercise.entities import Exercise
from app.domain.exercise.repositories import ExerciseRepository
from app.infrastructure.database.models.exercise import ExerciseModel


class SQLAlchemyExerciseRepository(ExerciseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_entity(self, model: ExerciseModel) -> Exercise:
        return Exercise(
            id=model.id,
            name=model.name,
            description=model.description,
            muscle_group=model.muscle_group,
            equipment=model.equipment,
            created_by=model.created_by,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )

    async def get_by_id(self, exercise_id: UUID) -> Exercise | None:
        stmt = select(ExerciseModel).where(
            ExerciseModel.id == exercise_id,
            ExerciseModel.deleted_at.is_(None),
        )
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def list(
        self,
        skip: int = 0,
        limit: int = 50,
        muscle_group: str | None = None,
    ) -> list[Exercise]:
        stmt = select(ExerciseModel).where(ExerciseModel.deleted_at.is_(None))
        if muscle_group:
            stmt = stmt.where(ExerciseModel.muscle_group == muscle_group)
        stmt = stmt.order_by(ExerciseModel.name).offset(skip).limit(limit)
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars().all()]

    async def create(self, exercise: Exercise) -> Exercise:
        model = ExerciseModel(
            id=exercise.id,
            name=exercise.name,
            description=exercise.description,
            muscle_group=exercise.muscle_group,
            equipment=exercise.equipment,
            created_by=exercise.created_by,
        )
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)

    async def update(self, exercise: Exercise) -> Exercise:
        stmt = select(ExerciseModel).where(ExerciseModel.id == exercise.id)
        result = await self._session.execute(stmt)
        model = result.scalar_one()
        model.name = exercise.name
        model.description = exercise.description
        model.muscle_group = exercise.muscle_group
        model.equipment = exercise.equipment
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)

    async def soft_delete(self, exercise_id: UUID) -> bool:
        stmt = select(ExerciseModel).where(
            ExerciseModel.id == exercise_id,
            ExerciseModel.deleted_at.is_(None),
        )
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        if not model:
            return False
        model.deleted_at = datetime.now(timezone.utc)
        await self._session.flush()
        return True
