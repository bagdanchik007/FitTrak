from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class TemplateItem:
    id: UUID
    template_id: UUID
    exercise_id: UUID
    target_sets: int
    target_reps: int | None
    sort_order: int


@dataclass(slots=True)
class WorkoutTemplate:
    id: UUID
    user_id: UUID
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime
    items: list[TemplateItem] = field(default_factory=list)
    deleted_at: datetime | None = None
