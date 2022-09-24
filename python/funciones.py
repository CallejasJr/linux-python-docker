"""
def suma(num_1, num_2):
    result = num_1 + num_2
    return result

number_1 = 10
number_2 = 100
response = suma(number_1, number_2)
print(response)

a = 100
b = 500
response_2 = suma(a, b)
print(response_2)

response_3 = suma(97, 100)
print(response_3)
"""
# get en una lista

def get_list(my_list, idx, if_not_exist=None):
    try:
        my_item = my_list[idx]
    except IndexError:
        my_item = if_not_exist
    return my_item

lista = ["hola", "mundo", "en", "diplomado", "IoT"]

print(get_list(my_list=lista, idx=20))