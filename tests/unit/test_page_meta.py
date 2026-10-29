from app.domain.pagination.page import page_meta

def test_page():
    m = page_meta(total=45, skip=20, limit=20)
    assert m["page"] == 2
    assert m["has_next"] is True
