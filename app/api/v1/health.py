from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.core.config import get_settings
from app.core.dependencies import DbSession

router = APIRouter(tags=["Health"])
settings = get_settings()


@router.get("/health", summary="Basic health check")
async def health() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "healthy",
            "app": settings.app_name,
            "version": "0.1.0",
            "environment": settings.app_env,
        }
    )


@router.get("/health/ready", summary="Readiness probe (includes DB)")
async def readiness(db: DbSession) -> JSONResponse:
    try:
        await db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception:
        db_status = "unavailable"

    status_code = 200 if db_status == "ok" else 503
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "ready" if db_status == "ok" else "not_ready",
            "database": db_status,
        },
    )

# /health = liveness (process up); /health/ready = readiness (DB up)
