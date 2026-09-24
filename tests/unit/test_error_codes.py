from app.core.errors import ErrorCode


def test_error_codes_are_stable_strings():
    assert ErrorCode.NOT_FOUND == "not_found"
    assert ErrorCode.UNAUTHORIZED == "unauthorized"
    assert ErrorCode.RATE_LIMITED == "rate_limited"
