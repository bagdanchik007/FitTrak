"""Meta endpoints (version, feature flags placeholder)."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.core.feature_flags import FEATURES

router = APIRouter(prefix="/meta", tags=["Meta"])
settings = get_settings()


@router.get("/version")
async def version() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "version": "0.4.0",
        "environment": settings.app_env,
    }


@router.get("/features")
async def features() -> dict[str, bool]:
    return dict(FEATURES)
