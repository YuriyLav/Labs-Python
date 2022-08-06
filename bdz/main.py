import pandas as pd
# coding=utf-8
data = pd.read_csv('train.csv')
mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # 1 класс, 2 класс, 3 класс
for row in data.iterrows():  # iterrows () - генератор, который выполняет итерацию по строкам в DataFrame.
    # Он возвращает индекс каждой строки и объект, содержащий саму строку.
    row = row[1]  # берем строку
    if row.Sex == 'male':
        if row.Survived == 0:
            mas[row.Pclass - 1][0] += 1  # dead male
        else:
            mas[row.Pclass - 1][1] += 1  # alive male
    else:
        if row.Survived == 0:
            mas[row.Pclass - 1][2] += 1  # dead female
        else:
            mas[row.Pclass - 1][3] += 1  # alive female
print("")
for i in range(3):
    print('Pclass', i + 1)
    print("Male: dead " + str(mas[i][0]) + "\talive " + str(mas[i][1]))
    print("Female: dead " + str(mas[i][2]) + "\talive " + str(mas[i][3]) + "\n")
