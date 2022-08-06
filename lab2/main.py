with open("inputEx1.txt", "r") as file:
    str1 = file.read()
    mass = []
    st = str1.split()
    for i in st:
        mass.append(int(i))
with open('output.txt', 'w') as fs:
    fs.write("Максимальное число: " + str(max(mass)) + "\n" + "Минимальное число: " + str(min(mass)))
