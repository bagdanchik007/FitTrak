"""Reusable value objects for the domain layer."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EmailAddress:
    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()
        if "@" not in normalized or "." not in normalized.split("@")[-1]:
            raise ValueError("Invalid email address")
        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True, slots=True)
class WeightKg:
    value: float

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Weight cannot be negative")


@dataclass(frozen=True, slots=True)
class Reps:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Reps cannot be negative")
