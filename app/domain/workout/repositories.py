from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.workout.entities import Workout


class WorkoutRepository(ABC):
    @abstractmethod
    async def get_by_id(self, workout_id: UUID, user_id: UUID) -> Workout | None: ...

    @abstractmethod
    async def list_by_user(
        self,
        user_id: UUID,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Workout]: ...

    @abstractmethod
    async def create(self, workout: Workout) -> Workout: ...

    @abstractmethod
    async def soft_delete(self, workout_id: UUID, user_id: UUID) -> bool: ...

    @abstractmethod
    async def get_owned(self, workout_id: UUID, user_id: UUID) -> Workout | None:
        """Return workout only if it belongs to user and is not soft-deleted."""
        ...
