from fastapi import APIRouter

from app.api.v1 import activity, auth, body_weights, exercises, favorites, goals, health, journal, meta, preferences, progress, stats, streaks, summary, templates, users, workouts

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(exercises.router)
api_router.include_router(workouts.router)
api_router.include_router(progress.router)
api_router.include_router(stats.router)
api_router.include_router(meta.router)
api_router.include_router(goals.router)
api_router.include_router(body_weights.router)
api_router.include_router(templates.router)
api_router.include_router(preferences.router)
api_router.include_router(activity.router)
api_router.include_router(journal.router)
api_router.include_router(favorites.router)
api_router.include_router(streaks.router)
api_router.include_router(summary.router)
api_router.include_router(health.router)
