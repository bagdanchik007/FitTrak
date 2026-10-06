from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy import func, select

from app.api.deps import get_user_service
from app.application.services.user_service import UserService
from app.core.dependencies import CurrentUserId, DbSession
from app.schemas.user import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get current authenticated user",
)
async def get_me(
    user_id: CurrentUserId,
    service: UserService = Depends(get_user_service),
) -> UserRead:
    return await service.get_by_id(user_id)


@router.patch(
    "/me",
    response_model=UserRead,
    summary="Update current user profile",
)
async def update_me(
    data: UserUpdate,
    user_id: CurrentUserId,
    service: UserService = Depends(get_user_service),
) -> UserRead:
    return await service.update_profile(user_id, data)


@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Get public user profile by id",
)
async def get_public_profile(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
) -> UserRead:
    return await service.get_by_id(user_id)


@router.get("/me/activity-summary")
async def my_activity_summary(user_id: CurrentUserId, db: DbSession) -> dict:
    from app.infrastructure.database.models.workout import WorkoutModel

    stmt = (
        select(func.count())
        .select_from(WorkoutModel)
        .where(WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None))
    )
    total = (await db.execute(stmt)).scalar_one()
    from datetime import date, timedelta

    from sqlalchemy import func as sa_func

    week_ago = date.today() - timedelta(days=6)
    week_stmt = select(sa_func.count()).select_from(WorkoutModel).where(
        WorkoutModel.user_id == user_id,
        WorkoutModel.deleted_at.is_(None),
        WorkoutModel.performed_at >= week_ago,
    )
    week = int((await db.execute(week_stmt)).scalar_one())
    return {
        "user_id": str(user_id),
        "total_workouts": int(total),
        "workouts_last_7_days": week,
    }
