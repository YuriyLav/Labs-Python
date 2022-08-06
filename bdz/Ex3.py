import pandas as pd
# coding=utf-8
data = pd.read_csv('train.csv')
ports = ['C', 'Q', 'S']
info = {'C': [0, 0], 'Q': [0, 0], 'S': [0, 0]}  # port : [dead, alive]
for row in data.iterrows():
    row = row[1]
    if row.Survived and row.Embarked in ports:
        info[row.Embarked][1] += 1
    if not row.Survived and row.Embarked in ports:
        info[row.Embarked][0] += 1
sum_dead = 0
for i in info.values():  # значение
    sum_dead += i[0]  # число умерших
for k, v in info.items():  # пара ключ-значение
    print(k, ':')
    print('dead ' + str(v[0]))
    print('alive ' + str(v[1]))
    print('proportion of deaths %.2f%%\n' % (v[0] / (v[0] + v[1]) * 100))
