import csv

import numpy as np
import re
import jieba
from matplotlib.pyplot import scatter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image

# 上面的包自己安装，不会的就百度

f = open('content.txt', 'r', encoding='utf-8')  # 这是数据源，也就是想生成词云的数据
words = f.read()  # 读取文件
f.close()  # 关闭文件，其实用with就好，但是懒得改了

name=["孙红雷","张艺兴","刘奕君","吴越","王志飞","刘之冰","江疏影"]

print(name)
count=[float(words.count("孙红雷")),
      float(words.count("艺兴")),
      float(words.count("刘奕君")),
      float(words.count("吴越")),
      float(words.count("王志飞")),
      float(words.count("刘之冰")),
      float(words.count("江疏影"))]
print(count)

import csv

from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint

from pyecharts.globals import ThemeType

num = count
lab = name
(
    Pie(init_opts=opts.InitOpts(width='1650px',height='450px',theme=ThemeType.LIGHT))#默认900，600
    .set_global_opts(
        title_opts=opts.TitleOpts(title="扫黑风暴主演提及占比",
                                               title_textstyle_opts=opts.TextStyleOpts(font_size=27)),legend_opts=opts.LegendOpts(

            pos_top="3%", pos_left="33%",# 图例位置调整
            ),)
    .add(series_name='',center=[280, 270], data_pair=[(j, i) for i, j in zip(num, lab)])#饼图
   .add(series_name='',center=[800, 270],data_pair=[(j,i) for i,j in zip(num,lab)],radius=['40%','75%'])#环图
    .add(series_name='', center=[1300, 270],data_pair=[(j, i) for i, j in zip(num, lab)], rosetype='radius')#南丁格尔图
).render('pie_pyecharts4.html')