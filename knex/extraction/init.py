from .chain.llm import init_chain_elt_llm
from .chain.obj_validation import init_chain_elt_validation
from .chain.verification import init_chain_verification
from .activities import init_chain_activities
from .person import init_chain_persons
from .persons_names import init_chain_person_names
from .relationships import init_chain_relationships

def init(source: str, model: str, url: str = ''):
    """
    Init all the extraction chains with the right model

    Args:
        source (str): the source of the LLM: 'ollama', 'openai'
        model (str): the model name (eg 'llama3.1', 'gpt-4o-mini')
        url (str): the url of the llm (if ollama server)
    """

    init_chain_elt_llm(source, model, url)
    init_chain_elt_validation()
    init_chain_verification()

    init_chain_activities()
    init_chain_persons()
    init_chain_person_names()
    init_chain_relationships()
