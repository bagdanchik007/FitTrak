from app.domain.list_util.chunk import chunked

def test_chunk():
    assert chunked([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
