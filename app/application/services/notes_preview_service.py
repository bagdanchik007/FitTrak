from app.domain.workout.notes import truncate_notes

def notes_preview(notes: str | None) -> dict:
    return {"preview": truncate_notes(notes), "full_length": len(notes or "")}
