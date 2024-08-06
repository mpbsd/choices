build:
	flask run

black:
	isort plan/conf/setup.py
	black -l 79 plan/conf/setup.py
	isort plan/conf/boost.py
	black -l 79 plan/conf/boost.py
	isort plan/data/load.py
	black -l 79 plan/data/load.py
	isort plan/core.py
	black -l 79 plan/core.py
	isort plan/home/routes.py
	black -l 79 plan/home/routes.py
	isort plan/home/models.py
	black -l 79 plan/home/models.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

ready:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt; \
	deactivate

.PHONY: build black clean ready
