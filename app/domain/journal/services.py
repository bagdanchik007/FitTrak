"""Journal pure helpers."""

ALLOWED_MOODS = frozenset(
    {"great", "good", "ok", "low", "bad", "tired", "energized", "sore"}
)


def normalize_mood(mood: str | None) -> str | None:
    if mood is None:
        return None
    value = mood.strip().lower()
    return value or None


def is_allowed_mood(mood: str) -> bool:
    return mood in ALLOWED_MOODS


def word_count(text: str | None) -> int:
    if not text:
        return 0
    return len([w for w in text.split() if w.strip()])


def mood_polarity(mood: str | None) -> str:
    if not mood:
        return "neutral"
    positive = {"great", "good", "energized"}
    negative = {"bad", "low", "tired", "sore"}
    m = mood.lower()
    if m in positive:
        return "positive"
    if m in negative:
        return "negative"
    return "neutral"
