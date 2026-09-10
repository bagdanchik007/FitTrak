from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.progress.entities import ProgressSummary


class ProgressRepository(ABC):
    @abstractmethod
    async def get_summary(self, user_id: UUID) -> ProgressSummary:
        ...
