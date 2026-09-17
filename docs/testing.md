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
