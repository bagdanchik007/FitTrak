from app.core.version import __version__
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.core.config import get_settings
from app.core.dependencies import DbSession
from app.core.status_texts import DB_UNAVAILABLE, STATUS_OK

router = APIRouter(tags=["Health"])
settings = get_settings()


@router.get("/health", summary="Basic health check")
async def health() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "healthy",
            "app": settings.app_name,
            "version": __version__,
            "features_enabled": True,
            "environment": settings.app_env,
        }
    )


@router.get("/health/ready", summary="Readiness probe (includes DB)")
async def readiness(db: DbSession) -> JSONResponse:
    try:
        await db.execute(text("SELECT 1"))
        db_status = STATUS_OK
    except Exception:
        db_status = DB_UNAVAILABLE

    status_code = 200 if db_status == STATUS_OK else 503
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "ready" if db_status == STATUS_OK else "not_ready",
            "database": db_status,
        },
    )


# /health = liveness (process up); /health/ready = readiness (DB up)
