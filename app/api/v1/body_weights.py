from uuid import uuid4

from fastapi import APIRouter, status
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.core.limits import MAX_PAGE_SIZE
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
        .limit(min(limit, MAX_PAGE_SIZE))
    )
    result = await db.execute(stmt)
    return [BodyWeightRead.model_validate(r) for r in result.scalars().all()]


@router.get("/delta", response_model=dict)
async def weight_delta(user_id: CurrentUserId, db: DbSession) -> dict:
    """Difference between earliest and latest logged weight for the user."""
    stmt = (
        select(BodyWeightModel)
        .where(BodyWeightModel.user_id == user_id)
        .order_by(BodyWeightModel.recorded_at.asc())
    )
    rows = (await db.execute(stmt)).scalars().all()
    if len(rows) < 2:
        return {"delta_kg": None, "samples": len(rows)}
    delta = round(rows[-1].weight_kg - rows[0].weight_kg, 2)
    return {
        "delta_kg": delta,
        "samples": len(rows),
        "from_date": str(rows[0].recorded_at),
        "to_date": str(rows[-1].recorded_at),
    }

