"""Preference application helpers."""

from app.domain.preference.entities import UserPreference
from app.domain.preference.services import clamp_weekly_goal, normalize_weight_unit


def apply_preference_defaults(pref: UserPreference) -> UserPreference:
    pref.weight_unit = normalize_weight_unit(pref.weight_unit)
    pref.weekly_goal_workouts = clamp_weekly_goal(pref.weekly_goal_workouts)
    return pref
