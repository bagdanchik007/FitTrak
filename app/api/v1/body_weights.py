from uuid import uuid4

from fastapi import APIRouter, status
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.body_weight import BodyWeightModel
from app.schemas.body_weight import BodyWeightCreate, BodyWeightRead

router = APIRouter(prefix="/body-weights", tags=["Body Weight"])


@router.post("", response_model=BodyWeightRead, status_code=status.HTTP_201_CREATED)
async def log_weight(data: BodyWeightCreate, user_id: CurrentUserId, db: DbSession) -> BodyWeightRead:
    row = BodyWeightModel(id=uuid4(), user_id=user_id, **data.model_dump())
    db.add(row)
    await db.flush()
    await db.refresh(row)
    return BodyWeightRead.model_validate(row)


@router.get("", response_model=list[BodyWeightRead])
async def list_weights(
    user_id: CurrentUserId, db: DbSession, skip: int = 0, limit: int = 50
) -> list[BodyWeightRead]:
    stmt = (
        select(BodyWeightModel)
        .where(BodyWeightModel.user_id == user_id)
        .order_by(BodyWeightModel.recorded_at.desc())
        .offset(skip)
        .limit(min(limit, 100))
    )
    result = await db.execute(stmt)
    return [BodyWeightRead.model_validate(r) for r in result.scalars().all()]
