"""Split a list into fixed-size chunks."""

def chunked(items: list, size: int) -> list[list]:
    if size <= 0:
        return [items] if items else []
    return [items[i : i + size] for i in range(0, len(items), size)]
