from app.domain.pagination.page import page_meta

def build_page_meta(total: int, skip: int, limit: int) -> dict:
    return page_meta(total=total, skip=skip, limit=limit)
