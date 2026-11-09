from app.domain.list_util.unique import unique_preserve

def test_unique():
    assert unique_preserve([1, 2, 1, 3]) == [1, 2, 3]
