from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class UserPreference:
    id: UUID
    user_id: UUID
    weight_unit: str
    language: str
    weekly_goal_workouts: int
    email_reminders: bool
    created_at: datetime
    updated_at: datetime
