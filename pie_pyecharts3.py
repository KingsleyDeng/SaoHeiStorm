import csv

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from sympy.combinatorics import Subset
from wordcloud import WordCloud

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)

    data2 = [int(row[1].strip('')[0:2]) for row in reader]


    #print(data2)
print(type(data2))

#先变成集合得到seq中的所有元素，避免重复遍历
set_seq = set(data2)
list = []
for item in set_seq:
    list.append((item,data2.count(item)))  #添加元素及出现个数
list.sort()
print(type(list))
#print(list)


with open("time2.csv", "w+", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    for i in list:                # 对于每一行的，将这一行的每个元素分别写在对应的列中
        writer.writerow(i)


n = 4#分成n组
m = int(len(list)/n)
list2 = []
for i in range(0, len(list), m):
    list2.append(list[i:i+m])

print("凌晨 : ",list2[0])
print("上午 : ",list2[1])
print("下午 : ",list2[2])
print("晚上 : ",list2[3])

with open('time2.csv') as csvfile:
    reader = csv.reader(csvfile)
    y1 = [int(row[1]) for row in reader]

    print(y1)

n =6
groups = [y1[i:i + n] for i in range(0, len(y1), n)]

print(groups)

x=['凌晨','上午','下午','晚上']
y1=[]
for y1 in groups:
    num_sum = 0
    for groups in y1:
        num_sum += groups

print(x)
print(y1)


import csv

from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint

str_name1 = '点'

num = y1
lab = x
(
    Pie(init_opts=opts.InitOpts(width='1500px',height='450px',theme=ThemeType.LIGHT))#默认900，600
        .set_global_opts(
        title_opts=opts.TitleOpts(title="扫黑风暴观看时间区间评论统计"
                                  , title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
        legend_opts=opts.LegendOpts(

            pos_top="8%",  # 图例位置调整
        ),
    )
    .add(series_name='',center=[260, 270], data_pair=[(j, i) for i, j in zip(num, lab)])#饼图
   .add(series_name='',center=[1230, 270],data_pair=[(j,i) for i,j in zip(num,lab)],radius=['40%','75%'])#环图
    .add(series_name='', center=[750, 270],data_pair=[(j, i) for i, j in zip(num, lab)], rosetype='radius')#南丁格尔图
).render('pie_pyecharts3.html')