"""Seed the database with demo exercises and a sample user."""

import asyncio
from datetime import date, datetime, timezone
from uuid import uuid4

from app.core.security import get_password_hash
from app.infrastructure.database.models.exercise import ExerciseModel
from app.infrastructure.database.models.user import UserModel
from app.infrastructure.database.models.workout import WorkoutModel, WorkoutSetModel
from app.infrastructure.database.session import AsyncSessionLocal


DEMO_EXERCISES = [
    ("Bench Press", "chest", "barbell"),
    ("Squat", "legs", "barbell"),
    ("Deadlift", "back", "barbell"),
    ("Overhead Press", "shoulders", "barbell"),
    ("Barbell Row", "back", "barbell"),
    ("Pull-Up", "back", "bodyweight"),
    ("Dumbbell Curl", "biceps", "dumbbell"),
    ("Tricep Pushdown", "triceps", "cable"),
    ("Leg Press", "legs", "machine"),
    ("Plank", "core", "bodyweight"),
]


async def seed() -> None:
    async with AsyncSessionLocal() as session:
        # Demo user
        user = UserModel(
            id=uuid4(),
            email="demo@fittrack.local",
            hashed_password=get_password_hash("DemoPass123!"),
            full_name="Demo Athlete",
            is_active=True,
        )
        session.add(user)
        await session.flush()

        # Exercises
        exercise_ids = []
        for name, muscle, equipment in DEMO_EXERCISES:
            ex = ExerciseModel(
                id=uuid4(),
                name=name,
                muscle_group=muscle,
                equipment=equipment,
                created_by=user.id,
            )
            session.add(ex)
            exercise_ids.append(ex.id)

        await session.flush()

        # Sample workout
        workout = WorkoutModel(
            id=uuid4(),
            user_id=user.id,
            title="Full Body Strength",
            performed_at=date.today(),
            duration_minutes=65,
            notes="Feeling strong today",
        )
        session.add(workout)
        await session.flush()

        # A few sets
        for i, ex_id in enumerate(exercise_ids[:4], start=1):
            for set_num in range(1, 4):
                session.add(
                    WorkoutSetModel(
                        id=uuid4(),
                        workout_id=workout.id,
                        exercise_id=ex_id,
                        set_number=set_num,
                        reps=8 + set_num,
                        weight_kg=60.0 + (i * 5) - set_num,
                        rpe=7.5,
                    )
                )

        await session.commit()
        print("✅ Seed completed")
        print(f"   User: demo@fittrack.local / DemoPass123!")
        print(f"   Exercises: {len(DEMO_EXERCISES)}")
        print(f"   Sample workout created")


if __name__ == "__main__":
    asyncio.run(seed())
