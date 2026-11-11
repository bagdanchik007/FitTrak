"""Map workout fields to an ordered CSV row tuple."""

from datetime import date


def workout_export_row(
    *,
    id: str,
    title: str,
    performed_at: date | str | None,
    duration_minutes: int | None,
    total_volume_kg: float | None,
    notes: str | None,
) -> tuple[str, ...]:
    return (
        str(id),
        title or "",
        str(performed_at or ""),
        "" if duration_minutes is None else str(duration_minutes),
        "" if total_volume_kg is None else str(total_volume_kg),
        (notes or "").replace("\n", " ").strip(),
    )
