all: prep

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
	python src/saying_hello_app.py

types:
	pyright ./src/

prep:
	make lint
	make types
	make test
