"""Preference domain helpers."""

from app.core.enums import WeightUnit


def normalize_weight_unit(unit: str | None) -> str:
    if unit is None:
        return WeightUnit.KG
    value = unit.strip().lower()
    if value in {WeightUnit.KG, WeightUnit.LBS}:
        return value
    return WeightUnit.KG


def clamp_weekly_goal(value: int) -> int:
    return max(1, min(14, value))
