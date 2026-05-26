install:
	uv sync


build: 
	uv build

init:
	uv run ruff check gendiff

test:
	run pytest
	
