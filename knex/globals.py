model_name = "llama3.1"
# ollama_base_url = "http://localhost:11434" # Direct Ollama
ollama_base_url = "http://127.0.0.1:5000" # Through the reverse proxy



system_prompt_extraction = """
You are an expert extraction algorithm.
From the context, answer the user query, and wrap the output in ```json and ``` tags.
Dates should be formated as such: yyyy.mm.dd, or yyyy.mm.00 or yyyy.00.00.
Information should not be modified (languages, names, etc): they should be retrieved as they appear in the text.
{format_instructions}.

Context:
{text}
""".strip()


system_prompt_verification = """
You are an expert verificator.
From the context, answer the user query using 'True' or 'False'.
Your answer should be a single word.

Context:
{text}
""".strip()