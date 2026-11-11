from app.domain.export.row_count import csv_data_row_count

def test_count():
    assert csv_data_row_count("h\na\nb\n") == 2
