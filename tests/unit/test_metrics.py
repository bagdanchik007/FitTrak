from app.core.metrics import get, incr, snapshot


def test_metrics_incr():
    incr("test_metric_x", 2)
    assert get("test_metric_x") >= 2
    snap = snapshot()
    assert "test_metric_x" in snap
