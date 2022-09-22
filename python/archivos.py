

with open("students.txt", "r") as file:
    students = file.readlines()
    file.close()

print(students)

lista = [2, 4, 5, 6]

with open("numbers.txt", "w") as file:
    for number in lista:
        file.write(str(number)+"\n")
    file.close()