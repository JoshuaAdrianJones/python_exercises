docker-build:
	docker build . -t py
docker-run:
	docker run py
test:
	python3 -m unittest
coverage: 
	coverage run -m unittest
	coverage report -m
lint:
	black  ./src/
	black  ./tests/
	pylint ./src/
	pylint ./tests/
run:
	make test coverage lint
