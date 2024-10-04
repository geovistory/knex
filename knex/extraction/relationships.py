from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from gmpykit import print_object

from ..schema.relationships import Relationships, Relationship, get_relationships_assertions
from ..constants import prompt_system_extraction
from .chain.obj_validation import get_chain_elt_validation
from .chain.llm import get_chain_elt_llm
from .chain.verification import verify_assertions


# ----------------------------------------------------

# The instance of the lang chain
chain = None


def init_chain_relationships():
    """Initiate the relationships chain"""

    global chain, extracting_prompt, parser
    chain = extracting_prompt | get_chain_elt_llm() | parser | get_chain_elt_validation()


def extract_relationships(text: str, persons_names: List[str], verify: bool, verbose: bool) -> List[Relationship]:
    """
    Given the text, extract information about person's relationships.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.

    Args:
        text (str): The text to extract information from.
        person_names (List[str]): The list of person present in the text.
        verify (bool): Either of not each information need to be verified with an additional LLM query.
        verbose (bool): Either or not display logs.

    Returns:
        List[Relationship]: The list of relationship that has been found in the text
    """
    global chain

    results = []
    # Extract information about all persons
    for person_name in persons_names:

        # Extract the information
        if verbose: print("\n=== Extracting relationships of:", person_name, "===")
        relationships = chain.invoke({'person_name': person_name, 'text': text})
        if verbose: print_object(relationships)

        # Verify extracted information
        if verify:
            assertions = get_relationships_assertions(relationships)
            relationships = verify_assertions(text, assertions, verbose)
        
        results += relationships.relationships
    return results

# ----------------------------------------------------


# Chain element: Parser
parser = PydanticOutputParser(pydantic_object=Relationships)


# Chain element: Prompt
extracting_prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_system_extraction),
        ("human", "What information do we know about {person_name} relationships? Avoid parent-child relations.")
]).partial(format_instructions=parser.get_format_instructions())