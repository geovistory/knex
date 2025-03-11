import math
import kit
from knex.constants.prompt import prompt


def get_assertions(raw_text: str, ollama_url='http://localhost:11434/api/generate', model_name='llama3'):
    """
    Extract the assertions from the raw text using the LLM running on an Ollama server, and the predefined prompt.

    Args:
    - raw_text (string): The initial text to get assertion from
    - ollama_url (string): The Ollama server URL the LLM is going to be asked from
    - model_name (string): which model is going to be queried.
    """

    # From the prefefined prompt, we add the needed part
    loc_prompt = prompt + f'\n\nText: "{raw_text}"'

    # Ask the LLM
    llm_answer = kit.ask_ollama(loc_prompt, ollama_url, model_name)
    llm_answer = llm_answer.replace('\n\n', '')

    # Adapt LLM answer: remove head of the line like "1. blahblah"
    lines = llm_answer.split('\n')
    lines = lines[1:]
    assertions = [line[line.find(' ') + 1:] for line in lines]

    return assertions



def get_assertion_large_text(raw_text: str, ollama_url='http://localhost:11434/api/generate', model_name='llama3', chunk_size=1000, overlap_size=200):

    # Get the main subject of the text
    main_subject = kit.ask_ollama(f'Who or what is the main subject of the following text: "{raw_text}". Answer with the sentence: "The text is about [REPLACE]".')

    # Split the large text into pieces
    pieces_nb = math.ceil(len(raw_text) / chunk_size)
    pieces = []
    for i in range(0, pieces_nb):
        start = max(0, i * chunk_size - overlap_size)
        end = i * chunk_size + chunk_size + overlap_size
        pieces.append(raw_text[start:end])

    # Loop on the pieces to get all assertions
    assertions = []
    for piece in pieces:
        # From the prefefined prompt, we add the needed part
        loc_prompt = prompt + f'\n\nThe text is an extract of a bigger text about {main_subject}.\nExtract: "{piece}"'

        # Ask the LLM
        llm_answer = kit.ask_llm(loc_prompt, ollama_url, model_name)
        llm_answer = llm_answer.replace('\n\n', '')

        # Adapt LLM answer: remove head of the line like "1. blahblah"
        lines = llm_answer.split('\n')
        lines = lines[1:]
        piece_assertions = [line[line.find(' ') + 1:] for line in lines]

        # DEBUG
        # print("> PIECE")
        # print(piece)
        # print("> PROMPT")
        # print(loc_prompt)
        # print("> ASSERTIONS")
        # for assertion in piece_assertions:
        #     print(assertion)

        assertions += piece_assertions

    return assertions