.DEFAULT_GOAL := help

help:
	@echo "make clean >> Clean ./build, ./dis, ./*.egg-info"
	@echo "make build >> Build the package, by running setup.py"
	@echo "make install-local >> Install the previously built package (locally)"
	@echo "make save >> Git add, commit, push to master"
	@echo "make new-graph name=graph-component-name >> Create an empty graph component file, ready to be developed"
	@echo "make graph text=\"This is an example text\" name=person,birth >> Test the full stack on a given text, and debug a list of components"
	@echo "make analyze text=\"This is an example text\" >> Run a full spaCy analysis on the given text"
	@echo "make test >> Run all the tests in ./tests/ folder"

clean:
	@rm -rf ./build
	@rm -rf ./dist
	@rm -rf ./knex.egg-info

build:
	@python3 setup.py sdist bdist_wheel

install-local:
	@pip install -e .
	
save:
	@git add .
	@git commit -m "save with make command"
	@git push origin main

install: clean build install

new-graph:
	@echo "Creating graph component at ./knex/graphs/$$name.py"; \
	sed -e "s/THE_NAME/$$name/g" ./templates/create-graph-component.py > ./knex/graphs/$$name.py; \
	echo "\nfrom .$$name import *" >> ./knex/graphs/__init__.py; \
	code ./knex/graphs/$$name.py

graph:
	@python3.12 ./scripts/graph-component-test.py "$$text" $$name

analyze:
	@python3.12 ./scripts/spacy-analyze-text.py "$$text"

test:
	@python3.12 ./tests/full-graphs.py