run:
		poetry run python manage.py runserver

migrations:
		poetry run python manage.py makemigrations

migrate:
		poetry run python manage.py migrate

build:
		./build.sh

lint:
		poetry run flake8

start:
		python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

install:
		poetry install