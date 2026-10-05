"""FitTrack FastAPI application entrypoint."""

from __future__ import annotations

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.core.middleware import RequestLoggingMiddleware
from app.core.version import __version__

settings = get_settings()

OPENAPI_TAGS = [
    {"name": "Auth", "description": "Registration, login, token refresh"},
    {"name": "Users", "description": "Profile and account"},
    {"name": "Exercises", "description": "Exercise catalog"},
    {"name": "Workouts", "description": "Training sessions and sets"},
    {"name": "Progress", "description": "Aggregates and personal records"},
    {"name": "Goals", "description": "User training goals"},
    {"name": "Health", "description": "Liveness and readiness probes"},
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield


app = FastAPI(
    title=settings.app_name,
    description=(
        "FitTrack – domain-driven fitness API built with FastAPI, SQLAlchemy 2.0 and PostgreSQL."
    ),
    version=__version__,
    openapi_tags=OPENAPI_TAGS,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}"
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)
register_exception_handlers(app)

app.include_router(api_router, prefix=settings.api_v1_prefix)
