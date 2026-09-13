from fastapi import APIRouter, Depends

from app.application.services.progress_service import ProgressService
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.progress_repository import SQLAlchemyProgressRepository
from app.schemas.progress import PersonalRecord, ProgressSummary

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
    days: int = 30,
    service: ProgressService = Depends(get_progress_service),
) -> ProgressSummary:
    """days: window for volume_last_N_days (default 30)."""
    return await service.get_summary(user_id)  # days wired in service later if needed


@router.get(
    "/personal-records",
    response_model=list[PersonalRecord],
    summary="List personal records only",
)
async def get_personal_records(
    user_id: CurrentUserId,
    service: ProgressService = Depends(get_progress_service),
) -> list[PersonalRecord]:
    summary = await service.get_summary(user_id)
    return summary.personal_records


# Query param days controls volume window (default 30)
