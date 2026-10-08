from uuid import uuid4

from fastapi import APIRouter
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.domain.preference.services import clamp_weekly_goal, normalize_weight_unit
from app.infrastructure.database.models.preference import UserPreferenceModel
from app.schemas.preference import PreferenceRead, PreferenceUpdate

ALLOWED_LANGUAGES = frozenset({"en", "de", "uk", "pl"})

router = APIRouter(prefix="/preferences", tags=["Preferences"])


async def _get_or_create(db: DbSession, user_id) -> UserPreferenceModel:
    stmt = select(UserPreferenceModel).where(UserPreferenceModel.user_id == user_id)
    pref = (await db.execute(stmt)).scalar_one_or_none()
    if pref:
        return pref
    pref = UserPreferenceModel(id=uuid4(), user_id=user_id)
    db.add(pref)
    await db.flush()
    await db.refresh(pref)
    return pref


@router.get("/me", response_model=PreferenceRead)
async def get_preferences(user_id: CurrentUserId, db: DbSession) -> PreferenceRead:
    pref = await _get_or_create(db, user_id)
    return PreferenceRead.model_validate(pref)


@router.put("/me", response_model=PreferenceRead)
async def update_preferences(
    data: PreferenceUpdate, user_id: CurrentUserId, db: DbSession
) -> PreferenceRead:
    pref = await _get_or_create(db, user_id)
    payload = data.model_dump(exclude_unset=True)
    if "weight_unit" in payload:
        payload["weight_unit"] = normalize_weight_unit(payload["weight_unit"])
    if "weekly_goal_workouts" in payload and payload["weekly_goal_workouts"] is not None:
        payload["weekly_goal_workouts"] = clamp_weekly_goal(payload["weekly_goal_workouts"])
    if "language" in payload and payload["language"]:
        lang = str(payload["language"]).lower()[:2]
        payload["language"] = lang if lang in ALLOWED_LANGUAGES else "en"
    for k, v in payload.items():
        setattr(pref, k, v)
    await db.flush()
    await db.refresh(pref)
    return PreferenceRead.model_validate(pref)


@router.post("/me/reset", response_model=PreferenceRead)
async def reset_preferences(user_id: CurrentUserId, db: DbSession) -> PreferenceRead:
    pref = await _get_or_create(db, user_id)
    pref.weight_unit = "kg"
    pref.language = "en"
    pref.weekly_goal_workouts = 3
    pref.email_reminders = False
    await db.flush()
    await db.refresh(pref)
    return PreferenceRead.model_validate(pref)


@router.get("/me/effective")
async def effective_preferences(user_id: CurrentUserId, db: DbSession) -> dict:
    pref = await _get_or_create(user_id, db)
    return {
        "weekly_goal_workouts": pref.weekly_goal_workouts or 3,
        "weight_unit": pref.weight_unit or "kg",
        "language": pref.language or "en",
    }

