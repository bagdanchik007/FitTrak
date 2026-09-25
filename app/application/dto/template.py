from uuid import UUID

from pydantic import BaseModel, Field


class CreateTemplateItemDTO(BaseModel):
    exercise_id: UUID
    target_sets: int = Field(3, ge=1, le=20)
    target_reps: int | None = Field(None, ge=0)
    sort_order: int = Field(0, ge=0)


class CreateTemplateDTO(BaseModel):
    user_id: UUID
    name: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    items: list[CreateTemplateItemDTO] = Field(default_factory=list)
