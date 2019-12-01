all: docs

docs:
    pdoc --html ./make_to_batch --output-dir docs/ --overwrite