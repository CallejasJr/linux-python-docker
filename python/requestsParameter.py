from fastapi import FastAPI

app = FastAPI()
lista = ["Mario", "Pedro", "Luis", "Camila", "Rosa"]

@app.get("/")
def health():
    return {
        "status": 200,
        "description": "Estoy vivo",
        "body": {}
    }

@app.get("/params")
def params(number: int):
    global lista

    try:
        response = lista[number]
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

@app.post("/inputparameter")
def input_param(body_request: dict):
    global lista

    try: 
        lista.append(body_request["new_student"])
        status = 200
        description = ""
        add = "OK"
    except KeyError:
        status = 400
        description = "La llave del body request es incorrecta, debe ser new_student"
        add = "Fail"

    return {
        "status": status,
        "description": description,
        "body": {
            "add": add
        }
    }

