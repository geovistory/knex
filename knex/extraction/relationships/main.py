from gmpykit import print_object

from .model import Relationships, get_assertions
from .chains import extraction_chain, verification_chain



def extract_relationships(text: str, verify: bool, verbose) -> Relationships:
    """
    Given the text, extract information about all relationships mentioned in the text.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.
    """

    # Extract informations
    if verbose: print("\nExtracting relationships")
    relationships = extraction_chain.invoke({'text': text})
    if verbose: print_object(relationships)

    # Verify extracted information
    if verify: 
        __verify(text, relationships, verbose)

    return relationships



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