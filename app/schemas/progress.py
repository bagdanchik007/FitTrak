"""Progress-related schemas."""

from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class PersonalRecord(BaseModel):
    exercise_id: UUID
    exercise_name: str
    max_weight_kg: float | None = None
    max_reps: int | None = None
    estimated_1rm: float | None = None
    achieved_at: date | None = None


class VolumeEntry(BaseModel):
    date: date
    total_volume_kg: float = Field(..., description="Sum of weight × reps for the day")
    total_sets: int
    total_reps: int


class ProgressSummary(BaseModel):
    total_workouts: int
    total_sets: int
    total_volume_kg: float
    personal_records: list[PersonalRecord] = []
    volume_last_30_days: list[VolumeEntry] = []

# estimated_1rm uses a simplified Epley formula: weight * (1 + reps/30)
