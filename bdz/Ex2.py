import pandas as pd
# coding=utf-8
data = pd.read_csv('train.csv')
man = data[data.Sex == 'male']
woman = data[data.Sex == 'female']

print("Male\n")
print(man.describe())  # describe() возвращает некоторые статистические данные
print("Female\n")
print(woman.describe())
