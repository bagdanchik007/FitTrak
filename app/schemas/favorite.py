from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class FavoriteCreate(BaseModel):
    exercise_id: UUID


class FavoriteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    exercise_id: UUID
    created_at: datetime
