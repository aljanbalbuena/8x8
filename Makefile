black:
	black . --exclude venv

flake8:
	flake8 . --exclude venv

quality_check: black flake8
