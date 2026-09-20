from uuid import uuid4

from fastapi import APIRouter
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.preference import UserPreferenceModel
from app.schemas.preference import PreferenceRead, PreferenceUpdate

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
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(pref, k, v)
    await db.flush()
    await db.refresh(pref)
    return PreferenceRead.model_validate(pref)
