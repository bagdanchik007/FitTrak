from app.core.enums import WeightUnit
from app.domain.preference.services import clamp_weekly_goal, normalize_weight_unit


def test_normalize_weight_unit():
    assert normalize_weight_unit("LBS") == WeightUnit.LBS
    assert normalize_weight_unit("invalid") == WeightUnit.KG


def test_clamp_weekly_goal():
    assert clamp_weekly_goal(0) == 1
    assert clamp_weekly_goal(20) == 14
    assert clamp_weekly_goal(4) == 4
