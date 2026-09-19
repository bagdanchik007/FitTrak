from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_user_service
from app.application.services.user_service import UserService
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
