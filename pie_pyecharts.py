import csv

from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint

from pyecharts.globals import ThemeType

with open('time1.csv') as csvfile:
    reader = csv.reader(csvfile)
    x = [str(row[0]) for row in reader]
    print(x)
with open('time1.csv') as csvfile:
    reader = csv.reader(csvfile)
    y1 = [float(row[1]) for row in reader]

    print(y1)

num = y1
lab = x
(
    Pie(init_opts=opts.InitOpts(width='1700px', height='450px', theme=ThemeType.LIGHT))  # 默认900，600
        .set_global_opts(
        title_opts=opts.TitleOpts(title="扫黑风暴近日评论统计",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=27)), legend_opts=opts.LegendOpts(

            pos_top="10%", pos_left="1%",  # 图例位置调整
        ), )
        .add(series_name='', center=[280, 270], data_pair=[(j, i) for i, j in zip(num, lab)])  # 饼图
        .add(series_name='', center=[845, 270], data_pair=[(j, i) for i, j in zip(num, lab)], radius=['40%', '75%'])  # 环图
        .add(series_name='', center=[1380, 270], data_pair=[(j, i) for i, j in zip(num, lab)], rosetype='radius')  # 南丁格尔图
).render('pie_pyecharts.html')
