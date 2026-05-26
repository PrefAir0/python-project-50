install:
	uv sync


build: 
	uv build

init:
	uv run ruff check gendiff

test:
<<<<<<< HEAD:makefile
uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

test-coverage — генерирует coverage.xml по модулю gendiff.
=======
	run pytest
	
>>>>>>> 1856bd7e4c80a267cfa12927671f4a359cef0c97:Makefile
