"""Refresh token persistence and rotation."""

import hashlib
from datetime import UTC, datetime, timedelta
from uuid import UUID, uuid4

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.infrastructure.database.models.refresh_token import RefreshTokenModel


def hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


async def store_refresh_token(
    db: AsyncSession, user_id: UUID, raw_token: str, days: int | None = None
) -> RefreshTokenModel:
    settings = get_settings()
    lifetime = days if days is not None else settings.refresh_token_expire_days
    row = RefreshTokenModel(
        id=uuid4(),
        user_id=user_id,
        token_hash=hash_token(raw_token),
        expires_at=datetime.now(UTC) + timedelta(days=lifetime),
    )
    db.add(row)
    await db.flush()
    return row


async def rotate_refresh_token(
    db: AsyncSession, raw_token: str, new_raw_token: str
) -> UUID | None:
    """Revoke old token, store new one; return user_id if valid."""
    settings = get_settings()
    th = hash_token(raw_token)
    stmt = select(RefreshTokenModel).where(RefreshTokenModel.token_hash == th)
    row = (await db.execute(stmt)).scalar_one_or_none()
    if row is None or row.revoked_at is not None:
        return None
    if row.expires_at < datetime.now(UTC):
        return None
    row.revoked_at = datetime.now(UTC)
    row.replaced_by = hash_token(new_raw_token)
    new_row = RefreshTokenModel(
        id=uuid4(),
        user_id=row.user_id,
        token_hash=hash_token(new_raw_token),
        expires_at=datetime.now(UTC) + timedelta(days=settings.refresh_token_expire_days),
    )
    db.add(new_row)
    await db.flush()
    return row.user_id


async def revoke_all_for_user(db: AsyncSession, user_id: UUID) -> int:
    stmt = select(RefreshTokenModel).where(
        RefreshTokenModel.user_id == user_id,
        RefreshTokenModel.revoked_at.is_(None),
    )
    rows = (await db.execute(stmt)).scalars().all()
    now = datetime.now(UTC)
    for r in rows:
        r.revoked_at = now
    await db.flush()
    return len(rows)
