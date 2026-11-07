"""Build safe export filenames."""

from datetime import date

def export_filename(prefix: str, *, day: date | None = None) -> str:
    d = day or date.today()
    safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in prefix).strip("-") or "export"
    return f"{safe}-{d.isoformat()}.csv"
