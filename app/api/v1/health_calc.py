"""Calorie and step calculators (rule-based portfolio helpers)."""

from fastapi import APIRouter, Query

from app.application.services.calorie_service import estimate_session_calories
from app.application.services.steps_service import steps_summary
from app.domain.exercise.calorie_hint import activity_key_from_exercise
from app.domain.nutrition.mets import MET_BY_ACTIVITY

router = APIRouter(prefix="/health-calc", tags=["Health calculators"])


@router.get("/calories")
async def calc_calories(
    weight_kg: float = Query(..., gt=0, le=400),
    duration_minutes: float = Query(..., gt=0, le=600),
    activity: str = Query("general"),
) -> dict:
    return estimate_session_calories(
        weight_kg=weight_kg,
        duration_minutes=duration_minutes,
        activity=activity,
    )


@router.get("/steps")
async def calc_steps(
    steps: int | None = Query(None, ge=0, le=200_000),
    distance_km: float | None = Query(None, ge=0, le=200),
    height_cm: float = Query(170, gt=50, le=250),
    weight_kg: float = Query(70, gt=0, le=400),
) -> dict:
    return steps_summary(
        steps=steps,
        distance_km=distance_km,
        height_cm=height_cm,
        weight_kg=weight_kg,
    )


@router.get("/activities")
async def list_activities() -> dict:
    return {"activities": sorted(MET_BY_ACTIVITY.keys()), "mets": MET_BY_ACTIVITY}


@router.get("/exercise-activity")
async def exercise_activity_hint(name: str = "", muscle_group: str = "") -> dict:
    key = activity_key_from_exercise(name=name or None, muscle_group=muscle_group or None)
    return {"activity": key, "name": name, "muscle_group": muscle_group}
