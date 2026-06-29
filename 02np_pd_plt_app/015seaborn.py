import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["KaiTi"]
penguins = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\penguins.csv")
penguins.dropna(inplace=True)
penguins.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 333 entries, 0 to 343
# Data columns (total 7 columns):
# #  Column       Non-Null Count Dtype
# --- ------       -------------- -----
# 0  species      333 non-null  object
# 1  island       333 non-null  object
# 2  bill_length_mm   333 non-null  float64
# 3  bill_depth_mm   333 non-null  float64
# 4  flipper_length_mm 333 non-null  float64
# 5  body_mass_g    333 non-null  float64
# 6  sex        333 non-null  object
# dtypes: float64(4), object(3)
# memory usage: 20.8+ KB

# 1）直方图
# 绘制不同种类企鹅数量的直方图。
sns.histplot(data=penguins, x="species")
plt.show()

# 2）核密度估计图
# 核密度估计图（KDE，Kernel Density Estimate Plot）是一种用于显示数据分布的统计图表，它通过平滑直方图的方法来估计数据的概率密度函数，使得分布图看起来更加连续和平滑。核密度估计是一种非参数方法，用于估计随机变量的概率密度函数。其基本思想是，将每个数据点视为一个“核”（通常是高斯分布），然后将这些核的贡献相加以形成平滑的密度曲线。
# 绘制喙长度的核密度估计图。
sns.kdeplot(data=penguins, x="bill_length_mm")

# 在histplot()中设置kde=True也可以得到核密度估计图。
sns.histplot(data=penguins, x="bill_length_mm", kde=True)
plt.show()

# 3）计数图
# 计数图用于绘制分类变量的计数分布图，显示每个类别在数据集中出现的次数，是分析分类数据非常直观的工具，可以快速了解类别的分布情况。
# 绘制不同岛屿企鹅数量的计数图。
sns.countplot(data=penguins, x="island")
plt.show()

# 3.14.3双变量可视化
# 1）散点图
# 绘制横轴为体重，纵轴为脚蹼长度的散点图。可通过hue参数设置不同组别进行对比。
sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="sex")

# 也可以通过regplot()函数绘制散点图，同时会拟合回归曲线。可以通过fit_reg=False关闭拟合。
sns.regplot(data=penguins, x="body_mass_g", y="flipper_length_mm")

# 也可以通过lmplot()函数绘制基于hue参数的分组回归图。
sns.lmplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="sex")
# 
# 也可以通过jointplot()函数绘制在每个轴上包含单个变量的散点图。
sns.jointplot(data=penguins, x="body_mass_g", y="flipper_length_mm")
plt.show()

# 2）蜂窝图
# 通过jointplot()函数，设置kind="hex"来绘制蜂窝图。
sns.jointplot(data=penguins, x="body_mass_g", y="flipper_length_mm", kind="hex")
plt.show()

# 3）二维核密度估计图
# 通过kdeplot()函数，同时设置x参数和y参数来绘制二维核密度估计图。
sns.kdeplot(data=penguins, x="body_mass_g", y="flipper_length_mm")

# 通过fill=True设置为填充，通过cbar=True设置显示颜色示意条。
sns.kdeplot(data=penguins, x="body_mass_g", y="flipper_length_mm", fill=True, cbar=True)
plt.show()

# 4）条形图
# 条形图会按x分组对y进行聚合，通过estimator参数设置聚合函数，并通过errorbar设置误差条，误差条默认会显示。可以通过误差条显示抽样数据统计结果的可能统计范围，如果数据不是抽样数据, 可以设置为None来关闭误差条。
sns.barplot(data=penguins, x="species", y="bill_length_mm", estimator="mean", errorbar=None)

# 5）箱线图
# 箱线图是一种用于展示数据分布、集中趋势、散布情况以及异常值的统计图表。它通过五个关键的统计量（最小值、第一四分位数、中位数、第三四分位数、最大值）来展示数据的分布情况。
# 箱线图通过箱体和须来表现数据的分布，能够有效地显示数据的偏斜、分散性以及异常值。箱线图的组成部分：
# 箱体（Box）：
# 下四分位数（Q1）：数据集下 25% 的位置，箱体的下边缘。
# 上四分位数（Q3）：数据集下 75% 的位置，箱体的上边缘。
# 四分位间距（IQR, Interquartile Range）：Q3 和 Q1 之间的距离，用来衡量数据的离散程度。
# 中位数（Median）：箱体内部的水平线，表示数据集的中位数。
# 须（Whiskers）：
# 下须：从 Q1 向下延伸，通常是数据集中最小值与 Q1 的距离，直到没有超过1.5倍 IQR 的数据点为止。
# 上须：从 Q3 向上延伸，通常是数据集中最大值与 Q3 的距离，直到没有超过1.5倍 IQR 的数据点为止。
# 异常值（Outliers）：
# 超过1.5倍 IQR 的数据被认为是异常值，通常用点标记出来。异常值是数据中相对于其他数据点而言“非常大”或“非常小”的值。
sns.boxplot(data=penguins, x="species", y="bill_length_mm")
plt.show()

# 6）小提琴图
# 小提琴图（Violin Plot） 是一种结合了箱线图和核密度估计图（KDE）的可视化图表，用于展示数据的分布情况、集中趋势、散布情况以及异常值。小提琴图不仅可以显示数据的基本统计量（如中位数和四分位数），还可以展示数据的概率密度，提供比箱线图更丰富的信息。
sns.violinplot(data=penguins, x="species", y="bill_length_mm")
plt.show()

# 7）成对关系图
# 成对关系图是一种用于显示多个变量之间关系的可视化工具。它可以展示各个变量之间的成对关系，并且通过不同的图表形式帮助我们理解数据中各个变量之间的相互作用。
# 对角线上的图通常显示每个变量的分布（如直方图或核密度估计图），帮助观察每个变量的单变量特性。其他位置展示所有变量的两两关系，用散点图表示。
sns.pairplot(data=penguins, hue="species")

# 通常情况下成对关系图左上和右下对应位置的图的信息是相同的，可以通过PairGrid()为每个区域设置不同的图类型。
pair_grid = sns.PairGrid(data=penguins, hue="species")

# 通过 map 方法在网格上绘制不同的图形
pair_grid.map_upper(sns.scatterplot) # 上三角部分使用散点图
pair_grid.map_lower(sns.kdeplot) # 下三角部分使用核密度估计图
pair_grid.map_diag(sns.histplot) # 对角线部分使用直方图
plt.show()

# 3.14.4多变量可视化
# 多数绘图函数都支持使用hue参数设置一个类别变量，统计时按此类别分组统计并在绘图时使用颜色区分。
# 例如对小提琴图设置hue参数添加性别类别：
sns.violinplot(data=penguins, x="species", y="bill_length_mm", hue="sex", split=True)
plt.show()

# 3.14.5Seaborn样式
# 在Seaborn中，样式（style）控制了图表的整体外观，包括背景色、网格线、刻度线等元素。Seaborn提供了一些内置的样式选项，可以通过seaborn.set_style()来设置当前图表的样式。常见的样式有以下几种：
# white：纯白背景，没有网格线。
# dark：深色背景，带有网格线。
# whitegrid：白色背景，带有网格线。
# darkgrid：深色背景，带有网格线（默认样式）。
sns.set_style("darkgrid")
sns.histplot(data=penguins, x="island", kde=True)
plt.show()