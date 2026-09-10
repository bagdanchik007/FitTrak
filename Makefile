.PHONY: help up down build logs migrate revision test lint format seed

help:
	@echo "FitTrack – available commands:"
	@echo "  make up        – Start the full stack (docker compose)"
	@echo "  make down      – Stop containers"
	@echo "  make build     – Rebuild images"
	@echo "  make logs      – Follow API logs"
	@echo "  make migrate   – Run Alembic migrations"
	@echo "  make revision  – Create new Alembic revision (autogenerate)"
	@echo "  make test      – Run pytest"
	@echo "  make lint      – Run ruff + mypy"
	@echo "  make format    – Format code with ruff"
	@echo "  make seed      – Seed demo data"

up:
	docker compose up --build -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f api

migrate:
	docker compose exec api alembic upgrade head

revision:
	docker compose exec api alembic revision --autogenerate -m "$(m)"

test:
	pytest -v --cov=app --cov-report=term-missing

lint:
	ruff check app tests
	mypy app

format:
	ruff format app tests
	ruff check --fix app tests

seed:
	python -m scripts.seed
