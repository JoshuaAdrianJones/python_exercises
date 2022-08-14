env: python3 -m venv env
pip:
	pip install --upgrade pip
	pip install -r requirements.txt
docker-build:
	docker build . -t py
docker-run:
	docker run py pytest
test:
	 pytest
coverage: 
	coverage run -m pytest
	coverage report -m
lint:
	isort --profile black ./src/
	black  ./src/
	pylint ./src/
run:
	python src/saying_hello_app.py

prep:
	make lint
	make coverage
