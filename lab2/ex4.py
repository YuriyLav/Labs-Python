with open("input_1.txt", "r", encoding="utf8") as file1:
    with open("input_2.txt", "r", encoding="utf8") as file2:
        str1 = file1.read()
        st1 = str1.split()
        str2 = file2.read()
        st2 = str2.split()
        flag = False
        s = ""
        for i in st2:
            for j in st1:
                if i == j:
                    flag = True
            if not flag:
                s = s + i + " "
            flag = False
with open('output.txt', 'w') as fs:
    fs.write(s)
