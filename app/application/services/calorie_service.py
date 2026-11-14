from app.domain.nutrition.calories import calories_burned
from app.domain.nutrition.mets import met_for


def estimate_session_calories(
    *,
    weight_kg: float,
    duration_minutes: float,
    activity: str | None = "general",
) -> dict:
    met = met_for(activity)
    kcal = calories_burned(
        weight_kg=weight_kg,
        duration_minutes=duration_minutes,
        activity=activity,
        met=met,
    )
    return {
        "activity": activity or "general",
        "met": met,
        "weight_kg": weight_kg,
        "duration_minutes": duration_minutes,
        "kcal": kcal,
    }
