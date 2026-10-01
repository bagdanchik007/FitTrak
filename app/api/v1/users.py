from sqlalchemy import func, select
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_user_service
from app.application.services.user_service import UserService
from app.core.messages import USER_NOT_FOUND
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
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

    stmt = select(func.count()).select_from(WorkoutModel).where(
        WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None)
    )
    total = (await db.execute(stmt)).scalar_one()
    return {"user_id": str(user_id), "total_workouts": int(total)}

