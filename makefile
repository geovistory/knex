.DEFAULT_GOAL := help

SHELL := /bin/bash
PYTHON := python3.10
PIPENV_NAME := pipenv_logre
REQUIREMENTS_FILE := requirements.txt

help:
	@echo "make save            -> Git add, commit, push to master (message: 'save with make command')"
	@echo "make install         -> Download all dependencies"
	@echo "make update-ontology -> Update the ontology file in the constant folder, according to OntoMe"
	@echo "make llm-proxy       -> Launch a reverse proxy in between. Ollama base URL needs to be set to: base_url='http://127.0.0.1:5000'"
	@echo "make start-gui       -> Start a Streamlit app with the Knex GUI"

install:
	$(PYTHON) -m pip install streamlit 


llm-proxy:
	$(PYTHON) ./scripts/reverse-proxy-llm.py


start-gui:
	@cd knex-gui; \
	$(PYTHON) -m streamlit run server.py