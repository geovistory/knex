# Knex - Knowledge Extraction


## Get Started

1. Download this repo: `git clone https://github.com/kleiolab/knex.git`
2. Jump in the downloaded folder: `cd knex`
3. Install dependencies: `make install`
4. Read this `README.md`
5. Start the gui (optional) `make start-gui`


## Introduction

Knex is a project that aims to extract information from raw text and model it into a strict ontology.

The current version consists of two parts:
- A Python library that "does the work", allowing developers to extract information from text, process corpora, run batches, etc.
- A web GUI that embeds the Python library, enabling non-developers to do the same, but also to visualize results, edit the graph, and manage it (reconcile, upload, fetch other data, etc.).

## Part 1: The Python Library and How It Works

### Extraction

Given raw text, the library will execute a chain of actions using LLMs and modeled classes to generate instances of those classes.

For example, it is defined that a Person has a birth date and a birthplace (i.e., the class Person has two attributes with dedicated descriptions, used to explain to the LLM). The LLM is then asked to extract this information from the text, and through the chain of actions (LangChain), the result is a list of Person instances with "real" attributes, filled by the chain.

This step is the most resource-intensive in terms of computing, cost, and development. As an example, estimating the extraction of Persons, Relationships, and Occupations for 25,000 people from the HLS would cost around $250 using OpenAI’s API, with GPT-4o and approximately 2.5 days of computation.

Using OpenAI is not mandatory, as there are other powerful open-source LLMs on Hugging Face (like Llama 3.1-405B, currently the highest-rated open-source model, source: [Chatbot Arena](https://lmarena.ai/)). However, there are hardware requirements for running such models.

During development, the smaller local Llama 3.1-7B was used instead of the larger GPT-4o, already yielding promising results. However, the limitations of this model became apparent (expressing the output in the desired format is complex and heavy). For example, it struggled to understand that a woman was not married to her father, likely due to the raw text format not being as verbose as it was trained on (the text was: "… Marié(e) à Suzanne Mina Arnoux, Française, fille de Jules Cyprien …"). It might be a good idea to test the extraction with an intermediate model like Llama 3.1-70B and compare the graphs produced by all three models.

A test on 140 random individuals from the HLS (using GPT-4o) has been conducted and is currently being analyzed.

### Knowledge

Once the instances of all classes have been extracted, the information needs to be transformed and parsed into knowledge, respecting an ontology. The ontology used here is from [OntoMe](https://ontome.net/), the same as the one used in Geovistory.

The class attributes are essentially property paths. For example, the class Person has an attribute named birth_date, which is actually the path: `Person < brought into life < Birth > at some time within > birth date`.
To build the graph, such property paths need to be expanded and reconciled locally (both birth_date and birth_place require a birth event, which is actually the same instance). For now, local reconciliation is done through entity labels (set at creation) and class type.

Each property path must be manually developed (unfold) using the ontology and the class attributes.

Once these property paths are expanded, everything can be placed in a graph (entities + triples), which can then be exported as a spreadsheet (CSV), as interactive graph visualizations, or even merged with multiple graphs.


## Part 2: The GUI and Its Features

Alongside the Python library, a GUI ha  s been developed using the [Streamlit](https://ontome.net/) package. The goal of this GUI is to allow non-technical users to use the library, but also to make it more ergonomic for everyone to work with, test the library, edit graphs, and export extractions into defined silos (Geovistory, SPARQL endpoints).

It is divided into three main sections:
1. **GUI Introduction**: Provides a brief presentation, introduces the extracted model, and shows how class attributes are described to the LLM for the extraction process.
2. **Knowledge Extraction**: Allows users to load a graph from disk, create a graph from raw text, and explore it (through triples and visualizations).
3. **LOD**: Enables the addition of data from external sources, reconciliation, and exporting the graph to SPARQL endpoints or Geovistory.

An additional section provides sample data for the user: a list of all cleaned records from the HLS.


## Future Features

### New Features for v1

- *Reconciliation against Geovistory data*: Given the graph, Knex would query Geovistory and try to find similar entities with a certain degree of confidence. Users would then have the option to validate or discard a reconciliation. Although there are serious leads on how to approach this, the theory/technique is still undecided (potential approaches include triples embedding, entity embeddings, graph similarities, property weights, etc.). For this version of the project, one quick way to reconcile the data would be to do it manually (since currently only Persons, Relationships, and Occupations are extracted). By manually, it means developing a script with hardcoded rules.
- *Export into Geovistory*: Before directly importing data into a Geovistory project, they would need to be reconciled first.
- *Export into a SPARQL endpoint*: Additionaly of exporting data to Geovistory, the GUI could also upload it to a SPARQL endpoint, enabling the user to perform more advanced operations on a "real" graph (perhaps with the LORD tool).

### New Features for v2

- *Add data from Wikidata, DBpedia, DNB, BNF, etc.*: This feature would have a dedicated page where setting *a same as URI* property to an entity would allow fetching data from external silos, with the option to import knowledge. Although useful, this feature would require significant effort, as not all silos use the same ontology, so ontologists would need to map properties from each silo.
- *Extract only micro profiles from raw texts*: Currently, extracted information is hard-coded (e.g., Person attributes are predefined). A future version of Knex could allow users to select a list of micro profiles to extract from the text, focusing on what is needed and speeding up the extraction process while reducing costs (fewer irrelevant tokens sent to the LLM).
- *Import regular CSVs into Geovistory or SPARQL endpoints*: Since the library is split into two separate parts, the second part could also be used to model and import semi-structured data. The idea is to provide a spreadsheet, specify the graph and column mapping, and then import it (with reconciliation) into Geovistory, LORD, or a SPARQL endpoint.

### Features for LORD

Because Knex could work well with the LORD tool, here are some feature ideas for how they could complement each other:

- Interact with data via a RAG: Since the loaded data may be relatively small, a RAG (Retrieval-Augmented Generation) could be applied, allowing users to interact with the data. The utility of this feature within the Knex GUI is debatable, so it may be more appropriate for the LORD tool.
- Store the graph in a database: Since the data is relatively simple (ontology, entities, and triples), it could be stored in a database (e.g., PostgreSQL) instead of in memory, allowing for embeddings and potential reconciliation. This idea needs further consideration and may be more suitable for the LORD tool.


## Version History

### v0:

POC using LLM to extract atomic assertions from texts and applying classic NLP on those assertions to build the graph. Was based on prompt engineering and spaCy.

### v1 (current version):

- Extraction: LLM chains to extract class instances from raw texts.
- Knowledge: Build the graph from class instances.
- GUI: Allows users to visualize, correct, and upload the results.

### v2 (to be developed):

- Add the ability to import data from external silos.
- Make extraction more flexible.
- Import semi-structured data into data silos.
