from app.domain.steps.estimate import (
    calories_from_steps,
    distance_km_from_steps,
    steps_from_distance_km,
)


def steps_summary(
    *,
    steps: int | None = None,
    distance_km: float | None = None,
    height_cm: float = 170.0,
    weight_kg: float = 70.0,
) -> dict:
    if steps is None and distance_km is not None:
        steps = steps_from_distance_km(distance_km=distance_km, height_cm=height_cm)
    steps = int(steps or 0)
    dist = distance_km_from_steps(steps=steps, height_cm=height_cm)
    kcal = calories_from_steps(steps=steps, weight_kg=weight_kg)
    return {
        "steps": steps,
        "distance_km": dist,
        "kcal_estimate": kcal,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
    }
