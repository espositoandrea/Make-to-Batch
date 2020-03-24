.PHONY: dist docs

all: docs

docs:
	pdoc --html ./make_to_batch --output-dir ./docs/ --force

dist:
	python3 setup.py sdist
	twine upload dist/* --skip-existing
