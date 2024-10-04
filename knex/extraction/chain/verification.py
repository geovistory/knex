from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_core.runnables import RunnableLambda

from ...constants import prompt_system_verification
from .llm import get_chain_elt_llm


# ----------------------------------------------------

# The instance of the lang chain
chain = None


def init_chain_verification():
    """Initiate the verification chain, with the instantiated llm"""
    global chain, verification_prompt, verification
    chain = verification_prompt | get_chain_elt_llm() | verification


def verify_assertions(text: str, assertions: List[str], verbose: bool) -> None:
    """
    Given the text and assertion, ask the LLM for each information if it is true or not. 
    """
    global chain

    # Verify each assertion
    if verbose: print('\nVerifications:')
    for assertion in assertions:
        verification = chain.invoke({'text': text, 'assertion': assertion})
        # If a verification turns out to be wrong, it has to be printed anyway
        if verbose or not verification: 
            print('>> ' + assertion + ' ---> ' + str(verification))

# ----------------------------------------------------


# Chain element: Prompt
verification_prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_system_verification),
        ("human", "Is the assertion '{assertion}' true? If it is not clearly stated, the answer should be 'False'.")
])


# Verify the format (function)
def __verification(answer: AIMessage) -> bool:
    text = answer.content
    if text.lower().startswith('true'): return True
    if text.lower().startswith('false'): return False
    raise Exception(f'ERROR IN VERIFICATION FUNCTION:\n{text}')

# Make a langchain element
verification = RunnableLambda(__verification)