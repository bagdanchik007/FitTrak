from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BodyWeightCreate(BaseModel):
    recorded_at: date
    weight_kg: float = Field(..., gt=0, le=500)
    note: str | None = Field(None, max_length=255)


class BodyWeightRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    recorded_at: date
    weight_kg: float
    note: str | None = None
    created_at: datetime
