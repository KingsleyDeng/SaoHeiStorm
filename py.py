import csv

from pyecharts import options as opts
from sympy.combinatorics import Subset
from wordcloud import WordCloud

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)

    data1 = [str(row[1])[0:2] for row in reader]

    print(data1)
print(type(data1))

# 先变成集合得到seq中的所有元素，避免重复遍历
set_seq = set(data1)
rst = []
for item in set_seq:
    rst.append((item, data1.count(item)))  # 添加元素及出现个数
rst.sort()
print(type(rst))
print(rst)

with open("time2.csv", "w+", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    for i in rst:  # 对于每一行的，将这一行的每个元素分别写在对应的列中
        writer.writerow(i)

with open('time2.csv') as csvfile:
    reader = csv.reader(csvfile)
    x = [str(row[0]) for row in reader]
    print(x)
with open('time2.csv') as csvfile:
    reader = csv.reader(csvfile)
    y1 = [float(row[1]) for row in reader]
    print(y1)
