from typing import List
from gmpykit import print_object

from .model import Occupations, get_assertions
from .chains import list_person_chain, extraction_chain, verification_chain



def extract_occupations(text: str, verify: bool, verbose) -> Occupations:
    """
    Given the text, extract information about all occupation mentioned in the text.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.
    """

    all_occupations = []

    # Get all persons from the text
    persons_names = list_person_chain.invoke({'text': text})
    if verbose: print("Persons found in the text:", ', '.join(persons_names))

    # Extract information about all persons
    for person_name in persons_names:

        # Extract the information
        if verbose: print("\nExtracting occupations of:", person_name)
        person_occupations = extraction_chain.invoke({'person_name': person_name, 'text': text})
        if verbose: print_object(person_occupations)

        # Verify extracted information
        if verify: 
            __verify(text, person_occupations, verbose)

        all_occupations.append(person_occupations)

    return all_occupations



def __verify(text: str, occupations: Occupations, verbose: bool):
    """
    Given the text and the extracted information, ask the LLM for each information
    if it is true or not. 
    TODO: in case llm answer it is wrong, diretly update the object
    """

    # Get the person assertions
    assertions = get_assertions(occupations)

    # Verify each assertion
    if verbose: print('\nVerifications:')
    for assertion in assertions:
        verification = verification_chain.invoke({'text': text, 'assertion': assertion})
        # If a verification turns out to be wrong, it has to be printed anyway
        if verbose or not verification: 
            print('>> ' + assertion + ' ---> ' + str(verification))

    return occupations