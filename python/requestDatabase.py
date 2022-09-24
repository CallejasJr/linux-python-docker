from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "status": 200,
        "description": "Estoy vivo",
        "body": {}
    }

@app.get("/params")
def params(number: int):
    with open("students.txt", "r") as file:
        students = file.readlines()
        file.close()

    for i in range(len(students)):
        students[i] = students[i].replace("\n","")  

    try:
        response = students[number]
        status = 200
        description = ""
    except IndexError:
        response = ""
        status = 400
        description = "No existe estudiantes en esa posicion"

    return {
        "status": status,
        "description": description,
        "body":{
            "student": response
        }
    }

