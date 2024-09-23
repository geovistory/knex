from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

from .model import Relationships
from ..globals import ollama_base_url, model_name
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
        ("system",
            "You are an expert extraction algorithm. "
            "From the context, answer the user query, and wrap the output in ```json and ``` tags. "
            "Dates should be formated as such: yyyy.mm.dd, or yyyy.mm.NA or yyyy.NA.NA. "
            "{format_instructions}.\n\n"
            "Context:\n{text}"
        ),
        ("human", 
            "Extract all relationships between 2 persons from the context."
        )
]).partial(format_instructions=parser.get_format_instructions())

# Build the chain
extraction_chain = extracting_prompt | llm | parser | obj_validation



###############################################
#### CHAIN 2: Verify extracted information ####
###############################################

# Chain element: Prompt
verification_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are an expert and strict verificator. "
            "From the context, answer the user query using 'True' or 'False'. "
            "Your answer should be a single word.\n"
            "Context:\n{text}"
        ),
        ("human", 
            "Is the assertion '{assertion}' true? "
            "If it is not clearly known or said, the answer should be 'False'"
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