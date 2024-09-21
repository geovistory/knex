from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda

from ..data_model import Person
from ..globals import ollama_base_url


# Chain element: Parser
parser = PydanticOutputParser(pydantic_object=Person)

# Chain element: Prompt
prompt = ChatPromptTemplate.from_messages([
        ("system",
                   "You are an expert extraction algorithm. "
                   "From the context, answer the user query, and wrap the output in ```json and ``` tags. "
                   "It is important that you do no provide unspecified information. " 
                   "Dates should be formated as such: yyyy.mm.dd. "
                   "{format_instructions}.\n\n"
                   "Context:\n{text}"
        ),
        ("human", "What information do we know about {person_name}?")
]).partial(format_instructions=parser.get_format_instructions())

# Define the LLM
llm_extraction = ChatOllama(model="llama3.1", temperature=0, base_url=ollama_base_url)

# Build the chain
person_chain = prompt | llm_extraction | parser





# Verification chain

verification_prompt = ChatPromptTemplate.from_messages([
        ("system", 
                "You are an expert verificator. "
                "From the context, answer the user query using \"True\" or \"False\". "
                "Your answer should be a single word.\n"
                "Context:\n{text}"
        ),
    ("human", "Is the assertion \"{assertion}\" true? If it is not clearly known, the answer should be \"False\"")
])

# Define the LLM
llm_verification = ChatOllama(model="llama3.1", temperature=0, base_url=ollama_base_url)


# Validate the format
def validate_verification(answer: AIMessage):
    text = answer.content
    if text.lower().startswith('true'): return True
    if text.lower().startswith('false'): return False
    print('ERROR')
    print(text)

# Make a langchain element
validate = RunnableLambda(validate_verification)


verification_person_chain = verification_prompt | llm_verification | validate