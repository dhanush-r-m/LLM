import requests
import json

# Function to query Ollama API
def query_ollama(prompt, model="llama3.1:8b"):
    url = "http://localhost:11434/api/generate"  # Ollama default server
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # disable streaming for simplicity
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data.get("response", "")
    