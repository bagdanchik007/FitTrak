from uuid import UUID

from pydantic import BaseModel, Field


class CreateJournalDTO(BaseModel):
    user_id: UUID
    title: str = Field(..., min_length=1, max_length=150)
    body: str = Field(..., min_length=1)
    mood: str | None = None
