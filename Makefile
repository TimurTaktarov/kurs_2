linter:
	@echo "Run linters"
	black .
	isort .
	flake8 .
	pytest .
