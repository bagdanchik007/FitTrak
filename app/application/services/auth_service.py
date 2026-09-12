from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException, status

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_password_hash,
    verify_password,
)
from app.domain.user.entities import User
from app.domain.user.repositories import UserRepository
from app.schemas.user import Token, UserCreate, UserRead


class AuthService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def register(self, data: UserCreate) -> UserRead:
        existing = await self._user_repo.get_by_email(data.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email already exists",
            )

        user = User(
            id=uuid4(),
            email=data.email.lower(),
            hashed_password=get_password_hash(data.password),
            full_name=data.full_name,
            is_active=True,
            is_superuser=False,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        created = await self._user_repo.create(user)
        return UserRead.model_validate(created)

    async def login(self, email: str, password: str) -> Token:
        user = await self._user_repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Inactive user",
            )

        # Update last login
        user.last_login_at = datetime.now(timezone.utc)
        await self._user_repo.update(user)

        return Token(
            access_token=create_access_token(subject=str(user.id)),
            refresh_token=create_refresh_token(subject=str(user.id)),
        )

# Passwords are hashed with bcrypt via passlib before persistence

    async def refresh(self, refresh_token: str) -> Token:
        payload = decode_token(refresh_token)
        if payload is None or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )
        user = await self._user_repo.get_by_id(__import__("uuid").UUID(user_id))
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found or inactive",
            )
        return Token(
            access_token=create_access_token(subject=str(user.id)),
            refresh_token=create_refresh_token(subject=str(user.id)),
        )

    async def change_password(self, user_id, current_password: str, new_password: str) -> None:
        user = await self._user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if not verify_password(current_password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is incorrect",
            )
        user.hashed_password = get_password_hash(new_password)
        await self._user_repo.update(user)

