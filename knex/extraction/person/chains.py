from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

from .model import Person
from ...globals import ollama_base_url, model_name
from ...tools import obj_validation

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



######################################
#### CHAIN 2: Extract information ####
######################################

# Chain element: Parser
parser = PydanticOutputParser(pydantic_object=Person)

# Chain element: Prompt
extracting_prompt = ChatPromptTemplate.from_messages([
        ("system",
            "You are an expert extraction algorithm. "
            "From the context, answer the user query, and wrap the output in ```json and ``` tags. "
            "Dates should be formated as such: yyyy.mm.dd, or yyyy.mm.00 or yyyy.00.00. "
            "{format_instructions}.\n\n"
            "Context:\n{text}"
        ),
        ("human", "What information do we know about {person_name}?")
]).partial(format_instructions=parser.get_format_instructions())

# Build the chain
extraction_chain = extracting_prompt | llm | parser | obj_validation



###############################################
#### CHAIN 3: Verify extracted information ####
###############################################

# Chain element: Prompt
verification_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are an expert verificator. "
            "From the context, answer the user query using 'True' or 'False'. "
            "Your answer should be a single word.\n"
            "Context:\n{text}"
        ),
        ("human", 
            "Is the assertion '{assertion}' true? "
            "If it is not clearly known, the answer should be 'False'"
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