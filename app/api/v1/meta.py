"""Meta endpoints (version, feature flags placeholder)."""

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(prefix="/meta", tags=["Meta"])
settings = get_settings()


@router.get("/version")
async def version() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "version": "0.3.0",
        "environment": settings.app_env,
    }


@router.get("/features")
async def features() -> dict[str, bool]:
    return {
        "refresh_tokens": True,
        "progress_tracking": True,
        "stats_dashboard": True,
        "rate_limiting": True,
        "soft_deletes": True,
        "goals": True,
        "body_weight": True,
        "templates": True,
        "preferences": True,
        "activity_feed": True,
        "csv_export": True,
        "journal": True,
        "favorites": True,
        "streaks": True,
        "weekly_summary": True,
    }
