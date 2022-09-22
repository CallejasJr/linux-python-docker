for i in range(4):
    print(i)

my_list = [1, 23.2, True, "Hola"]

for i in range(len(my_list)):
    print(my_list[i])

for item in my_list:
    print(item)

my_dict = {
    "number": 1,
    2: "number",
    True: 2.3,
    2.3: False
}

for item in my_dict:
    print(item)

for k in my_dict.keys():
    print(my_dict[k])

for v in my_dict.values():
    print(v)

for k, v in my_dict.items():
    print(f"{k} -> {v}")

a = 0
while a < 2:
    print(a)
    a += 1