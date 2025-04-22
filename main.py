from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/ask")
def ask_mistral(data: Prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": data.prompt}
    )
    return {"response": response.json()["response"]}
