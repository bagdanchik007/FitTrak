from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.application.services.pr_service import evaluate_candidate
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
)
async def get_progress_summary(
    user_id: CurrentUserId,
    days: int = 30,
    service: ProgressService = Depends(get_progress_service),
) -> ProgressSummary:
    """days: window for volume series; clamped to [1, 365]."""
    days = max(1, min(days, 365))
    return await service.get_summary(user_id)


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


class PRCheckRequest(BaseModel):
    exercise_name: str = Field(..., min_length=1, max_length=120)
    weight_kg: float = Field(..., gt=0)
    reps: int = Field(..., ge=1)
    previous_best_kg: float | None = Field(None, ge=0)


class PRCheckResponse(BaseModel):
    is_personal_record: bool
    label: str | None
    previous_best_kg: float | None
    candidate_kg: float


@router.post(
    "/personal-record/check",
    response_model=PRCheckResponse,
    summary="Evaluate whether a candidate lift would be a PR",
)
async def check_personal_record(body: PRCheckRequest) -> PRCheckResponse:
    result = evaluate_candidate(
        exercise_name=body.exercise_name,
        previous_best_kg=body.previous_best_kg,
        weight_kg=body.weight_kg,
        reps=body.reps,
    )
    return PRCheckResponse(**result)
