from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class ExerciseFavorite:
    id: UUID
    user_id: UUID
    exercise_id: UUID
    created_at: datetime
