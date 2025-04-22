# from fastapi import FastAPI
# from pydantic import BaseModel
# import requests

# app = FastAPI()

# class Prompt(BaseModel):
#     prompt: str

# @app.post("/ask")
# def ask_mistral(data: Prompt):
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": "mistral", "prompt": data.prompt}
#     )
#     return {"response": response.json()["response"]}


# Contoh Kedua 

from fastapi import FastAPI
from pydantic import BaseModel
from services.llm import ask_mistral

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    prompt: str
    response: str

@app.post("/ask", response_model=PromptResponse)
def ask_question(req: PromptRequest):
    result = ask_mistral(req.prompt)
    return {"prompt": req.prompt, "response": result}
