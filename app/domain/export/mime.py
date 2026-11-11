"""MIME type for CSV downloads."""

CSV_MIME = "text/csv"


def content_disposition(filename: str = "workouts.csv") -> str:
    safe = filename.replace('"', "")
    return f'attachment; filename="{safe}"'
