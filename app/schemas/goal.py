from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class GoalBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    target_value: float | None = None
    current_value: float | None = None
    unit: str | None = Field(None, max_length=40)
    deadline: date | None = None


class GoalCreate(GoalBase):
    pass


class GoalUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=150)
    description: str | None = None
    target_value: float | None = None
    current_value: float | None = None
    unit: str | None = None
    deadline: date | None = None
    is_completed: bool | None = None


class GoalRead(GoalBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    is_completed: bool
    created_at: datetime
