"""Workout suggestion heuristics (no network)."""

from __future__ import annotations

FOCUS_ROTATION = ("push", "pull", "legs", "upper", "full_body")

TEMPLATES: dict[str, list[str]] = {
    "push": ["Bench Press", "Overhead Press", "Incline DB Press", "Triceps Pushdown", "Lateral Raise"],
    "pull": ["Barbell Row", "Pull-Up", "Lat Pulldown", "Face Pull", "Barbell Curl"],
    "legs": ["Back Squat", "Romanian Deadlift", "Leg Press", "Walking Lunge", "Calf Raise"],
    "upper": ["Bench Press", "Barbell Row", "Overhead Press", "Pull-Up", "Lateral Raise"],
    "full_body": ["Squat", "Bench Press", "Barbell Row", "Romanian Deadlift", "Plank"],
}


def suggest_focus(*, recent_focuses: list[str] | None = None) -> str:
    recent = [f.lower().strip() for f in (recent_focuses or []) if f]
    for focus in FOCUS_ROTATION:
        if focus not in recent[-3:]:
            return focus
    return FOCUS_ROTATION[len(recent) % len(FOCUS_ROTATION)]


def suggest_session(*, focus: str, experience: str = "intermediate") -> dict:
    key = focus.lower().strip() if focus else "full_body"
    if key not in TEMPLATES:
        key = "full_body"
    exercises = list(TEMPLATES[key])
    sets = 3 if experience != "beginner" else 2
    reps = "8-12" if experience != "advanced" else "5-8"
    return {
        "focus": key,
        "experience": experience,
        "exercises": [
            {"name": name, "sets": sets, "reps": reps, "rest_seconds": 90 if key == "legs" else 75}
            for name in exercises
        ],
        "notes": f"Rule-based {key} session. Adjust loads to leave 1–2 reps in reserve.",
        "engine": "rules",
    }


def coach_reply(message: str) -> str:
    text = (message or "").lower()
    if any(w in text for w in ("sore", "pain", "verletz", "schmerz")):
        return (
            "If you feel sharp pain, stop and consider professional advice. "
            "Mild soreness is common—prefer light movement and sleep. This is not medical advice."
        )
    if any(w in text for w in ("bulk", "masse", "gain")):
        return "For muscle gain: progressive overload, protein ~1.6–2.2 g/kg, and a small calorie surplus help most people."
    if any(w in text for w in ("cut", "abnehmen", "fat")):
        return "For fat loss: a moderate calorie deficit, keep protein high, and maintain 2–4 strength sessions per week."
    if any(w in text for w in ("beginner", "anfänger", "start")):
        return "Start with full-body 3x/week, learn squat/hinge/push/pull patterns, and add weight slowly."
    return (
        "Focus on consistency: 3–5 sessions weekly, log your lifts, and progress one variable at a time "
        "(load, reps, or sets). Ask about push, pull, legs, recovery, or goals for a tighter tip."
    )


KEYWORDS = {
    "push": ("push", "bench", "press", "chest", "triceps", "shoulder"),
    "pull": ("pull", "row", "lat", "back", "curl", "deadlift"),
    "legs": ("leg", "squat", "lunge", "quad", "hamstring", "calf", "glute"),
    "upper": ("upper",),
    "full_body": ("full", "fullbody", "full-body", "fbw"),
}


def infer_focus_from_title(title: str) -> str | None:
    low = (title or "").lower()
    for focus, words in KEYWORDS.items():
        if any(w in low for w in words):
            return focus
    return None


def infer_focuses_from_titles(titles: list[str], *, limit: int = 5) -> list[str]:
    found: list[str] = []
    for title in titles[:20]:
        focus = infer_focus_from_title(title)
        if focus:
            found.append(focus)
        if len(found) >= limit:
            break
    return found
