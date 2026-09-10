from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.core.exceptions import NotFoundError
from app.domain.exercise.entities import Exercise
from app.domain.exercise.repositories import ExerciseRepository
from app.schemas.exercise import ExerciseCreate, ExerciseRead, ExerciseUpdate


class ExerciseService:
    def __init__(self, repo: ExerciseRepository) -> None:
        self._repo = repo

    async def create(self, data: ExerciseCreate, user_id: UUID) -> ExerciseRead:
        exercise = Exercise(
            id=uuid4(),
            name=data.name,
            description=data.description,
            muscle_group=data.muscle_group,
            equipment=data.equipment,
            created_by=user_id,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        created = await self._repo.create(exercise)
        return ExerciseRead.model_validate(created)

    async def get(self, exercise_id: UUID) -> ExerciseRead:
        exercise = await self._repo.get_by_id(exercise_id)
        if not exercise:
            raise NotFoundError("Exercise")
        return ExerciseRead.model_validate(exercise)

    async def list(
        self,
        skip: int = 0,
        limit: int = 50,
        muscle_group: str | None = None,
    ) -> list[ExerciseRead]:
        exercises = await self._repo.list(skip=skip, limit=limit, muscle_group=muscle_group)
        return [ExerciseRead.model_validate(e) for e in exercises]

    async def update(self, exercise_id: UUID, data: ExerciseUpdate) -> ExerciseRead:
        exercise = await self._repo.get_by_id(exercise_id)
        if not exercise:
            raise NotFoundError("Exercise")

        if data.name is not None:
            exercise.name = data.name
        if data.description is not None:
            exercise.description = data.description
        if data.muscle_group is not None:
            exercise.muscle_group = data.muscle_group
        if data.equipment is not None:
            exercise.equipment = data.equipment

        updated = await self._repo.update(exercise)
        return ExerciseRead.model_validate(updated)

    async def delete(self, exercise_id: UUID) -> None:
        deleted = await self._repo.soft_delete(exercise_id)
        if not deleted:
            raise NotFoundError("Exercise")
