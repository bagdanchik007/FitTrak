"""Internal DTOs for exercise use cases."""

from uuid import UUID

from pydantic import BaseModel, Field


class CreateExerciseDTO(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: str | None = None
    muscle_group: str | None = None
    equipment: str | None = None
    created_by: UUID | None = None


class UpdateExerciseDTO(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=120)
    description: str | None = None
    muscle_group: str | None = None
    equipment: str | None = None
