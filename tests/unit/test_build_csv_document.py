from app.application.services.export_download_service import build_csv_document

def test_doc():
    text = build_csv_document([("1", "Push", "2026-01-01", "60", "100", "")])
    assert "title" in text
    assert "Push" in text
