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


ALLOWED_LANGUAGES = frozenset({"en", "de", "uk", "pl"})


def normalize_language(value: str | None) -> str:
    if not value:
        return "en"
    code = value.strip().lower()[:2]
    return code if code in ALLOWED_LANGUAGES else "en"
