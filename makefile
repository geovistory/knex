.DEFAULT_GOAL := clean

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./geovdata.egg-info

build:
	python3 setup.py sdist bdist_wheel

install-local:
	pip install -e .
	
save:
	git add .
	git commit -m "save"
	git push origin master

install: clean build install

new-graph:
	@echo "Creating graph component at ./knex/graphs/$$name.py"; \
	sed -e "s/THE_NAME/$$name/g" ./templates/create-graph-component.py > ./knex/graphs/$$name.py; \
	echo "\nfrom $$name import *" >> ./knex/graphs/__init__.py

test-graph:
	@python3.12 ./test-graph-component.py "$$text" $$list

analyze:
	@python3.12 ./test-analyze.py "$$text"