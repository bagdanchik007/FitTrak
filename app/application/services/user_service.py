"""User application service."""

from uuid import UUID

from app.core.exceptions import NotFoundError
from app.core.security import get_password_hash
from app.domain.user.repositories import UserRepository
from app.schemas.user import UserRead, UserUpdate


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def get_by_id(self, user_id: UUID) -> UserRead:
        user = await self._user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User")
        return UserRead.model_validate(user)

    async def update_profile(self, user_id: UUID, data: UserUpdate) -> UserRead:
        user = await self._user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User")
        if data.full_name is not None:
            user.full_name = data.full_name
        if data.password is not None:
            user.hashed_password = get_password_hash(data.password)
        updated = await self._user_repo.update(user)
        return UserRead.model_validate(updated)
