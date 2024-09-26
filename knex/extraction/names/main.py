from typing import List
from gmpykit import print_object

from .chains import list_person_chain, verification_chain


def extract_names(text: str, verify: bool, verbose: bool) -> List[str]:
    """
    Given the text, extract all persons mentioned in it.
    """

    persons_names = list_person_chain.invoke({'text': text})
    if verbose: print("Persons found in the text:", ', '.join(persons_names))

    if verify:
        persons_names = __verify(text, persons_names, verbose)

    return persons_names


def __verify(text: str, persons_names: str, verbose: bool):
    """
    Given the text and the extracted information, ask the LLM for each information
    TODO: in case llm answer it is wrong, diretly update the object
    """

    correct_persons_names = []

    for person_name in persons_names:
        verification = verification_chain.invoke({'text': text, 'person_name': person_name})
        # If a verification turns out to be wrong, it has to be printed anyway
        if verbose or not verification: 
            print('>> Person ' + person_name + ' is mentioned in the text ---> ' + str(verification))
        if verification: correct_persons_names.append(person_name)

    return correct_persons_names