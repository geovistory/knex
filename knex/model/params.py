from typing import List


class Params:

    # Whether or not print debug logs
    debug: bool
    
    # If developer only wants to debug some parts
    debug_list: List[str]

    # Whether or not ask the LLM to reparse the input string
    ask_llm: bool

    # The Ollama server api route to call to ask LLM
    ollama_url: str

    # The model name (inside Ollama) to query
    llm_name: str

    # Whether or not create the html visuals from the graph
    visual: bool

    # If visuals should be created, the path where to store the file
    visual_path: str