
my_bool = True
if my_bool:
    print("Dentro del condicional")


number_1 = 20
number_2 = 30

if number_1 >= number_2:
    print(f"{number_1} es mayor o igual a {number_2}")
else:
    print(f"{number_1} es menor a {number_2}")


my_list = [2, "Correcta", False]

if len(my_list) > 10:
    print("La lista es correcta por longitud")
elif True in my_list:
    print("La lista es correcta por booleano")
elif my_list[1] == "Correcta":
    print("La lista es correcta por string")
else:
    print("La lista no es correcta")

print(1 == True)
print(0 == False)

false_boolean_exist = True if False in my_list else False
print(false_boolean_exist)