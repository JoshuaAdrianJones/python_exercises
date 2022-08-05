docker-build:
	docker build . -t py
docker-run:
	docker run py
test:
	python3 -m unittest tests/*.py
coverage: 
	coverage run -m unittest tests/*.py
	coverage report -m
lint:
	pylint ./src/
run:
	make test coverage lint
