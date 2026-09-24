from app.core.http_headers import PROCESS_TIME, RATE_LIMIT_REMAINING, REQUEST_ID


def test_header_constants():
    assert REQUEST_ID == "X-Request-ID"
    assert PROCESS_TIME == "X-Process-Time"
    assert RATE_LIMIT_REMAINING == "X-RateLimit-Remaining"
