"""Filter workouts by title query."""

from app.domain.search.normalize import normalize_query

def title_matches(title: str, query: str | None) -> bool:
    q = normalize_query(query)
    if not q:
        return True
    return q in (title or "").lower()
