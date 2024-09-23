from .person import extract_person
from .occupations import extract_occupations
from .relationships import extract_relationships


def extract(text: str, extraction_type: str, verify=True, verbose=False):
    """
    Extract a dedicated topic from the given text.

    Parameters:
    text [str]: The
    """


    # Extract persons from the text
    if extraction_type.lower() == 'person':
        return extract_person(text, verify, verbose)
    
    # Extract occupations from the text
    if extraction_type.lower() == 'occupations':
        return extract_occupations(text, verify, verbose)
    
    # Extract relationships from the text
    if extraction_type.lower() == 'relationships':
        return extract_relationships(text, verify, verbose)
    


def extract_all(text: str, verify=True, verbose=False):
    persons = extract_person(text, verify, verbose)
    occupations = extract_occupations(text, verify, verbose)
    relationships = extract_relationships(text, verify, verbose)