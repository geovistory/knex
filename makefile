.DEFAULT_GOAL := help


help:
	@echo "\033[1mmake save\033[0m \033[3m-> Git add, commit, push to master (message: 'save with make command')\033[0m"
	@echo "\033[1mmake install\033[0m \033[3m-> Clean, build and locally install the package\033[0m"
	@echo "=== DEV PART ==="
	@echo "\033[1mmake update-ontology\033[0m \033[3m-> Update the ontology file in the constants folder, according to OntoMe\033[0m"
	@echo "\033[1mmake new-graph-component name=[COMPONENT_NAME]\033[0m \033[3m-> Create an empty graph component file, ready to be developed\033[0m"
	@echo "\033[1mmake new-ner-component name=[COMPONENT_NAME]\033[0m \033[3m-> Create an empty spaCy NER component file, ready to be developed\033[0m"
	@echo "\033[1mmake analyze text=[\"EXAMPLE TEXT\"]\033[0m \033[3m-> Run an KnEx analysis on the given text, usefull for a component's development\033[0m"
	@echo "\033[1mmake test\033[0m \033[3m-> Run all the tests in ./tests/ folder\033[0m"
	@echo "\033[1mmake knex text=[\"EXAMPLE TEXT\"] explain=[person,birth]\033[0m \033[3m-> Test the library on a given text, and debug a list of components\033[0m"

save:
	@git add .
	@git commit -m "save with make command"
	@git push origin main


################################
####### Package handling #######
################################


clean:
	@rm -rf ./build
	@rm -rf ./dist
	@rm -rf ./knex.egg-info

build:
	@python3 setup.py sdist bdist_wheel

install-local:
	@pip install -e .
	
install: clean build install-local


###############################
######### Dev helping #########
###############################


new-graph-component:
	@echo "Creating graph component at ./knex/graphs/$$name.py"; \
	sed -e "s/THE_NAME/$$name/g" ./templates/graph-component.py > ./knex/graphs/$$name.py; \
	echo -n "\nfrom .$$name import *" >> ./knex/graphs/__init__.py; \
	code ./knex/graphs/$$name.py

new-ner-component:
	@echo "Creating NER component at ./knex/spacy_components/$$name.py"; \
	sed -e "s/THE_NAME/$$name/g" ./templates/ner-spacy-component.py > ./knex/spacy_components/$$name.py; \
	echo -n "\nfrom .$$name import *" >> ./knex/spacy_components/__init__.py; \
	code ./knex/spacy_components/$$name.py

analyze:
	@python3.12 ./scripts/analyze.py "$$text"

tests:
	@python3.12 ./scripts/run_tests.py

knex:
	@python3.12 ./scripts/graph-component-test.py "$$text" $$explain

update-ontology:
	@python3.10 ./scripts/update-ontology.py