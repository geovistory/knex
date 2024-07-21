# Knowledge Extractor (KnEx)

## Introduction

Before this library, to construct a knowledge graph from raw text (eg. historical texts), one had two solutions. First solution was to manually read, understand, write and insert the graph into a data silo, like a triple store.
The other solution was to pay hundreds hours of development in order to make NLP based on a particular corpus in order to gather all the information in it and pour them in the right triple store. Afterwards, all this code could be thrown to waste, the corpus being already taken care of.

Meet KnEx, an automated knowledge extractor, for any corpus of data, extracting a strict, reusable and scientifically developed and accepted ontology: [OntoMe](https://ontome.net/).
The main advantage of KnEx is that the code is written. For any corpus. 
KnEx outputs are multiple, it can be:
- Triples (datasets, spreadsheets, or directly inserted in databases)
- Visualizations, like HTML pages or simply images.
- RDF triples in a file (To be developed)
- RDF triples poured in a SPARQL endpoint (To be developed)


## How it works (headlines) ?

- A given raw text is reformulated (by a LLM)
- Entities and word roles are identified inside the reformulated strings (NLP techniques)
- The graph is built, following the ontology


## How it works (more detailed) ?

- KnEx get the raw text to extract knowledge from.
- A LLM is asked to rephrase each given text from the corpus in a more usable (understand 'NLP parsable') way: give a list, the most complete possible, of particle assertions understood from the initial text. To do that, some prompt engineering is done.
- Run a *spaCy* pipeline (the default ones plus those created in this library) on the assertions to get lemmas, POS, NER, ... 
- Run NLP algorithm to build a graph between the identified entities, based on *spaCy* pipeline results. KnEx handles the fact that an entity can be identified multiple times in the assertions: reasonably deduplicates entities (first round of deduplication)
- Return the assertions, parsed knowledge graph and some feedback strings. Feedbacks are usefull to, as the word state it, give feeback to the developer (or the app) about what has been identified and what has not in the initial text.


## What is in the repository

KnEx comes as a Python package repository available privately on GitHub.

Structure:
- `knex`: source code of the library
    - `constants`: this folder defines the constant needed in the library, eg. the ontology with all the properties, the classes and their keys, or the prompt to use with the LLM.
    - `graphs`: code to concretely build the graph. Each code file is responsible to creating the correct information. This folder is ontology dependent.
    - `model`: classes (objects) definition for the library
    - `spacy_components`: regroup in a single folder all created *spaCy* components. They are for instance all specific NER components to recognize what the default *spaCy* NER does not recognize (eg. Religions)
    - `globals.py`: defines global variables to be imported from various files
    - `main.py`: regroup library features calls
- `scripts`: various scripts available from CLI, or with `make` tool (run `make help` for more information)
- `templates`: any kind of templates, mostly things that are needed in script runs
- `tests`: place to store all the library tests, in order to insure no regression, see *How to develop* for more information
- `makefile`: easy run of various things, run `make help` for more information
- `setup.py`: file required for package building, classic Pythonic file
- `spacy-cheatsheet.md`: list usefull links into the *spaCy* documentation to ease development of new components/features


## Dependencies

For usability, and to avoid code duplication, this package depends on *spaCy*, for all the NLP parts, and on *gmpykit* which is the developer personal library for redundant Python code. It is publicly available on Pypi (https://pypi.org/project/gmpykit/)


## How to use (Library API):

**Extract graph from a text**
```python
import knex

text = 'This is an example text' # Any text
graph, feedbacks = knex.extract(text)

# graph is a Pandas DataFrame that contains the full graph of the execution
# feedbacks: initial text + some information. This is usefull to see what has been parsed, and what has not.
```

**Get LLM assertions from a text**
```python
import knex

text = 'This is an example text' # Any text
assertions = knex.get_assertions(text)

# assertions is a list of string, with each element being a assertion that is in the initial text
```

**Generate HTML visuals**
```python
import knex

text = 'This is an example text' # Any text
graph, feedbacks = knex.extract(text)

html_path = './graph-visual.html'
knex.generate_visual(graph, html_path)
```


## How to develop ?

Add a new part of the ontology to the library:
- Get everything ready:
    - The example text as a string
    - The example ontology as a CSV (or DataFrame)
- Define the needs:
    - Are they new classes that need to be identified in the text (eg. a Religion)? Is this class already parsed, and needs to be complemented (like added in the class white list) or is it new for the library?
    - Is the graph to be build all new? Or can/should it be added to an existing graph? eg: Adding a mother to a birth can be added when parsing the Birth, or when parsing the Person, or even be a new file.
- Use make tool (`make help`), and focus on `dev` commands
- Once the right files has been created, development of component/graph extension can start.
- To help develop those parts, the command `make dev-spacy-analyze text=""` can be usefull: it shows what is available to make NLP on.
- When the code is written (or in the middle of development) the command `make dev-knex text="" explain="new component"` allows developer to observe the result of the written code, without being poluted with all debugs.
- Once everything works, a test in the `test` folder needs to be added, to ensure that future development, change of LLM etc will still validate this part.


## Next features

- The library, just before sending the response, could verify, with asking the llm again, if the parsing caught all the information provided in the raw text. if no, it could raise an error, return a error message, or log it in a file to inform developer. This option could be activated or deactivated.
