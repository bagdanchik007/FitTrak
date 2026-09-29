from contextlib import asynccontextmanager

import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.version import __version__
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.core.exception_handlers import register_exception_handlers
from app.core.middleware import RequestLoggingMiddleware

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield



OPENAPI_TAGS = [
    {"name": "Auth", "description": "Registration, login, token refresh"},
    {"name": "Users", "description": "Profile and account"},
    {"name": "Exercises", "description": "Exercise catalog"},
    {"name": "Workouts", "description": "Training sessions and sets"},
    {"name": "Progress", "description": "Aggregates and personal records"},
    {"name": "Goals", "description": "User training goals"},
    {"name": "Health", "description": "Liveness and readiness probes"},
]

app = FastAPI(
    openapi_tags=OPENAPI_TAGS,
    
    title=settings.app_name,
    description=(
        "## FitTrack API\n\n"
        "A modern, clean-architecture fitness tracking backend built with **FastAPI**, "
        "**SQLAlchemy 2.0** and **PostgreSQL**.\n\n"
        "### Features\n"
        "- JWT Authentication (Access + Refresh Tokens)\n"


@app.middleware("http")

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response

async def add_process_time_header(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}"
    return response

        "- Exercises & Workouts with Sets\n"
        "- Progress tracking (PRs, volume, estimated 1RM)\n"
        "- Soft deletes & proper domain modeling\n"
        "- Fully asynchronous stack\n"
        "- Docker-ready\n"
    ),
    version=__version__,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
    contact={
        "name": "FitTrack",
        "url": "https://github.com/yourusername/fittrack",
    },
    license_info={
        "name": "MIT",
    },
)

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


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "health": "/api/v1/health",
    }

# OpenAPI schema is available at /api/v1/openapi.json
