.PHONY: install clean isort black flake8 format

default: install

install:
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	docker system prune

ISORT_ARGS=--profile black
BLACK_ARGS=--line-length 90
FLAKE8_ARGS=--ignore=E501

isort:
	isort $(ISORT_ARGS) .

black:
	black $(BLACK_ARGS) .

flake8:
	flake8 $(FLAKE8_ARGS) .

format: isort black flake8
