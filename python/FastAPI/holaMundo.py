from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {"body": "Hello World"}
