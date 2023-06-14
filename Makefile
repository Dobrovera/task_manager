install:
	poetry install

lint:
	poetry run flake8 task_manager

build:
	poetry build

test:
	coverage run manage.py test

test-cov:
	coverage xml
