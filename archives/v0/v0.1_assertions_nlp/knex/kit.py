import requests
import json


def ask_ollama(prompt, server_url="http://localhost:11434/api/generate", model_name="llama3.1"):
    response = requests.post(server_url, json={"model": model_name, "prompt": prompt, "options": {"temperature": 0}})
    text = response.text.strip()
    lines = text.split("\n")
    tokens = list(map(lambda line: json.loads(line)["response"], lines))
    formated = "".join(tokens)
    answer = formated.strip()
    return answer


def to_camel_case(text):
    output = "".join(x for x in text.title() if x.isalnum()).replace("'", "")
    return output[0].lower() + output[1:]