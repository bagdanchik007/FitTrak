"""Preserve-order unique values."""

def unique_preserve(items: list) -> list:
    seen: set = set()
    out = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out
