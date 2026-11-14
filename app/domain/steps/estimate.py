"""Step and distance helpers (rule-based estimates)."""

# Average stride length factor relative to height (very approximate)
STRIDE_FACTOR = 0.415


def steps_from_distance_km(*, distance_km: float, height_cm: float = 170.0) -> int:
    if distance_km <= 0 or height_cm <= 0:
        return 0
    stride_m = (height_cm / 100.0) * STRIDE_FACTOR
    if stride_m <= 0:
        return 0
    return int(round((distance_km * 1000.0) / stride_m))


def distance_km_from_steps(*, steps: int, height_cm: float = 170.0) -> float:
    if steps <= 0 or height_cm <= 0:
        return 0.0
    stride_m = (height_cm / 100.0) * STRIDE_FACTOR
    return round((steps * stride_m) / 1000.0, 3)


def calories_from_steps(*, steps: int, weight_kg: float) -> float:
    """Rough ~0.04 kcal per step scaled lightly by body weight vs 70 kg."""
    if steps <= 0 or weight_kg <= 0:
        return 0.0
    scale = weight_kg / 70.0
    return round(steps * 0.04 * scale, 1)
