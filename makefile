.DEFAULT_GOAL := help

help:
	@echo "make save            -> Git add, commit, push to master (message: 'save with make command')"
	@echo "make install         -> Download all dependencies"
	@echo "make update-ontology -> Update the ontology file in the constant folder, according to OntoMe"
	@echo "make llm-proxy       -> Launch a reverse proxy in between. Ollama base URL needs to be set to: base_url='http://127.0.0.1:5000'"
	@echo "make start-gui       -> Start a Streamlit app with the Knex GUI"


save:
	@git add .
	@git commit -m "save with make command"
	@git push origin main


install:
	@cd ..; git clone https://github.com/gaetanmuck/gmpykit.git
	@poetry install


update-ontology:
	@python3.10 ./scripts/update-ontology.py


llm-proxy:
	@python3.10 ./scripts/reverse-proxy-llm.py


start-gui:
	@cd knex-gui; \
	python3.10 -m streamlit run server.py