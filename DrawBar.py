import csv
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType


class DrawBar(object):
    """绘制柱形图类"""

    def __init__(self):
        """创建柱状图实例，并设置宽高和风格"""
        self.bar = Bar(init_opts=opts.InitOpts(width='1500px', height='700px', theme=ThemeType.LIGHT))

    def add_x(self):
        """为图形添加X轴数据"""
        with open('time1.csv') as csvfile:
            reader = csv.reader(csvfile)
            x = [str(row[0]) for row in reader]
            print(x)

        self.bar.add_xaxis(
            xaxis_data=x,

        )

    def add_y(self):
        with open('time1.csv') as csvfile:
            reader = csv.reader(csvfile)
            y1 = [float(row[1]) for row in reader]

            print(y1)

        """为图形添加Y轴数据，可添加多条"""
        self.bar.add_yaxis(  # 第一个Y轴数据
            series_name="评论数",  # Y轴数据名称
            y_axis=y1,  # Y轴数据
            label_opts=opts.LabelOpts(is_show=True, color="black"),  # 设置标签
            bar_max_width='100px',  # 设置柱子最大宽度
        )

    def set_global(self):
        """设置图形的全局属性"""
        # self.bar(width=2000,height=1000)
        self.bar.set_global_opts(
            title_opts=opts.TitleOpts(  # 设置标题
                title='扫黑风暴近日评论统计', title_textstyle_opts=opts.TextStyleOpts(font_size=35)

            ),
            tooltip_opts=opts.TooltipOpts(  # 提示框配置项（鼠标移到图形上时显示的东西）
                is_show=True,  # 是否显示提示框
                trigger="axis",  # 触发类型（axis坐标轴触发，鼠标移到时会有一条垂直于X轴的实线跟随鼠标移动，并显示提示信息）
                axis_pointer_type="cross"  # 指示器类型（cross将会生成两条分别垂直于X轴和Y轴的虚线，不启用trigger才会显示完全）
            ),
            toolbox_opts=opts.ToolboxOpts(),  # 工具箱配置项(什么都不填默认开启所有工具)

        )

    def draw(self):
        """绘制图形"""

        self.add_x()
        self.add_y()
        self.set_global()
        self.bar.render('DrawBar.html')  # 将图绘制到 test.html 文件内，可在浏览器打开

    def run(self):
        """执行函数"""
        self.draw()


if __name__ == '__main__':
    app = DrawBar()

app.run()
