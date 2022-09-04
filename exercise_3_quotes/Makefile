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
coverage: 
	coverage run -m pytest
	coverage report -m
lint:
	isort --profile black ./src/
	black  ./src/
	pylint --rcfile .pylintrc ./src/
types:
	mypy ./src/

prep:
	make coverage
	make types
	make test
	make lint
