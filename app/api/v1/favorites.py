from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.exercise import ExerciseModel
from app.infrastructure.database.models.favorite import ExerciseFavoriteModel
from app.schemas.favorite import FavoriteCreate, FavoriteRead

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.post("", response_model=FavoriteRead, status_code=status.HTTP_201_CREATED)
async def add_favorite(data: FavoriteCreate, user_id: CurrentUserId, db: DbSession) -> FavoriteRead:
    ex = (
        await db.execute(
            select(ExerciseModel).where(
                ExerciseModel.id == data.exercise_id, ExerciseModel.deleted_at.is_(None)
            )
        )
    ).scalar_one_or_none()
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")

    existing = (
        await db.execute(
            select(ExerciseFavoriteModel).where(
                ExerciseFavoriteModel.user_id == user_id,
                ExerciseFavoriteModel.exercise_id == data.exercise_id,
            )
        )
    ).scalar_one_or_none()
    if existing:
        return FavoriteRead.model_validate(existing)

    fav = ExerciseFavoriteModel(id=uuid4(), user_id=user_id, exercise_id=data.exercise_id)
    db.add(fav)
    await db.flush()
    await db.refresh(fav)
    return FavoriteRead.model_validate(fav)


@router.get("", response_model=list[FavoriteRead])
async def list_favorites(user_id: CurrentUserId, db: DbSession) -> list[FavoriteRead]:
    stmt = (
        select(ExerciseFavoriteModel)
        .where(ExerciseFavoriteModel.user_id == user_id)
        .order_by(ExerciseFavoriteModel.created_at.desc())
    )
    result = await db.execute(stmt)
    return [FavoriteRead.model_validate(f) for f in result.scalars().all()]


@router.delete("/{exercise_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_favorite(exercise_id: UUID, user_id: CurrentUserId, db: DbSession) -> None:
    stmt = select(ExerciseFavoriteModel).where(
        ExerciseFavoriteModel.user_id == user_id,
        ExerciseFavoriteModel.exercise_id == exercise_id,
    )
    fav = (await db.execute(stmt)).scalar_one_or_none()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")
    await db.delete(fav)
    await db.flush()
