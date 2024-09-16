from typing import List
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from ..globals import llm_name
from ..model import Assertion

# Prompt used
system_prompt = """
Your task is to get all atomic assertions from the text you will be provided with, and add the assertion main topic as described in the example.
Be explicit on the names (do not use pronouns like 'he', 'his', 'her', ...).
Give me as much assertions as possible.
Do not repeat yourself, in any kind of manner.
Dates should have the following format: day.month.year (eg 31.12.2000).
Your answers should like:
```json
{{"assertions":[
    {{"topic":"nationality","text":"John Doe was French"}}, 
    {{"topic":"birth","text":"John Doe was born in 1950 in Basel"}},
    {{"topic":"job","text":"John Doe was a carpenter"}},
    {{"topic":"family","text":"John Doe was the son of Martin"}},
    {{"topic":"family","text":"John Doe married Augustine in 1988"}},
    {{"topic":"religion","text":"Augustine was a Catholic"}},
    {{"topic":"family","text":"Augustine's parents are Albert and Justine"}},
    {{"topic":"job","text":"Albert was a general"}}
]}}
```
Make sure your answer includes the json code tag.
"""

# Chain element 1: the prompt handling
element_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), 
    ("human", "{text}")
])

# Chain element 2: asking the LLM
element_llm = ChatOllama(model=llm_name, temperature=0)


# Build the chain
chain = element_prompt | element_llm


def get_assertions(text: str) -> List[Assertion]:
    # Call the LangChain chain
    assertions_str = chain.invoke({"text": text}).content

    # Extract the JSON
    begin_index = assertions_str.index('```json') + 7
    end_index = assertions_str.index('```', begin_index)
    the_json_str = assertions_str[begin_index:end_index]
    the_json = json.loads(the_json_str)

    # Transform and return a list of Assertions
    return list(map(lambda obj: Assertion(obj['topic'], obj['text']), the_json['assertions']))