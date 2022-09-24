#print(range(4)) #-> [0, 1, 2, 3]

#for i in range(0, 10, 2):
#    print(i)

#my_list = [1, 23.2, True, "Hola", [1,2,3], {"key": 1}]
#for item in my_list:
#    print(item)

students = ["Juan", "Pedro", "Pepe", "Camilo"]
#for student in students:
#    print(student)

calificacion = ""
for i in range(len(students)):
    if students[i].find("P") >= 0:
        calificacion = " Gano"
    else:
        calificacion = " Perdio"

    students[i] = "Estudiante: " + students[i] + calificacion

#print(students)


my_dict = {
    "number": 1,
    2: "number",
    True: 2.3,
    2.3: False
}

#for item in my_dict.values():
#    print(item)

#for key, value in my_dict.items():
#    print(f" {key} -> {value}")

#a = 0
#while a <= 2:
    #print(a)
    #a += 1