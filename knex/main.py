from .chains import persons_chain, person_chain, persons_prompt, person_prompt, verification_person_chain

from gmpykit import print_object

def get_prompts(text, extraction_type='person'):
    if extraction_type == 'person':
        prompt1 = persons_prompt.invoke({'text': text})
        prompt2 = person_prompt.invoke({'person_name': 'PERSON_NAME', 'text': text})

        prompt1_ = ''
        for msg in prompt1.messages:
            prompt1_ += msg.content + '\n'

        prompt2_ = ''
        for msg in prompt2.messages:
            prompt2_ += msg.content + '\n'

        return prompt1_, prompt2_


def extract(text, extraction_type='person', verbose=False):
    if extraction_type == 'person':
        results = []
        
        # Get the list of person in the text
        persons_names = persons_chain.invoke({'text': text})
        if verbose: print("Persons found in the text:", ', '.join(persons_names))

        # Extract information about all persons
        for person_name in persons_names:
            if verbose: print("\nExtracting information about:", person_name)
            person = person_chain.invoke({'person_name': person_name, 'text': text})
            person.validate()
            if verbose: print_object(person)
            person = verify(person, text, extraction_type, verbose)
            results.append(person)
        return results
    

def verify(result, text, extraction_type='person', verbose=False):

    # Select the right chain
    if extraction_type == 'person':
        verification_chain = verification_person_chain

    # Get the assertions
    assertions = result.get_assertions()

    # Verify each assertion
    if verbose: print('\nVerification:')
    for assertion in assertions:
        if verbose: print('>> ' + assertion, end=' ---> ')
        verification = verification_chain.invoke({'text': text, 'assertion': assertion})
        if verbose: print(verification)

    return result


