from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

from ...globals import ollama_base_url, model_name
from ...globals import system_prompt_verification


# Define the LLM used in all chains
llm = ChatOllama(model=model_name, temperature=0, base_url=ollama_base_url)



#######################################
#### CHAIN 1: List person names ####
#######################################

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

# Build the chain
list_person_chain = list_person_prompt | llm | transform


###############################################
#### CHAIN 2: Verify extracted information ####
###############################################

# Chain element: Prompt
verification_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt_verification),
        ("human", 
            "Is the person {person_name} mentioned in the text? "
            "If it is not clearly stated, the answer should be 'False'"
        )
])

# Verify the format
def __verification(answer: AIMessage) -> bool:
    text = answer.content
    if text.lower().startswith('true'): return True
    if text.lower().startswith('false'): return False
    raise Exception(f'ERROR IN VERIFICATION FUNCTION:\n{text}')

# Make a langchain element
verification = RunnableLambda(__verification)

# Build the chain
verification_chain = verification_prompt | llm | verification