import pandas as pd
# coding=utf-8
from collections import Counter
data = pd.read_csv('train.csv')
mas_name = data['Name'].tolist()
names = []
for name in mas_name:
    names.append(name.split(',')[0])

c = Counter(names).most_common(10)  # вид словаря, most_common([n]) - возвращает n
# наиболее часто встречающихся элементов
count = 0
for name in c:
    if count < 10:
        print(name)
    count += 1
