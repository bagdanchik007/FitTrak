"""Export helpers for tabular workout data."""


def workout_csv_header() -> list[str]:
    return [
        "performed_at",
        "exercise",
        "set_number",
        "reps",
        "weight_kg",
        "rpe",
        "duration_minutes",
    ]


def format_csv_row(values: list) -> str:
    out = []
    for v in values:
        if v is None:
            out.append("")
        else:
            s = str(v)
            if "," in s or '"' in s:
                s = '"' + s.replace('"', '""') + '"'
            out.append(s)
    return ",".join(out)
