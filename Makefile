linter:
	@echo "Run linters"
	black .
	isort .
	flake .

info:
	echo "Hello"
	@echo "Hello 2"