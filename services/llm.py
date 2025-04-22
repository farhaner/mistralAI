# import requests

# def ask_mistral(prompt: str) -> str:
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": "mistral", "prompt": prompt}
#     )
#     return response.json()["response"]


# Contoh kedua

import requests

def ask_mistral(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "")
    else:
        return "Error from LLM: " + str(response.text)
