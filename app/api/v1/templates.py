from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.template import WorkoutTemplateItemModel, WorkoutTemplateModel
from app.schemas.template import TemplateCreate, TemplateRead

router = APIRouter(prefix="/templates", tags=["Templates"])


@router.post("", response_model=TemplateRead, status_code=status.HTTP_201_CREATED)
async def create_template(
    data: TemplateCreate, user_id: CurrentUserId, db: DbSession
) -> TemplateRead:
    tmpl = WorkoutTemplateModel(
        id=uuid4(), user_id=user_id, name=data.name, description=data.description
    )
    db.add(tmpl)
    await db.flush()
    for item in data.items:
        db.add(
            WorkoutTemplateItemModel(
                id=uuid4(),
                template_id=tmpl.id,
                exercise_id=item.exercise_id,
                target_sets=item.target_sets,
                target_reps=item.target_reps,
                sort_order=item.sort_order,
            )
        )
    await db.flush()
    stmt = (
        select(WorkoutTemplateModel)
        .options(selectinload(WorkoutTemplateModel.items))
        .where(WorkoutTemplateModel.id == tmpl.id)
    )
    tmpl = (await db.execute(stmt)).scalar_one()
    return TemplateRead.model_validate(tmpl)


@router.get("", response_model=list[TemplateRead])
async def list_templates(user_id: CurrentUserId, db: DbSession) -> list[TemplateRead]:
    stmt = (
        select(WorkoutTemplateModel)
        .options(selectinload(WorkoutTemplateModel.items))
        .where(
            WorkoutTemplateModel.user_id == user_id,
            WorkoutTemplateModel.deleted_at.is_(None),
        )
        .order_by(WorkoutTemplateModel.name)
    )
    result = await db.execute(stmt)
    return [TemplateRead.model_validate(t) for t in result.scalars().all()]


@router.get("/{template_id}", response_model=TemplateRead)
async def get_template(
    template_id: UUID, user_id: CurrentUserId, db: DbSession
) -> TemplateRead:
    stmt = (
        select(WorkoutTemplateModel)
        .options(selectinload(WorkoutTemplateModel.items))
        .where(
            WorkoutTemplateModel.id == template_id,
            WorkoutTemplateModel.user_id == user_id,
            WorkoutTemplateModel.deleted_at.is_(None),
        )
    )
    tmpl = (await db.execute(stmt)).scalar_one_or_none()
    if not tmpl:
        raise HTTPException(status_code=404, detail="Template not found")
    return TemplateRead.model_validate(tmpl)


@router.delete("/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_template(
    template_id: UUID, user_id: CurrentUserId, db: DbSession
) -> None:
    from datetime import datetime, timezone

    stmt = select(WorkoutTemplateModel).where(
        WorkoutTemplateModel.id == template_id,
        WorkoutTemplateModel.user_id == user_id,
        WorkoutTemplateModel.deleted_at.is_(None),
    )
    tmpl = (await db.execute(stmt)).scalar_one_or_none()
    if not tmpl:
        raise HTTPException(status_code=404, detail="Template not found")
    tmpl.deleted_at = datetime.now(timezone.utc)
    await db.flush()
