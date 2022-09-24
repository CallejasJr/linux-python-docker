
my_bool = False
if my_bool:
    print("Dentro de la condicion")

number_1 = 15
number_2 = 30
if number_1 >= number_2:
    print(f"{number_1} es mayor o igual a {number_2}")
else:
    print(f"{number_1} es menor a {number_2}")

my_list = ["hola", "mundo", "hola mundo", 5]
if len(my_list) >= 4:
    print("La lista es correcta por longitud")
elif 2 in my_list:
    print("La lista es correcta por numero entero 2")
elif my_list[0] == "Hola":
    print("La lista es correcta por Hola")
else:
    print("La lista es incorrecta")

if ("hola" in my_list) or (number_1 >= 20):
    print("Las condicones se cumplen")
else: 
    print("Las condiciones no se cumplen")

print(1 == True)
print(0 == False)

number = 1
if number:
    print("Las condicon se cumple")
else: 
    print("Las condicion no se cumple")

hola_mundo_exist = True if "hola mundo" in my_list else False
print(hola_mundo_exist)