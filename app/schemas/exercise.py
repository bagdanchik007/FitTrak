from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ExerciseBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: str | None = None
    muscle_group: str | None = Field(None, max_length=80)
    equipment: str | None = Field(None, max_length=80)


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=120)
    description: str | None = None
    muscle_group: str | None = Field(None, max_length=80)
    equipment: str | None = Field(None, max_length=80)


class ExerciseRead(ExerciseBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_by: UUID | None = None
    created_at: datetime
