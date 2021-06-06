ISORT_ARGS := --combine-star --combine-as --order-by-type --thirdparty scrapy --multi-line 3 --trailing-comma --force-grid-wrap 0 --use-parentheses --line-width 79

SRC_DIRS := ./app

check:
	python -m isort --check --diff $(ISORT_ARGS) $(SRC_DIRS)
	python -m black --check $(SRC_DIRS)
	flake8 $(SRC_DIRS)

format:
	python -m isort --apply $(ISORT_ARGS) $(SRC_DIRS)
	python -m black -l 79 -S $(SRC_DIRS)

run:
	gunicorn packages.app.wsgi:app --bind 0.0.0.0:5000 --timeout 1000 --worker-class gevent

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .tox/
	rm -rf docs/_build

test:
	pytest packages/tests/ -v --cov=packages.app
	coverage html
