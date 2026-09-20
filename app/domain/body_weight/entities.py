from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID


@dataclass(slots=True)
class BodyWeightEntry:
    id: UUID
    user_id: UUID
    recorded_at: date
    weight_kg: float
    note: str | None
    created_at: datetime
