import os
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


# Define the LLM used in all chains
llm = None

def init_chain_elt_llm(source: str, model: str, url: str = ''):
    """
    Replace the default ollama llm by another one

    Args:
        source (str): the source of the LLM: 'ollama', 'openai'
        url (str): the url of the llm
        model (str): the model name (eg 'llama3.1', 'gpt-4o-mini')
    """
    global llm
    
    if source == 'ollama':
        llm = ChatOllama(model=model, temperature=0, base_url=url)

    if source == 'openai':
        llm = ChatOpenAI(model=model, temperature=0, api_key=os.getenv('OPENAI_API_KEY'))


def get_chain_elt_llm():
    """Return the LLM. Need to be instanciated first."""
    global llm
    return llm