install:
	poetry install

lint:
	poetry run flake8 task_manager

build:
	poetry build
