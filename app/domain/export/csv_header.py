"""CSV header labels for workout export."""

WORKOUT_CSV_HEADERS = (
    "id",
    "title",
    "performed_at",
    "duration_minutes",
    "total_volume_kg",
    "notes",
)


def header_line() -> str:
    return ",".join(WORKOUT_CSV_HEADERS)
