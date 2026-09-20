from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TemplateItemCreate(BaseModel):
    exercise_id: UUID
    target_sets: int = Field(3, ge=1, le=20)
    target_reps: int | None = Field(None, ge=0)
    sort_order: int = Field(0, ge=0)


class TemplateItemRead(TemplateItemCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class TemplateCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    items: list[TemplateItemCreate] = Field(default_factory=list)


class TemplateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    name: str
    description: str | None
    created_at: datetime
    items: list[TemplateItemRead] = []
