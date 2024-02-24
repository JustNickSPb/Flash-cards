up:
	docker compose up --build -d

lint:
	isort app
	black app
	flake8 app
	mypy app
	

