build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show_logs:
	docker compose -f local.yml logs

command:
	docker compose -f local.yml exec admin sh

migrate:
	docker compose -f local.yml run --rm admin python manage.py migrate

makemigrations:
	docker compose -f local.yml run --rm admin python manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm admin python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm admin python manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

flake8:
	docker compose -f local.yml exec admin flake8 .

black-check:
	docker compose -f local.yml exec admin black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec admin black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec admin black --exclude=venv .

isort-check:
	docker compose -f local.yml exec admin isort . --check-only --skip .venv --skip migrations

isort-diff:
	docker compose -f local.yml exec admin isort . --diff --skip .venv --skip migrations

isort:
	docker compose -f local.yml exec admin isort . --skip .venv --skip migrations

devops-db:
	docker compose -f local.yml exec postgres psql --username=postgres --dbname=Devops

test:
	docker compose -f local.yml run --rm admin python manage.py test