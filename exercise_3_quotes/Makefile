all: prep

env: 
	python3 -m venv env
pip:
	pip install --upgrade pip
	pip install -r requirements.txt
docker-build:
	docker build . -t py
docker-run:
	docker run py pytest
test:
	 pytest ./src/

lint:
	isort --profile black ./src/
	black  ./src/
	flake8 --ignore=E501 ./src/
types:
	pyright ./src/

prep:
	make types
	make test
	make lint
