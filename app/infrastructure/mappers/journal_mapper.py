from app.domain.journal.entities import JournalEntry
from app.infrastructure.database.models.journal import JournalEntryModel


def model_to_journal(model: JournalEntryModel) -> JournalEntry:
    return JournalEntry(
        id=model.id,
        user_id=model.user_id,
        title=model.title,
        body=model.body,
        mood=model.mood,
        created_at=model.created_at,
        updated_at=model.updated_at,
        deleted_at=model.deleted_at,
    )
