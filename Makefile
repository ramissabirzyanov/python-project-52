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

shell:
		python manage.py shell_plus --print-sql

test:
		python manage.py test

msg:
		python manage.py makemessages --ignore=".env"  -l en

compile:
		python manage.py compilemessages