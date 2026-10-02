# Testing guide

## Unit tests

- Services with mocked repositories
- Validators, pagination, value objects, cache

```bash
pytest tests/unit -v
```

## Integration tests

- Full HTTP stack via `httpx.AsyncClient`
- Real DB session overridden in `conftest.py`

```bash
pytest tests/integration -v
```

## Coverage

```bash
pytest --cov=app --cov-report=term-missing
```

Integration: test_preferences_normalize, test_goal_progress

New: test_workout_metrics_service, test_goal_reopen

New: test_recovery_service, test_recovery
