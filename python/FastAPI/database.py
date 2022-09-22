from turtle import st
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

@app.get("/getStudents")
def params():
    with open("students.txt", "r") as file:
        students = file.readlines()
        file.close()

    
    for idx in range(len(students)):
        students[idx] = students[idx].replace("\n","")
    
    response = {"students": students}
    return {
            "status": 200,
            "description": "",
            "body": response
        }

