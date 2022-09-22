from typing import Union

from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

@app.get("/")
def health():
    return {
            "status": 200,
            "description": "",
            "body": {
                "message": "I am here"
            }
        }

@app.post("/parameters")
def params(body: dict):
    return {
            "status": 200,
            "description": "",
            "body": body
        }

