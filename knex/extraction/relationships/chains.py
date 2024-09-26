from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

from .model import Relationships
from ...globals import ollama_base_url, model_name
from ...globals import system_prompt_extraction, system_prompt_verification
from ..tools import obj_validation

# Define the LLM used in all chains
llm = ChatOllama(model=model_name, temperature=0, base_url=ollama_base_url)



######################################
#### CHAIN 1: Extract information ####
######################################

# Chain element: Parser
parser = PydanticOutputParser(pydantic_object=Relationships)

# Chain element: Prompt
extracting_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt_extraction),
        ("human", "What information do we know about {person_name} relationships? Avoid parent-child relations.")
]).partial(format_instructions=parser.get_format_instructions())

# Build the chain
extraction_chain = extracting_prompt | llm | parser | obj_validation



###############################################
#### CHAIN 2: Verify extracted information ####
###############################################

# Chain element: Prompt
verification_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt_verification),
        ("human", "Is the assertion '{assertion}' true? If it is not clearly stated, the answer should be 'False'.")
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