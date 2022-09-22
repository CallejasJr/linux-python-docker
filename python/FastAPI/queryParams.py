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

@app.get("/parameters")
def params(name: str):
    return {
            "status": 200,
            "description": "",
            "body": {
                "name": name
            }
        }

@app.get("/parameters")
def params(age: int = None, name: str=Query(..., example="Tom", title="User name", description="This is the user name")):
    return {
            "status": 200,
            "description": "",
            "body": {
                "name": name
            }
        }

