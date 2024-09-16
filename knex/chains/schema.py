from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from ..globals import llm_name
from ..model import Assertion, ExtractedSchema
from ..tools import get_schema


system_prompt = """
You are an expert extraction algorithm.
Only extract relevant information from the text.
If you do not know the value of an attribute asked to extract,
return null for the attribute's value.
"""

# Chain element 1: the prompt handling
element_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{assertion}")
])

# Chain element 2: asking the LLM
element_llm = ChatOllama(model=llm_name, temperature=0)



def extract_schema(assertion: Assertion) -> ExtractedSchema | None:

    # Get the right class
    schema = get_schema(assertion.topic)
    if not schema: return None

    # Build the chain with the prompt and the right output structure
    chain = element_prompt | element_llm.with_structured_output(schema=schema)

    # Execute the chain 
    result = chain.invoke({'assertion': assertion.text})

    return result