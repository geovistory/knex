from langchain_ollama import ChatOllama

model_name = "llama3.1"
# ollama_base_url = "http://localhost:11434" # Direct Ollama
ollama_base_url = "http://127.0.0.1:5000" # Through the reverse proxy


# Define the LLM used in all chains
llm = ChatOllama(model=model_name, temperature=0, base_url=ollama_base_url)
