from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID


@dataclass(slots=True)
class Goal:
    id: UUID
    user_id: UUID
    title: str
    description: str | None
    target_value: float | None
    current_value: float | None
    unit: str | None
    deadline: date | None
    is_completed: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None

    @property
    def progress_ratio(self) -> float | None:
        if self.target_value is None or self.target_value == 0 or self.current_value is None:
            return None
        return min(1.0, max(0.0, self.current_value / self.target_value))
