SHELL := /bin/bash

setup-linux:
	sh bin/setup.sh
	python3 -m venv .venv
	source .venv/bin/activate
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
	source ${HOME}/.poetry/env

seeds:
	poetry run seeder
