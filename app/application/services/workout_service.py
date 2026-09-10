from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.core.exceptions import NotFoundError
from app.domain.workout.entities import Workout, WorkoutSet
from app.domain.workout.repositories import WorkoutRepository
from app.schemas.workout import WorkoutCreate, WorkoutRead


class WorkoutService:
    def __init__(self, repo: WorkoutRepository) -> None:
        self._repo = repo

    async def create(self, data: WorkoutCreate, user_id: UUID) -> WorkoutRead:
        sets = [
            WorkoutSet(
                id=uuid4(),
                workout_id=uuid4(),  # will be overwritten
                exercise_id=s.exercise_id,
                set_number=s.set_number,
                reps=s.reps,
                weight_kg=s.weight_kg,
                rpe=s.rpe,
                notes=s.notes,
            )
            for s in data.sets
        ]
        workout = Workout(
            id=uuid4(),
            user_id=user_id,
            title=data.title,
            notes=data.notes,
            performed_at=data.performed_at,
            duration_minutes=data.duration_minutes,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            sets=sets,
        )
        created = await self._repo.create(workout)
        return WorkoutRead.model_validate(created)

    async def get(self, workout_id: UUID, user_id: UUID) -> WorkoutRead:
        workout = await self._repo.get_by_id(workout_id, user_id)
        if not workout:
            raise NotFoundError("Workout")
        return WorkoutRead.model_validate(workout)

    async def list(self, user_id: UUID, skip: int = 0, limit: int = 20) -> list[WorkoutRead]:
        workouts = await self._repo.list_by_user(user_id, skip=skip, limit=limit)
        return [WorkoutRead.model_validate(w) for w in workouts]

    async def delete(self, workout_id: UUID, user_id: UUID) -> None:
        deleted = await self._repo.soft_delete(workout_id, user_id)
        if not deleted:
            raise NotFoundError("Workout")
