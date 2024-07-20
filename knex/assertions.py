import gmpykit as kit
from knex.constants.prompt import prompt


def get_assertions(raw_text: str, ollama_url='http://localhost:11434/api/generate', model_name='llama3'):
    """
    Extract the assertions from the raw text using the LLM running on an Ollama server, and the predefined prompt.

    Args:
    - raw_text (string): The initial text to get assertion from
    - ollama_url (string): The Ollama server URL the LLM is going to be asked from
    - model_name (string): which model is going to be queried.
    """

    # From the prefefined prompt, we replace only the needed part
    prompt = __build_prompt(raw_text)

    # Ask the LLM
    llm_answer = kit.ask_llm(prompt, ollama_url, model_name)

    # Adapt LLM answer: remove head of the line like "1. blahblah"
    assertions = [line[line.find(' ') + 1:] for line in llm_answer.split('\n')]

    return assertions



def __build_prompt(input_text):
    return prompt.replace('[INPUT_TEXT]', input_text)