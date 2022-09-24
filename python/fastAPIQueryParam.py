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
    
    lista = ["Mario", "Pedro", "Luis", "Camila", "Rosa"]

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