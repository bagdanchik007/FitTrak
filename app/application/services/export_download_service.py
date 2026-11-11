from app.domain.export.csv_header import header_line
from app.domain.export.csv_escape import csv_escape
from app.domain.workout.export_row import workout_export_row


def build_csv_document(rows: list[tuple[str, ...]]) -> str:
    lines = [header_line()]
    for row in rows:
        lines.append(",".join(csv_escape(c) for c in row))
    return "\n".join(lines) + "\n"
