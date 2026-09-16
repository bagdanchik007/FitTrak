from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.exercise.entities import Exercise


class ExerciseRepository(ABC):
    @abstractmethod
    async def get_by_id(self, exercise_id: UUID) -> Exercise | None:
        ...

    @abstractmethod
    async def list(
        self,
        skip: int = 0,
        limit: int = 50,
        muscle_group: str | None = None,
    ) -> list[Exercise]:
        ...

    @abstractmethod
    async def create(self, exercise: Exercise) -> Exercise:
        ...

    @abstractmethod
    async def update(self, exercise: Exercise) -> Exercise:
        ...

    @abstractmethod
    async def soft_delete(self, exercise_id: UUID) -> bool:
        ...

# Interface only – concrete class lives in infrastructure
