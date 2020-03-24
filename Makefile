.PHONY: dist docs

all: docs

docs:
	pdoc --html ./make_to_batch --html-dir ./docs/ --overwrite

dist:
	python3 setup.py sdist
	twine upload dist/* --skip-existing
