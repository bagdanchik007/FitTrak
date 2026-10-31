"""Minimal CSV field escaping."""

def csv_escape(value: str | None) -> str:
    text = "" if value is None else str(value)
    if any(c in text for c in (',', '"', '\n', '\r')):
        return '"' + text.replace('"', '""') + '"'
    return text
