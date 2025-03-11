from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from ..schema.person import Person, get_person_assertions
from ..constants import prompt_system_extraction
from .chain.obj_validation import get_chain_elt_validation
from .chain.llm import get_chain_elt_llm
from .chain.verification import verify_assertions


# ----------------------------------------------------


def print_object(obj, heading="", key=""):
    """Print out an object with indentation."""

    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        print(heading + key + ": " + str(obj))

    elif isinstance(obj, list):
        for i, elt in enumerate(obj):
            print(heading + key + " " + str(i) + ": ")
            print_object(elt, heading + "    ")

    elif isinstance(obj, dict):
        for key, value in obj.items():
            print_object(heading=heading, key=key, obj=value)

    elif obj:
        print_object(obj.__dict__, heading)

# ----------------------------------------------------

# The instance of the lang chain
chain = None


def init_chain_persons():
    """Initiate the person chain"""
    global chain, extracting_prompt, parser
    chain = extracting_prompt | get_chain_elt_llm() | parser | get_chain_elt_validation() 


def extract_persons(text: str, persons_names: List[str], verify: bool, verbose: bool) -> List[Person]:
    """
    Given the text, extract information about persons.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.

    Args:
        text (str): The text to extract information from.
        person_names (List[str]): The list of person present in the text.
        verify (bool): Either of not each information need to be verified with an additional LLM query.
        verbose (bool): Either or not display logs.

    Returns:
        List[Person]: The list of Person that has been found in the text
    """
    global chain

    results = []
    # Extract information about all persons
    for person_name in persons_names:

        # Extract the information
        if verbose: print("\n==== Extracting information about:", person_name, "====")
        person = chain.invoke({'person_name': person_name, 'text': text})
        if verbose: print_object(person)

        # Verify extracted information
        if verify:
            assertions = get_person_assertions(person)
            person = verify_assertions(text, assertions, verbose)
        
        results.append(person)
    return results

# ----------------------------------------------------


# Chain element: Parser
parser = PydanticOutputParser(pydantic_object=Person)


# Chain element: Prompt
extracting_prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_system_extraction),
        ("human", "What information do we know about {person_name}?")
]).partial(format_instructions=parser.get_format_instructions())