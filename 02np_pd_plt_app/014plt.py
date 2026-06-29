# 3.12.2种画图接口
# Matplotlib有两种画图接口：一个是便捷的MATLAB风格的有状态的接口，另一个是功能更强大的面向对象接口。
# 1）状态接口
import numpy as np
import matplotlib.pyplot as plt # 导入matplotlib

x = np.linspace(0, 10, 100) # 创建x轴的数据
y1 = np.sin(x) # 创建y轴的数据
y2 = np.cos(x) # 创建y轴的数据

plt.figure(figsize=(10, 6)) # 创建画布，并指定画布大小 10*6英寸

plt.subplot(2, 1, 1) # 创建2行1列个子图，并指定第1个子图
plt.xlim(0, 10) # 设置x轴的范围
plt.ylim(-1, 1) # 设置y轴的范围
plt.xlabel("x") # 设置x轴的标签
plt.ylabel("sin(x)") # 设置y轴的标签
plt.title("sin") # 设置子图的标题
plt.plot(x, y1) # 绘制曲线

plt.subplot(2, 1, 2) # 创建2行1列个子图，并指定第2个子图
plt.xlim(0, 10) # 设置x轴的范围
plt.ylim(-1, 1) # 设置y轴的范围
plt.xlabel("x") # 设置x轴的标签
plt.ylabel("cos(x)") # 设置y轴的标签
plt.title("cos") # 设置子图的标题
plt.plot(x, y2)

plt.show() # 显示图像

import numpy as np
import matplotlib.pyplot as plt # 导入matplotlib

x = np.linspace(0, 10, 100) # 创建x轴的数据
y1 = np.sin(x) # 创建y轴的数据
y2 = np.cos(x) # 创建y轴的数据

fig, ax = plt.subplots(2, figsize=(10, 6)) # 创建画布，并指定画布大小

ax[0].set_xlim(0, 10) # 设置x轴的范围
ax[0].set_ylim(-1, 1) # 设置y轴的范围
ax[0].set_xlabel("x") # 设置x轴的标签
ax[0].set_ylabel("sin(x)") # 设置y轴的标签
ax[0].set_title("sin") # 设置子图的标题
ax[0].plot(x, y1) # 绘制曲线

ax[1].plot(x, y2) # 绘制曲线
ax[1].set_xlim(0, 10) # 设置x轴的范围
ax[1].set_ylim(-1, 1) # 设置y轴的范围
ax[1].set_xlabel("x") # 设置x轴的标签
ax[1].set_ylabel("cos(x)") # 设置y轴的标签
ax[1].set_title("cos") # 设置子图的标题

plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"] # 指定中文字体
rcParams["axes.unicode_minus"] = False # 解决负号显示问题

df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
df.info() # 查看数据集信息
# RangeIndex: 1461 entries, 0 to 1460
# Data columns (total 6 columns):
# #  Column     Non-Null Count Dtype
# --- ------     -------------- -----
# 0  date      1461 non-null  object
# 1  precipitation 1461 non-null  float64
# 2  temp_max    1461 non-null  float64
# 3  temp_min    1461 non-null  float64
# 4  wind      1461 non-null  float64
# 5  weather    1461 non-null  object
# dtypes: float64(4), object(2)
# memory usage: 68.6+ KB
# 使用直方图将降水量分组并绘制每组出现频次。
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.hist(df["precipitation"], bins=5) # 绘制直方图，将降水量均匀分为5组
ax1.set_xlabel("降水量")
ax1.set_ylabel("出现频次")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"] # 指定中文字体
rcParams["axes.unicode_minus"] = False # 解决负号显示问题

df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(df["temp_max"], df["precipitation"]) # 绘制散点图，横轴为最高气温，纵轴为降水量
ax1.set_xlabel("最高气温")
ax1.set_ylabel("降水量")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"] # 指定中文字体
rcParams["axes.unicode_minus"] = False # 解决负号显示问题

def year_color(x):
    """添加一列，为不同年份的数据添加不同的颜色"""
    if x.year == 2022:
        return "r"
    elif x.year == 2023:
        return "g"
    elif x.year == 2024:
        return "b"
    else:
        return "k"

df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
df["date"] = pd.to_datetime(df["date"])
df["color"] = df["date"].apply(year_color)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 绘制散点图，横轴为最高气温，纵轴为降水量
# c设置颜色,alpha设置透明度
ax1.scatter(df["temp_max"], df["precipitation"], c=df["color"], alpha=0.5)
ax1.set_xlabel("最高气温")
ax1.set_ylabel("降水量")
plt.show()


import pandas as pd

df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\sleep.csv")
df.info() # 查看数据集信息
# RangeIndex: 400 entries, 0 to 399
# Data columns (total 13 columns):
# #  Column          Non-Null Count Dtype
# --- ------          -------------- -----
# 0  person_id        400 non-null  int64
# 1  gender          400 non-null  object
# 2  age           400 non-null  int64
# 3  occupation        400 non-null  object
# 4  sleep_duration      400 non-null  float64
# 5  sleep_quality      400 non-null  float64
# 6  physical_activity_level 400 non-null  int64
# 7  stress_level       400 non-null  int64
# 8  bmi_category       400 non-null  object
# 9  blood_pressure      400 non-null  object
# 10 heart_rate        400 non-null  int64
# 11 daily_steps       400 non-null  int64
# 12 sleep_disorder      110 non-null  object
# dtypes: float64(2), int64(6), object(5)
# memory usage: 40.8+ KB
# 1）柱状图
# 柱状图用于展示类别数据的分布情况。它通过一系列矩形的高度（或长度）来展示数据值，适合对比不同类别之间的数量或频率。简单直观，容易理解和比较各类别数据。
# 使用柱状图展示不同睡眠时长的数量。
pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().plot.bar(
  color=["red", "green", "blue", "yellow", "cyan", "magenta", "black", "purple"]
)
plt.show()

# 2）折线图
# 折线图通常用于展示连续数据的变化趋势。它通过一系列数据点连接成的线段来表示数据的变化。能够清晰地展示数据的趋势和波动。
# 使用折线图展示不同睡眠时长的数量。
pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().sort_index().plot()
plt.show()

# 3）面积图
# 面积图是折线图的一种变体，线下的区域被填充颜色，用于强调数据的总量或变化。可以更直观地展示数据量的变化，适合用来展示多个分类的累计趋势。
# 使用面积图展示不同睡眠时长的数量。
pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().sort_index().plot.area()
plt.show()

# 4）直方图
# 直方图用于展示数据的分布情况。它将数据范围分成多个区间，并通过矩形的高度显示每个区间内数据的频率或数量。可以揭示数据分布的模式，如偏态、峰度等。
# 使用直方图展示不同睡眠时长的数量。
df["sleep_duration"].value_counts().plot.hist()

# 5）饼状图
# 饼状图用于展示一个整体中各个部分所占的比例。它通过一个圆形图形分割成不同的扇形，每个扇形的角度与各部分的比例成正比。能够快速展示各部分之间的比例关系，但不适合用于展示过多的类别或比较数值差异较小的部分。
# 使用饼状图展示不同睡眠时长的占比。
pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]).value_counts().sort_index().plot.pie()

# 3.13.2双变量可视化
# 1）散点图
# 散点图通过在二维坐标系中绘制数据点来展示两组数值数据之间的关系。能够揭示两个变量之间的相关性和趋势。
# 绘制睡眠时间与睡眠质量的散点图。
df.plot.scatter(x="sleep_duration", y="sleep_quality")
plt.show()

# 2）蜂窝图
# 蜂窝图是散点图的扩展，通常用于表示大量数据点之间的关系。它通过将数据点分布在一个六边形网格中，每个六边形的颜色代表其中的数据密度。适合展示大量数据点，避免了散点图中的过度重叠问题。
# 绘制睡眠时间与睡眠质量的蜂窝图。
df.plot.hexbin(x="sleep_duration", y="sleep_quality", gridsize=10)
plt.show()

# 3）堆叠图
# 堆叠图用于展示多个数据系列的累积变化。常见的堆叠图包括堆叠柱状图、堆叠面积图等。它通过将每个数据系列堆叠在前一个系列之上，展示数据的累积情况。能够清晰地展示不同部分的相对贡献，适合多个数据系列的比较。
# 绘制睡眠时间与睡眠质量的堆叠图。
df["sleep_quality_stage"] = pd.cut(df["sleep_quality"], range(11))
df["sleep_duration_stage"] = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12])
df_pivot_table = df.pivot_table(
  values="person_id", index="sleep_quality_stage", columns="sleep_duration_stage", aggfunc="count"
)
df_pivot_table.plot.bar()

# 设置stacked=True，会将柱体堆叠。
df_pivot_table.plot.bar(stacked=True)

# 4）折线图
df_pivot_table.plot.line()
plt.show()
