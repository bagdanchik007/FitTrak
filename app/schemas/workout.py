from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class WorkoutSetBase(BaseModel):
    exercise_id: UUID
    set_number: int = Field(..., ge=1)
    reps: int | None = Field(None, ge=0)
    weight_kg: float | None = Field(None, ge=0)
    rpe: float | None = Field(None, ge=1, le=10)
    notes: str | None = Field(None, max_length=255)


class WorkoutSetCreate(WorkoutSetBase):
    pass


class WorkoutSetRead(WorkoutSetBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class WorkoutBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    notes: str | None = None
    performed_at: date
    duration_minutes: int | None = Field(None, ge=0)


class WorkoutCreate(WorkoutBase):
    sets: list[WorkoutSetCreate] = Field(default_factory=list)


class WorkoutUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=150)
    notes: str | None = None
    performed_at: date | None = None
    duration_minutes: int | None = Field(None, ge=0)


class WorkoutRead(WorkoutBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    created_at: datetime
    sets: list[WorkoutSetRead] = []
