
# Numeros enteros
mi_numero = 20
"""
print("entero", mi_numero, "tipo", type(mi_numero))

print("sumar uno", mi_numero + 1)
print("mi numero", mi_numero)

mi_numero = mi_numero + 1
print("mi numero", mi_numero)

mi_numero -= 1
print("mi numero", mi_numero)

mi_numero_2 = 10
print("Suma de variables", mi_numero+mi_numero_2)
"""
# Numeros flotantes
mi_numero_flotante = 20.35
"""
print("flotante", mi_numero_flotante, "tipo", type(mi_numero_flotante))

print(mi_numero+mi_numero_flotante)

mi_numero_flotante_2 = 50/20
print("flotante", mi_numero_flotante_2, "tipo", type(mi_numero_flotante_2))
"""

# Cadenas de caracteres
'''
mi_string = "Hola mundo"
mi_string_2 = 'Hola mundo'

print(mi_string, type(mi_string))
print(mi_string_2, type(mi_string_2))

print(mi_string[0])
print(mi_string[-1])

print(mi_string[0:2])
print(mi_string[:2])
print(mi_string[-2:])

print(len(mi_string))
print(mi_string.find("Hola") >= 0)
print(mi_string.find("caso") >= 0)

print(mi_string.replace("mundo", "Mario"))

mi_string_3 = "Hola " + "mundo"
print(mi_string_3)

mi_string_3 = "Hola "*10
print(mi_string_3)

mis_alumnos = """
mario callejas cabarcas,
antonio martinez gonzalez
"""
mis_alumnos = mis_alumnos.replace("\n", "")

print(mis_alumnos.split(","))

# Listas
mi_lista = mis_alumnos.split(",")
print(mi_lista[1])
'''

"""
mi_lista_2 = [1, 2, 3, 4, "Mario", 94.5, 12, 123, 345, "Mario"]
print(mi_lista_2)
print(len(mi_lista_2))

mi_lista_2.append(5)
print(mi_lista_2)

print(mi_lista_2.index("Mario"))

primer_mario = mi_lista_2.index("Mario")
print(mi_lista_2[:primer_mario])

segundo_mario = primer_mario + mi_lista_2[primer_mario+1:].index("Mario") + 1

print(primer_mario, segundo_mario)
print(mi_lista_2[primer_mario+1:segundo_mario])

mi_lista_2[1] = 10
print(mi_lista_2)

print(94.5 in mi_lista_2)
print(94.5 not in mi_lista_2)

mi_lista_2.pop()
print(mi_lista_2)
"""
"""
# Diccionarios

mi_diccionario = {"key1": 1, "key2": 2} # Tipo de dato que permite relacionar una llave con un valor 
print(mi_diccionario)

print("Accediendo a key1 ->", mi_diccionario["key1"])
print("Accediendo a key2 ->", mi_diccionario["key2"])

# Las llaves deben ser unicas
# llave:valor
mi_diccionario_2 = {
    "number": 1,
    2: "number",
    True: 2.3,
    2.3: True,
    2.4: "number"
}

print(mi_diccionario_2)
print(mi_diccionario_2["number"])
print(mi_diccionario_2[2])
print(mi_diccionario_2[True])
print(mi_diccionario_2[2.3])
print(mi_diccionario_2[2.4])

mi_estudiante = {
    "nombre": "Pepito",
    "apellido": "Perez",
    "edad": 20
}
print(mi_estudiante)

mi_estudiante["nombre"] = "Juanito"
print(mi_estudiante)

mi_estudiante.update({"apellido": "Mora"})
print(mi_estudiante)

mi_estudiante_copia = mi_estudiante.copy()

mi_estudiante["nota1"] = 450
print(mi_estudiante)

mi_estudiante.update({"nota2": 50})
print(mi_estudiante)

print(mi_estudiante_copia)

nota_final = mi_estudiante["nota1"] + mi_estudiante["nota2"]
print(f"La nota final del estudiante {mi_estudiante['nombre']} es {nota_final}")

print(mi_estudiante.items()) # Retorna una lista de tuplas (tipo de dato inmutable - no se puede modificar), que contienen SIEMPRE en la primera posicion de cada tupla, la llave y en la segunda, el valor

print(mi_estudiante.keys())
print(mi_estudiante.values())

#print(mi_estudiante["nota3"])
print(mi_estudiante.get("nota2", 0))
print(mi_estudiante.get("nota3", 0))

print(mi_estudiante)

mi_diccionario_3 = {
    "lista": [1, "hola", True, 2.4],
    "diccionario": {"key1": 1, 1:"mundo"},
    "tupla": (3,4)
}

print(mi_diccionario_3)
print(mi_diccionario_3["lista"][1])
print(mi_diccionario_3["diccionario"]["key1"])
print(mi_diccionario_3["tupla"][0])

mi_lista_4 = [mi_diccionario_3, 2, True, "Mundo"]
print(mi_lista_4[0]["lista"][1])
"""
"""
# Conversion de entero a string
mi_entero = 23
mi_entero_str = str(mi_entero)
print(f"mi entero es {mi_entero}, su tipo es {type(mi_entero)}")
print(f"mi entero string es {mi_entero_str}, su tipo es {type(mi_entero_str)}")

# Conversion de string a entero
mi_entero_str = "25"
mi_entero = int(mi_entero_str)
print(f"mi entero es {mi_entero}, su tipo es {type(mi_entero)}")
print(f"mi entero string es {mi_entero_str}, su tipo es {type(mi_entero_str)}")

# Conversion de string a float
mi_flotante_str = "35.45"
mi_flotante = float(mi_flotante_str)
print(f"mi flotante es {mi_flotante}, su tipo es {type(mi_flotante)}")
print(f"mi flotante string es {mi_flotante_str}, su tipo es {type(mi_flotante_str)}")

# Conversion de float a str
mi_flotante = 35.45
mi_flotante_str = str(mi_flotante)
print(f"mi flotante es {mi_flotante}, su tipo es {type(mi_flotante)}")
print(f"mi flotante string es {mi_flotante_str}, su tipo es {type(mi_flotante_str)}")
"""

# Ejercicio
mi_entero_str = "212314-ha2na092"
mi_entero_split = mi_entero_str.split("-")
print(mi_entero_split)
mi_entero = int(mi_entero_split[0])
print(f"mi entero es {mi_entero}, su tipo es {type(mi_entero)}")