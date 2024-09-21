.DEFAULT_GOAL := help

help:
	@echo "make save            -> Git add, commit, push to master (message: 'save with make command')"
	@echo "make install         -> Clean, build and locally install the package"
	@echo "make update-ontology -> Update the ontology file in the constant folder, according to OntoMe"
	@echo "make llmlog          -> Launch a reverse proxy in between. Ollama base URL needs to be set to: base_url='http://127.0.0.1:5000'"

save:
	@git add .
	@git commit -m "save with make command"
	@git push origin main

clean:
	@rm -rf ./build
	@rm -rf ./dist
	@rm -rf ./knex.egg-info

build:
	@python3 setup.py sdist bdist_wheel

install-local:
	@pip install -e .
	@python3.10 -m pip install -e .
	
install: clean build install-local


update-ontology:
	@python3.10 ./scripts/update-ontology.py


llmlog:
	@python3.10 ./scripts/llm-logging.py