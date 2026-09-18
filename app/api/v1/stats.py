from fastapi import APIRouter, Depends

from app.application.services.stats_service import DashboardStats, StatsService
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.repositories.progress_repository import SQLAlchemyProgressRepository
from app.infrastructure.repositories.workout_repository import SQLAlchemyWorkoutRepository

router = APIRouter(prefix="/stats", tags=["Stats"])


def get_stats_service(db: DbSession) -> StatsService:
    return StatsService(
        progress_repo=SQLAlchemyProgressRepository(db),
        workout_repo=SQLAlchemyWorkoutRepository(db),
    )


@router.get(
    "/dashboard",
    response_model=DashboardStats,
    summary="Dashboard stats for current user",
)
async def get_dashboard(
    user_id: CurrentUserId,
    service: StatsService = Depends(get_stats_service),
) -> DashboardStats:
    return await service.dashboard(user_id)
