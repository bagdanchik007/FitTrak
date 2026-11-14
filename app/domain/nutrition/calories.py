"""Estimate calories burned from MET, body weight, and duration."""

from app.domain.nutrition.mets import met_for


def calories_burned(
    *,
    weight_kg: float,
    duration_minutes: float,
    activity: str | None = "general",
    met: float | None = None,
) -> float:
    if weight_kg <= 0 or duration_minutes <= 0:
        return 0.0
    m = met if met is not None else met_for(activity)
    hours = duration_minutes / 60.0
    # Standard estimate: kcal ≈ MET × weight_kg × hours
    return round(m * weight_kg * hours, 1)
