

# This prompt is used to extract information from a given text
prompt_system_extraction = """
You are an expert extraction algorithm.
From the context, answer the user query, and wrap the output in ```json and ``` tags.
Dates should be formated as such: yyyy.mm.dd, or yyyy.mm.00 or yyyy.00.00.
Information should not be modified (languages, names, etc): they should be retrieved as they appear in the text.
{format_instructions}.

Context:
{text}
""".strip()


# This prompt is used in the verification chain, to verify information from a given text
prompt_system_verification = """
You are an expert verificator.
From the context, answer the user query using 'True' or 'False'.
Your answer should be a single word.

Context:
{text}
""".strip()

