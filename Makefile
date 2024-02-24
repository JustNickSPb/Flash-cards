up:
	pipenv lock
	docker compose up --build

lint:
	isort app
	black app
	flake8 app
	mypy app
	

