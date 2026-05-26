install:
	uv sync


build: 
	uv build

init:
	uv run ruff check gendiff

test:
uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

