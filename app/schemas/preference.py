from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class PreferenceUpdate(BaseModel):
    weight_unit: str | None = Field(None, pattern="^(kg|lbs)$")
    language: str | None = Field(None, min_length=2, max_length=10)
    weekly_goal_workouts: int | None = Field(None, ge=1, le=14)
    email_reminders: bool | None = None


class PreferenceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    weight_unit: str
    language: str
    weekly_goal_workouts: int
    email_reminders: bool
    updated_at: datetime
