"""Journal application helpers."""

from app.domain.journal.services import is_allowed_mood, normalize_mood


def prepare_mood(mood: str | None) -> str | None:
    normalized = normalize_mood(mood)
    if normalized and not is_allowed_mood(normalized):
        return normalized  # still store free-text; validation optional at API layer
    return normalized
