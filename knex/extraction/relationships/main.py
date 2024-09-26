from typing import List
from gmpykit import print_object

from .model import Relationships, Relationship, get_assertions
from .chains import extraction_chain, verification_chain


def extract_relationships(text: str, persons_names: List[str], verify: bool, verbose: bool) -> List[Relationship]:
    """
    Given the text, extract information about person's relationships found in it.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.
    """

    results = []
    # Extract information about all persons
    for person_name in persons_names:

        # Extract the information
        if verbose: print("\n=== Extracting relationships of:", person_name, "===")
        relationships = extraction_chain.invoke({'person_name': person_name, 'text': text})
        if verbose: print_object(relationships)

        # Verify extracted information
        if verify:
            relationships = __verify(text, relationships, verbose)
        
        results += relationships.relationships
    return results



def __verify(text: str, relationships: Relationships, verbose: bool):
    """
    Given the text and the extracted information, ask the LLM for each information
    if it is true or not. 
    TODO: in case llm answer it is wrong, diretly update the object
    """

    # Get the person assertions
    assertions = get_assertions(relationships)

    # Verify each assertion
    if verbose: print('\nVerifications:')
    for assertion in assertions:
        verification = verification_chain.invoke({'text': text, 'assertion': assertion})
        # If a verification turns out to be wrong, it has to be printed anyway
        if verbose or not verification: 
            print('>> ' + assertion + ' ---> ' + str(verification))

    return relationships