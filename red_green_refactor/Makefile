test-all:
	python3 -m unittest tests/*.py

test:
	python3 -m unittest tests/*
coverage: 
	coverage run -m unittest tests/*.py
	coverage report -m

docker-build:
	docker build . -t py
docker-run:
	docker run py