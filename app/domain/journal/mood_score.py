"""Map mood strings to a simple numeric score."""

SCORES = {
    "great": 5,
    "good": 4,
    "ok": 3,
    "okay": 3,
    "low": 2,
    "bad": 1,
    "terrible": 1,
}

def mood_score(mood: str | None) -> int | None:
    if not mood:
        return None
    return SCORES.get(mood.strip().lower())
