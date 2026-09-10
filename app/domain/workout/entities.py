from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import UUID


@dataclass(slots=True)
class WorkoutSet:
    id: UUID
    workout_id: UUID
    exercise_id: UUID
    set_number: int
    reps: int | None = None
    weight_kg: float | None = None
    rpe: float | None = None
    notes: str | None = None


@dataclass(slots=True)
class Workout:
    id: UUID
    user_id: UUID
    title: str
    performed_at: date
    notes: str | None = None
    duration_minutes: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    sets: list[WorkoutSet] = field(default_factory=list)
