.PHONY: dist docs

all: docs

docs:
	pdoc --html ./make_to_batch --output-dir ./docs/ --overwrite

dist:
	python setup.py sdist
	twine upload dist/* --skip-existing
