"""Email verification token helpers (store token; send mail is out of band)."""

import secrets
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models.user import UserModel


def generate_verification_token() -> str:
    return secrets.token_urlsafe(32)


async def issue_verification_token(db: AsyncSession, user_id: UUID) -> str | None:
    stmt = select(UserModel).where(UserModel.id == user_id, UserModel.deleted_at.is_(None))
    user = (await db.execute(stmt)).scalar_one_or_none()
    if user is None:
        return None
    token = generate_verification_token()
    user.email_verification_token = token
    await db.flush()
    return token


async def verify_email_token(db: AsyncSession, token: str) -> bool:
    stmt = select(UserModel).where(
        UserModel.email_verification_token == token,
        UserModel.deleted_at.is_(None),
    )
    user = (await db.execute(stmt)).scalar_one_or_none()
    if user is None:
        return False
    user.email_verified = True
    user.email_verification_token = None
    await db.flush()
    return True
