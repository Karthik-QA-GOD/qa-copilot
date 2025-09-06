from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class Requirement(BaseModel):
    text: str

@app.post("/generate_testcases")
async def generate_testcases(req: Requirement):
    # For now return mock response
    return {
        "requirement": req.text,
        "testcases": [
            "Given user is on login page",
            "When user enters valid username and password",
            "Then user should be redirected to dashboard"
        ]
    }
