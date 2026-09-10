from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Exercise:
    id: UUID
    name: str
    description: str | None
    muscle_group: str | None
    equipment: str | None
    created_by: UUID | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
