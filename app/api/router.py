from fastapi import APIRouter

from app.api.v1 import auth, exercises, health, progress, users, workouts

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(exercises.router)
api_router.include_router(workouts.router)
api_router.include_router(progress.router)
api_router.include_router(health.router)
