from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages.ai import AIMessage
from langchain_core.runnables import RunnableLambda

from ..globals import ollama_base_url


# Chain element: Prompt
prompt = ChatPromptTemplate.from_messages([
        ("system", 'List all the persons named in the text given by the user. Your answer should look like: "Person1, Person2, Person3"'),
        ("human", "{text}")
])

# Define the LLM
llm = ChatOllama(model="llama3.1", temperature=0, base_url=ollama_base_url)


def transform_to_list(answer: AIMessage):
    text = answer.content
    names = list(map(lambda name: name.replace('.', ' ').strip(), text.split(',')))
    return names

# Make a langchain element
transform = RunnableLambda(transform_to_list)

# Build the chain
persons_chain = prompt | llm | transform