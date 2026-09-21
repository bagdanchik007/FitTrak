from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.journal import JournalEntryModel
from app.schemas.journal import JournalCreate, JournalRead, JournalUpdate

router = APIRouter(prefix="/journal", tags=["Journal"])


@router.post("", response_model=JournalRead, status_code=status.HTTP_201_CREATED)
async def create_entry(data: JournalCreate, user_id: CurrentUserId, db: DbSession) -> JournalRead:
    entry = JournalEntryModel(id=uuid4(), user_id=user_id, **data.model_dump())
    db.add(entry)
    await db.flush()
    await db.refresh(entry)
    return JournalRead.model_validate(entry)


@router.get("", response_model=list[JournalRead])
async def list_entries(user_id: CurrentUserId, db: DbSession, skip: int = 0, limit: int = 20) -> list[JournalRead]:
    stmt = (
        select(JournalEntryModel)
        .where(JournalEntryModel.user_id == user_id, JournalEntryModel.deleted_at.is_(None))
        .order_by(JournalEntryModel.created_at.desc())
        .offset(skip)
        .limit(min(limit, 50))
    )
    result = await db.execute(stmt)
    return [JournalRead.model_validate(e) for e in result.scalars().all()]


@router.patch("/{entry_id}", response_model=JournalRead)
async def update_entry(
    entry_id: UUID, data: JournalUpdate, user_id: CurrentUserId, db: DbSession
) -> JournalRead:
    stmt = select(JournalEntryModel).where(
        JournalEntryModel.id == entry_id,
        JournalEntryModel.user_id == user_id,
        JournalEntryModel.deleted_at.is_(None),
    )
    entry = (await db.execute(stmt)).scalar_one_or_none()
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(entry, k, v)
    await db.flush()
    await db.refresh(entry)
    return JournalRead.model_validate(entry)


@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(entry_id: UUID, user_id: CurrentUserId, db: DbSession) -> None:
    from datetime import datetime, timezone

    stmt = select(JournalEntryModel).where(
        JournalEntryModel.id == entry_id,
        JournalEntryModel.user_id == user_id,
        JournalEntryModel.deleted_at.is_(None),
    )
    entry = (await db.execute(stmt)).scalar_one_or_none()
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    entry.deleted_at = datetime.now(timezone.utc)
    await db.flush()
