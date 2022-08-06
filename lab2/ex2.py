with open("inputEx2.txt", "r") as file:
    st = file.readline()
    st = st.split(";")
    max1 = int(st[2])
    min1 = int(st[2])
    maxCost = st[0]
    minCost = st[0]
    st = file.readlines()
    for i in st:
        i = i.split(";")
        if int(i[2]) > max1:
            max1 = int(i[2])
            maxCost = i[0]
        if int(i[2]) < min1:
            min1 = int(i[2])
            minCost = i[0]
with open('output.txt', 'w') as fs:
    fs.write("Артикул самого дорогого товара: " + maxCost + "\n" + "Артикул самого дешевого товара: " + minCost)
