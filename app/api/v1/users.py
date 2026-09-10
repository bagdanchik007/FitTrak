from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.schemas.user import UserRead

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
