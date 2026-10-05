"""Meta endpoints (version, feature flags placeholder)."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.core.feature_flags import FEATURES
from app.core.version import __version__
from app.schemas.meta import VersionResponse

router = APIRouter(prefix="/meta", tags=["Meta"])
settings = get_settings()


@router.get("/version", response_model=VersionResponse)
async def version() -> VersionResponse:
    return VersionResponse(
        app=settings.app_name,
        version=__version__,
        environment=settings.app_env,
    )


@router.get("/features")
async def features() -> dict[str, bool]:
    return dict(FEATURES)


@router.get("/build")
async def build_info() -> dict[str, str]:
    return {"version": __version__, "api": "v1"}
