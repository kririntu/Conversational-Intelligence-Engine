from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question

app = FastAPI()

class UserQuery(BaseModel):
        question:str

@app.get("/")
def home():

        return { "message":"RAG API running" }

@app.post("/chat")

def chat(data:UserQuery):

        result = ask_question(data.question)

        return {"response":result}


