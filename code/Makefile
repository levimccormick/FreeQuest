build:
	docker build . -t freequest
	
heroes: build
	docker run --rm -it \
		-w /app \
		freequest \
		python test_heroes.py