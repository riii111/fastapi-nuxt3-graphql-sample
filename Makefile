dev-build:
	docker compose -f ./docker-compose.yml -f docker-compose.dev.yml build
dev-up:
	docker compose -f ./docker-compose.yml -f docker-compose.dev.yml up -d
dev-down:
	docker compose -f ./docker-compose.yml -f docker-compose.dev.yml down
dev-restart-all:
	make dev-down
	make dev-up
dev-restart:
	docker compose -f ./docker-compose.yml -f docker-compose.dev.yml rm -fsv ${container}
	docker compose -f ./docker-compose.yml -f docker-compose.dev.yml up -d ${container}

prod-build:
	docker compose -f ./docker-compose.yml -f docker-compose.prod.yml build
prod-up:
	docker compose -f ./docker-compose.yml -f docker-compose.prod.yml up -d
prod-down:
	docker compose -f ./docker-compose.yml -f docker-compose.prod.yml down
prod-restart:
	docker compose -f ./docker-compose.yml -f docker-compose.prod.yml restart

container=legal-scheduler-frontend
command=/bin/bash
tail=200
logs:
	docker compose logs --tail=${tail} ${container}
logs-all:
	docker compose logs --tail=${tail}
exec:
	docker compose exec ${container} ${command}

lintfix-python:
	black . && isort . --profile black && flake8 --max-line-length=88 --ignore=E501,W503
lintfix-python-docker:
	docker compose run --rm ${container} bash -c "poetry run black . && poetry run isort . --profile black"