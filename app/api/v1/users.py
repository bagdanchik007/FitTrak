from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.core.security import get_password_hash
from app.schemas.user import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get current authenticated user",
)
async def get_me(
    user_id: CurrentUserId,
    db: DbSession,
) -> UserRead:
    repo = SQLAlchemyUserRepository(db)
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return UserRead.model_validate(user)


@router.patch(
    "/me",
    response_model=UserRead,
    summary="Update current user profile",
)
async def update_me(
    data: UserUpdate,
    user_id: CurrentUserId,
    db: DbSession,
) -> UserRead:
    repo = SQLAlchemyUserRepository(db)
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if data.full_name is not None:
        user.full_name = data.full_name
    if data.password is not None:
        user.hashed_password = get_password_hash(data.password)
    updated = await repo.update(user)
    return UserRead.model_validate(updated)


@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Get public user profile by id",
)
async def get_public_profile(
    user_id: UUID,
    db: DbSession,
) -> UserRead:
    """Returns limited profile data (email hidden for privacy in production would use a PublicUser schema)."""
    repo = SQLAlchemyUserRepository(db)
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserRead.model_validate(user)

