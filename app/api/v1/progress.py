from fastapi import APIRouter, Depends

from app.application.services.progress_service import ProgressService
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.progress_repository import SQLAlchemyProgressRepository
from app.schemas.progress import ProgressSummary

router = APIRouter(prefix="/progress", tags=["Progress"])


def get_progress_service(db: DbSession) -> ProgressService:
    return ProgressService(repo=SQLAlchemyProgressRepository(db))


@router.get(
    "/summary",
    response_model=ProgressSummary,
    summary="Get progress summary for the current user",
    description=(
        "Returns total workouts, sets, volume, personal records "
        "(with estimated 1RM) and daily volume for the last 30 days."
    ),
)
async def get_progress_summary(
    user_id: CurrentUserId,
    service: ProgressService = Depends(get_progress_service),
) -> ProgressSummary:
    return await service.get_summary(user_id)
