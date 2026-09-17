"""Internal DTOs for progress use cases."""

from datetime import date
from uuid import UUID

from pydantic import BaseModel


class ProgressQueryDTO(BaseModel):
    user_id: UUID
    days: int = 30


class VolumePointDTO(BaseModel):
    date: date
    total_volume_kg: float
    total_sets: int
    total_reps: int
