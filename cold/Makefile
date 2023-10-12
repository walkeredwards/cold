all: unittest test
	@echo "All done..."

unittest:
	pytest -v test_cold.py

test:
	@cat cold-001.in | python cold.py | diff - cold-001.ans
	@cat cold-002.in | python cold.py | diff - cold-002.ans
	@echo "All Local Tests Passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

kattis:
	@kattis -f cold.py