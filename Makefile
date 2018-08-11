test: docker_build
	pytest tests/
docker_build:
	docker build . -t freequest