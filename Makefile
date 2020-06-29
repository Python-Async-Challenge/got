PROJECT_NAME=got_microservice

default: run

tests:
	pipenv run pytest --cov=. --cov-report html

run:
	pipenv run python main.py

update:
	git submodule update --remote

init-kong:
	docker-compose run kong kong migrations bootstrap