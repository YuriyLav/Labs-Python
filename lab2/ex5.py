with open("inputEx5.txt", "r", encoding="utf8") as file:
    str1 = file.read()
    str1 = str1.replace(" ", "")
    str1 = str1.replace("\n", "")
    freq = {}
    for i in str1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)  # coding: utf-8 Лямбда функция возвращает значение
with open('output.txt', 'w') as fs:
    fs.write(str(sort))
