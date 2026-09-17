"""Internal DTOs for workout use cases."""

from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class CreateWorkoutSetDTO(BaseModel):
    exercise_id: UUID
    set_number: int = Field(..., ge=1)
    reps: int | None = Field(None, ge=0)
    weight_kg: float | None = Field(None, ge=0)
    rpe: float | None = Field(None, ge=1, le=10)
    notes: str | None = None


class CreateWorkoutDTO(BaseModel):
    user_id: UUID
    title: str = Field(..., min_length=1, max_length=150)
    performed_at: date
    notes: str | None = None
    duration_minutes: int | None = Field(None, ge=0, le=600)
    sets: list[CreateWorkoutSetDTO] = Field(default_factory=list)
