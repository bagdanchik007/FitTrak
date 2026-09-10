from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(slots=True)
class PersonalRecord:
    exercise_id: UUID
    exercise_name: str
    max_weight_kg: float | None
    max_reps: int | None
    estimated_1rm: float | None
    achieved_at: date | None


@dataclass(slots=True)
class VolumeEntry:
    date: date
    total_volume_kg: float
    total_sets: int
    total_reps: int


@dataclass(slots=True)
class ProgressSummary:
    total_workouts: int
    total_sets: int
    total_volume_kg: float
    personal_records: list[PersonalRecord]
    volume_last_30_days: list[VolumeEntry]
