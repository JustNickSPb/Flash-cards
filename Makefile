up:
	docker build . -t blacksheep
	docker run -p 80:8000 blacksheep

lint:
	isort app
	black app
	flake8 app
	mypy app
	

