prompt = """
Provide me with all atomic assertions from the following text, and add the assertion main topic as described in the example.
Be explicit on the names (do not use pronouns like 'he', 'his', 'her', ...).
Give me as much assertions as possible.
Do not repeat yourself, in any kind of manner.
Dates should have the following format: day.month.year (eg 31.12.2000).
Do not be verbose, here is what your answer should look like:
"Atomic assertions:
- John Doe was French -> nationality
- John Doe was born in 1950 in Basel -> birth
- John Doe was a carpenter -> job
- John Doe was the son of Martin -> family
- John Doe married Augustine in 1988 -> family
- Augustine was a Catholic -> religion
- Augustine's parents are Albert and Justine -> family
- Albert was a general -> job"
"""

# Old prompt from v0, used with mistral
# prompt = """
# Provide me all statements you understand from the following text. 
# Be exhaustive and explicit. 
# Never use pronouns.
# Dates should have the following format: day.month.year (eg 31.12.2000).
# Your answer should be a list of short phrases about a single fact.

# Examples:
# - John Doe is the son of Martin
# - John Doe married Augustine in 1988
# - Augustine was a Catholic
# - Augustine's parents are Albert and Justine
# - Albert was a general
                 
# Text: "[INPUT_TEXT]"
# """