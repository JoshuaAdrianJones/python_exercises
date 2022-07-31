test-all:
	python3 -m unittest tests/*.py

test:
	python3 -m unittest tests/*

docker-cleanup:
	docker images prune
	docker containers prune
docker-build:
	docker build . -t py
docker-run:
	docker run py

checkers: 
	coverage run -m unittest tests/*.py
	coverage report -m
	pylint src/