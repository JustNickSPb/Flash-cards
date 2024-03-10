up:
	pipenv install
	docker compose up --build

lint:
	isort app
	black app
	flake8 app
	mypy app
	

