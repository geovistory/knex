# Knowledge Extractor (KnEx)

## Introduction

Before this library, to construct a knowledge graph from raw text (eg. historical texts), one had two solutions. First solution was to manually read, understand, write and insert the graph into a data silo, like a triple store.
The other solution was to pay hundreds hours of development in order to make NLP based on a particular corpus in order to gather all the information in it and pour them in the right triple store. Afterwards, all this code could be thrown to waste, the corpus being already taken care of.

Meet KnEx, an automated knowledge extractor, for any corpus of data, extracting a strict, reusable and scientifically developed and accepted ontology: [OntoMe](https://ontome.net/).
The main advantage of KnEx is that the code is written. For any corpus. 
KnEx outputs are multiple, it can be:
- Triples in form of text
- Triples in form of dataset (Spreadsheets or directly inserted in databases)
- RDF triples in a file
- RDF triples poured in a SPARQL endpoint
- Visualizations, like HTML pages or simply images.


## How it works (headlines) ?

- Given raw text is reformulated (by a LLM)
- Entities and word roles are identified inside the reformlated strings (NLP techniques)
- The graph is built, following the ontology


## How it works (detailed) ?

- KnEx get the raw text to extract knowledge from.
- A LLM is asked to rephrase each given text from the corpus in a more usable (understand 'NLP parsable') way: give a list, the most complete possible, of particle assertions understood from the initial text. To do that, some prompt engineering is done.
- Run a *spaCy* pipeline (the default ones plus those created in this library) on the assertions to get lemmas, POS, NER, ... 
- Run NLP algorithm to build a graph between the identified entities, based on *spaCy* pipeline results. Handle the fact that an entity can be multiple times identified in the assertions: reasonably handle duplicated entities (only inside the same text) 
- Return the assertions, parsed knowledge graph and some feedback strings


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


## How to use ?

## How to develop ?

Add a new part of the ontology to the library:
- Get everything ready:
    - The example text as a string
    - The example ontology as a CSV (or DataFrame)
- Define the needs:
    - Are they new classes that need to be identified in the text (eg. a Religion)? Is this class already parsed, and needs to be complemented (like added in the class white list) or is it new for the library?
    - Is the graph to be build all new? Or can/should it be added to an existing graph? eg: Adding a mother to a birth can be added when parsing the Birth, or when parsing the Person, or even be a new file.
- Use make tool (`make help`), and focus on `dev` commands


- Tests are made from test text to see if they are correctly knexed

## Next feature

- Completiveness using the feedbacks