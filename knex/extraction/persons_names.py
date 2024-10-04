from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_core.runnables import RunnableLambda

from .chain.llm import get_chain_elt_llm
from .chain.verification import verify_assertions


# ----------------------------------------------------

# The instance of the lang chain
chain = None


def init_chain_person_names():
    """Initiate the person names chain"""
    global chain, list_person_prompt, transform
    chain = list_person_prompt | get_chain_elt_llm() | transform


def extract_names(text: str, verify: bool, verbose: bool) -> List[str]:
    """
    Given the text, fetch all the person names in it.
    If the option is set, make a second call to LLM to check the truthfulness of extracted information.

    Args:
        text (str): The text to extract information from.
        verify (bool): Either of not each information need to be verified with an additional LLM query.
        verbose (bool): Either or not display logs.

    Returns:
        List[str]: The list of persons names that has been found in the text
    """
    global chain

    persons_names = chain.invoke({'text': text})
    if verbose: print("Persons found in the text:", ', '.join(persons_names))

    if verify:
        assertions = list(map(lambda name: f'Person {name} is mentioned in the text.', persons_names))
        persons_names = verify_assertions(text, assertions, verbose)

    return persons_names

# ----------------------------------------------------


# Chain element: Prompt
list_person_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            'List all the persons named in the text given by the user. '
            'Your answer should look like: "Person1, Person2, Person3"'
        ),
        ("human", "{text}")
])


def __transform_to_list(answer: AIMessage) -> List[str]:
    """Transform the LLM answer into a list of string"""
    text = answer.content
    names = list(map(lambda name: name.replace('.', ' ').strip(), text.split(',')))
    return names

# Make a langchain element
transform = RunnableLambda(__transform_to_list)