prompt = """
Provide me all statements you understand from the following text. 
Be exhaustive and explicit. 
Never use pronouns.
Dates should have the following format: day.month.year (eg 31.12.2000).
Your answer should be a list of short phrases about a single fact.

Examples:
- John Doe is the son of Martin
- John Doe married Augustine in 1988
- Augustine was a Catholic
- Augustine's parents are Albert and Justine
- Albert was a general
                 
Text: "[INPUT_TEXT]"
"""

def build_prompt(input_text):
    return prompt.replace('[INPUT_TEXT]', input_text)