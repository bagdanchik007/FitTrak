from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class JournalCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    body: str = Field(..., min_length=1)
    mood: str | None = Field(None, max_length=40)


class JournalUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=150)
    body: str | None = Field(None, min_length=1)
    mood: str | None = Field(None, max_length=40)


class JournalRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    title: str
    body: str
    mood: str | None
    created_at: datetime
