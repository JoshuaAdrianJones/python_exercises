test-all:
	python3 -m unittest tests/*.py

test:
	python3 -m unittest tests/test_sort_list.py
coverage: 
	coverage run -m unittest tests/*.py
	coverage report -m
docker-cleanup:
	docker images prune
	docker containers prune
docker-build:
	docker build . -t py
docker-run:
	docker run py