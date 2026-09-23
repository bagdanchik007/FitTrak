from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class JournalEntry:
    id: UUID
    user_id: UUID
    title: str
    body: str
    mood: str | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
