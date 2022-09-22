
# Variables con numeros enteros
my_first_number = 30
my_second_number = 20

my_first_number += 1 # my_first_number + 1
print(my_first_number)
my_first_number -= 1 # my_first_number - 1
print(my_first_number)

print("Suma ", (my_first_number+my_second_number))
 
diff = my_first_number - my_second_number # Almacenando operaciones con variables
print("Resta ", diff)

myFloatVar = 2431/231 # Variables con punto flotante
print("Division ", myFloatVar)

#Variables tipo string
my_hello_world = "Hola Mundo"
print(my_hello_world)
print("Este es mi ", my_hello_world)

# Variables booleanas
my_true = True
my_false = False
print("OR ", (my_true | my_false))
print("AND ", (my_true and my_false))

# Variables tipo listas

my_list = [1, 2, 3, 4]

print(my_list[0])

my_list.append(5)
print(my_list)

my_list.pop()
print(my_list)

print("El item 2 esta en la posicion: ", my_list.index(2))
print(my_list[my_list.index(3)])

three_idx = my_list.index(3)
print(my_list[three_idx])

my_list_2 = [1, 23.2, True, "Hola"]
print(my_list_2)

my_list_2.insert(3, "Mundo")
print(my_list_2)

my_list_2[3] = "mundo"
print(my_list_2)

print(len(my_list_2))

print("mundo" in my_list_2)
print("mundo" not in my_list_2)

# Variables tipo diccionario

my_dict = {"key1": 1, "key2": 2}
print(my_dict)
print(my_dict["key1"])

my_dict.update({"key2": 3})
print(my_dict)

print(my_dict.items())

print(my_dict.keys())
print(my_dict.values())

print(my_dict.get("key1", "No existe"))
print(my_dict.get("key3", "No existe"))

my_dict["key3"] = "4"
print(my_dict)

my_dict.pop("key3")
print(my_dict)

my_dict_2 = {
    "number": 1,
    2: "number",
    True: 2.3,
    2.3: False
}

print(my_dict_2)
print(my_dict_2["number"])
print(my_dict_2[True])
print(my_dict_2[2])
print(my_dict_2[2.3])

my_dict_2 = {
    "nombre": "Juan",
    "edad": 23,
    "genero": "M",
    "activo": False
}

print(my_dict_2["nombre"] == "Mario")

my_students = [
    {
        "nombre": "Juan",
        "edad": 23,
        "genero": "M",
        "activo": False
    },
    {
        "nombre": "Maria",
        "edad": 25,
        "genero": "F",
        "activo": True
    }
]

student_number = 0

print("El/La estudiante ", my_students[student_number]["nombre"], " esta en estado ",my_students[student_number]["activo"] == True)