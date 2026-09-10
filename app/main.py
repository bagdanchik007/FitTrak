from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.config import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title=settings.app_name,
    description=(
        "## FitTrack API\n\n"
        "A modern, clean-architecture fitness tracking backend built with **FastAPI**, "
        "**SQLAlchemy 2.0** and **PostgreSQL**.\n\n"
        "### Features\n"
        "- JWT Authentication (Access + Refresh Tokens)\n"
        "- Exercises & Workouts with Sets\n"
        "- Soft deletes & proper domain modeling\n"
        "- Fully asynchronous stack\n"
        "- Docker-ready\n"
    ),
    version="0.1.0",
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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/health", tags=["Health"])
async def health_check() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "healthy",
            "app": settings.app_name,
            "version": "0.1.0",
            "environment": settings.app_env,
        }
    )


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "health": "/health",
    }
