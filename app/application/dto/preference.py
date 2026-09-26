from uuid import UUID

from pydantic import BaseModel, Field


class UpdatePreferenceDTO(BaseModel):
    user_id: UUID
    weight_unit: str | None = None
    language: str | None = Field(None, min_length=2, max_length=10)
    weekly_goal_workouts: int | None = Field(None, ge=1, le=14)
    email_reminders: bool | None = None
