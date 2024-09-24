from typing import List
from gmpykit import print_object

from .model import Person, get_assertions
from .chains import list_person_chain, extraction_chain, verification_chain


def extract_persons(text: str, verify: bool, verbose) -> List[Person]:
    """
    Given the text, extract information about all persons found in it.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.
    """

    results = []

    # Get all persons from the text
    persons_names = list_person_chain.invoke({'text': text})
    if verbose: print("Persons found in the text:", ', '.join(persons_names))

    # Extract information about all persons
    for person_name in persons_names:

        # Extract the information
        if verbose: print("\nExtracting information about:", person_name)
        person = extraction_chain.invoke({'person_name': person_name, 'text': text})
        if verbose: print_object(person)

        # Verify extracted information
        if verify:
            person = __verify(text, person, verbose)
        
        results.append(person)
    return results



def __verify(text: str, person: Person, verbose: bool):
    """
    Given the text and the extracted information, ask the LLM for each information
    if it is true or not. 
    TODO: in case llm answer it is wrong, diretly update the object
    """

    # Get the person assertions
    assertions = get_assertions(person)

    # Verify each assertion
    if verbose: print('\nVerifications:')
    for assertion in assertions:
        verification = verification_chain.invoke({'text': text, 'assertion': assertion})
        # If a verification turns out to be wrong, it has to be printed anyway
        if verbose or not verification: 
            print('>> ' + assertion + ' ---> ' + str(verification))

    return person