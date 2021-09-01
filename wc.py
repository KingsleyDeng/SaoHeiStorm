import numpy as np
import re
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image

# 上面的包自己安装，不会的就百度

f = open('../Spiders/content.txt', 'r', encoding='utf-8')  # 这是数据源，也就是想生成词云的数据
txt = f.read()  # 读取文件
f.close()  # 关闭文件，其实用with就好，但是懒得改了
# 如果是文章的话，需要用到jieba分词，分完之后也可以自己处理下再生成词云
newtxt = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", txt)
print(newtxt)
words = jieba.lcut(newtxt)

img = Image.open(r'wc.jpg')  # 想要搞得形状
img_array = np.array(img)

# 相关配置，里面这个collocations配置可以避免重复
wordcloud = WordCloud(
    background_color="white",
    width=1080,
    height=960,
    font_path="../文悦新青年.otf",
    max_words=150,
    scale=10,  # 清晰度
    max_font_size=100,
    mask=img_array,
    collocations=False).generate(newtxt)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('wc.png')
