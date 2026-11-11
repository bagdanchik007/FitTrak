"""Count data rows in a CSV document (excluding header)."""

def csv_data_row_count(document: str) -> int:
    lines = [ln for ln in document.splitlines() if ln.strip()]
    return max(0, len(lines) - 1)
