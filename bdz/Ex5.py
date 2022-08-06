import pandas as pd
# coding=utf-8
data = pd.read_csv('train.csv')
print('Столбцы, содержащие NaN:')
print(data.isnull().any())  # Извлечение нулевых значений из набора данных,
# any возвращает True для всего столбца если есть NaN
data['Age'] = data['Age'].fillna(data['Age'].median())  # Функция fillna() автоматически найдет и заменит все значения NaN
print('Age больше не содержит NaN')
print(data.isnull().any())
