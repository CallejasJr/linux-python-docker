
def suma(a, b):
    return a + b

print(suma(2, 4))

def get_list(lista, idx):
    return lista[idx]

my_list = [12, 13, 14]
print(get_list(my_list, 2))

def get_list(lista, idx, if_not_exist=None):
    try:
        return lista[idx]
    except IndexError:
        return if_not_exist

my_list = [12, 10, 14]
print(get_list(my_list, 2))
print(get_list(my_list, 3))
print(get_list(my_list, 1, "No existe"))
print(get_list(my_list, 3, "No existe"))

small_func = lambda x, y: x+y
print(small_func(2, 5))