from app.domain.export.csv_header import header_line

def test_header():
    assert "title" in header_line()
