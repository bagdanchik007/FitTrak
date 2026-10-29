"""Pagination metadata helpers."""

def page_meta(*, total: int, skip: int, limit: int) -> dict:
    limit = max(limit, 1)
    page = (skip // limit) + 1
    pages = max((total + limit - 1) // limit, 1) if total else 1
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "page": page,
        "pages": pages,
        "has_next": skip + limit < total,
        "has_prev": skip > 0,
    }
