from app.domain.export.csv_escape import csv_escape

def test_plain():
    assert csv_escape("ok") == "ok"

def test_comma():
    assert csv_escape("a,b") == '"a,b"'
