import pandas as pd
import numpy as np
s = pd.Series([np.nan, None, pd.NA])
print(s)
# 0   NaN
# 1  None
# 2  <NA>
# dtype: object
print(s.isnull())
# 0  True
# 1  True
# 2  True
# dtype: bool

df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather_withna.csv")
print(df.tail(5))
#       date precipitation temp_max temp_min wind weather
# 1456 2015-12-27      NaN    NaN    NaN  NaN   NaN
# 1457 2015-12-28      NaN    NaN    NaN  NaN   NaN
# 1458 2015-12-29      NaN    NaN    NaN  NaN   NaN
# 1459 2015-12-30      NaN    NaN    NaN  NaN   NaN
# 1460 2015-12-31      20.6   12.2    5.0  3.8  rain

# 可以通过keep_default_na参数设置是否将空白值设置为缺失值。
df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather_withna.csv", keep_default_na=False)
print(df.tail(5))
# 可通过na_values参数将指定值设置为缺失值。
df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather_withna.csv", na_values=["2015-12-31"])
print(df.tail(5))

# 1）通过isnull()查看缺失值数量
print(df.isnull().sum())

# 2）通过missingno条形图展示缺失值
import missingno as msno
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather_withna.csv")
# msno.bar(df)
# plt.show()
# 3）
# missingno绘制的热力图能够展示数据集中不同列的缺失值之间的相关性。这里的相关性体现的是当某一列出现缺失值时，其他列出现缺失值的可能性。如果两个列的缺失值呈现正相关，意味着当其中一列有缺失值时，另一列也很可能有缺失值；若为负相关，则表示当一列有缺失值时，另一列更倾向于没有缺失值。
# 颜色与数值：热力图中的颜色和数值反映了列之间缺失值的相关性。接近 1 表示正相关，接近 -1 表示负相关，接近 0 则表示缺失值之间没有明显的关联。
# 示例说明：假如A列和B列在热力图中对应区域颜色较深且数值接近 1，这就表明当A列出现缺失值时，B列也很可能出现缺失值；若数值接近 -1，情况则相反
# msno.heatmap(df)
# plt.show()

# 3.7.4剔除缺失值
# 通过dropna()方法来剔除缺失值。
# 1）Series剔除缺失值
s = pd.Series([1, pd.NA, None])
print(s)
# 0    1
# 1  <NA>
# 2  None
# dtype: object
print(s.dropna())
# 0  1
# dtype: object
# 2）DataFrame剔除缺失值
# 无法从DataFrame中单独剔除一个值，只能剔除缺失值所在的整行或整列。默认情况下，dropna()会剔除任何包含缺失值的整行数据。
df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
print(df)
#    0   1 2
# 0   1 <NA> 2
# 1   2   3 5
# 2 <NA>   4 6
print(df.dropna())
#  0 1 2
# 1 2 3 5
# 可以设置按不同的坐标轴剔除缺失值，比如axis=1（或 axis='columns'）会剔除任何包含缺失值的整列数据。
df = pd.DataFrame([[1, pd.NA, 2], [2, 3, 5], [pd.NA, 4, 6]])
print(df)
#    0   1 2
# 0   1 <NA> 2
# 1   2   3 5
# 2 <NA>   4 6
print(df.dropna(axis=1))
#  2
# 0 2
# 1 5
# 2 6
# 有时只需要剔除全部是缺失值的行或列，或者绝大多数是缺失值的行或列。这些需求可以通过设置how或thresh参数来满足，它们可以设置剔除行或列缺失值的数量阈值。
df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
print(df)
#    0   1   2
# 0   1 <NA>   2
# 1 <NA> <NA>   5
# 2 <NA> <NA> <NA>
print(df.dropna(how="all")) # 如果所有值都是缺失值,则删除这一行
#    0   1 2
# 0   1 <NA> 2
# 1 <NA> <NA> 5
print(df.dropna(thresh=2)) # 如果至少有2个值不是缺失值,则保留这一行
#  0   1 2
# 0 1 <NA> 2
# 可以通过设置subset参数来设置某一列有缺失值则进行剔除。
df = pd.DataFrame([[1, pd.NA, 2], [pd.NA, pd.NA, 5], [pd.NA, pd.NA, pd.NA]])
print(df)
#    0   1   2
# 0   1 <NA>   2
# 1 <NA> <NA>   5
# 2 <NA> <NA> <NA>
print(df.dropna(subset=[0])) # 如果0列有缺失值,则删除这一行
#  0   1 2
# 0 1 <NA> 2

# 1）使用固定值填充
# 通过fillna()方法，传入值或字典进行填充。
df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather_withna.csv")
print(df.fillna(0).tail()) # 使用固定值填充
#       date precipitation temp_max temp_min wind weather
# 1456 2015-12-27      0.0    0.0    0.0  0.0    0
# 1457 2015-12-28      0.0    0.0    0.0  0.0    0
# 1458 2015-12-29      0.0    0.0    0.0  0.0    0
# 1459 2015-12-30      0.0    0.0    0.0  0.0    0
# 1460 2015-12-31      20.6   12.2    5.0  3.8  rain
print(df.fillna({"temp_max": 60, "temp_min": -60}).tail()) # 使用字典来填充
#       date precipitation temp_max temp_min wind weather
# 1456 2015-12-27      NaN   60.0   -60.0  NaN   NaN
# 1457 2015-12-28      NaN   60.0   -60.0  NaN   NaN
# 1458 2015-12-29      NaN   60.0   -60.0  NaN   NaN
# 1459 2015-12-30      NaN   60.0   -60.0  NaN   NaN
# 1460 2015-12-31      20.6   12.2    5.0  3.8  rain
# 2）使用统计值填充
# 通过fillna()方法，传入统计后的值进行填充。
print(df.fillna(df[["precipitation", "temp_max", "temp_min", "wind"]].mean()).tail()) # 使用平均值填充
#       date precipitation  temp_max temp_min   wind weather
# 1456 2015-12-27    3.052332 15.851468 7.877202 3.242055   NaN
# 1457 2015-12-28    3.052332 15.851468 7.877202 3.242055   NaN
# 1458 2015-12-29    3.052332 15.851468 7.877202 3.242055   NaN
# 1459 2015-12-30    3.052332 15.851468 7.877202 3.242055   NaN
# 1460 2015-12-31   20.600000 12.200000 5.000000 3.800000  rain
# 3）使用前后的有效值填充
# 通过ffill()或bfill()方法使用前面或后面的有效值填充。
print(df.ffill().tail()) # 使用前面的有效值填充
#       date precipitation temp_max temp_min wind weather
# 1456 2015-12-27      0.0   11.1    4.4  4.8   sun
# 1457 2015-12-28      0.0   11.1    4.4  4.8   sun
# 1458 2015-12-29      0.0   11.1    4.4  4.8   sun
# 1459 2015-12-30      0.0   11.1    4.4  4.8   sun
# 1460 2015-12-31      20.6   12.2    5.0  3.8  rain
print(df.bfill().tail()) # 使用后面的有效值填充
#       date precipitation temp_max temp_min wind weather
# 1456 2015-12-27      20.6   12.2    5.0  3.8  rain
# 1457 2015-12-28      20.6   12.2    5.0  3.8  rain
# 1458 2015-12-29      20.6   12.2    5.0  3.8  rain
# 1459 2015-12-30      20.6   12.2    5.0  3.8  rain
# 1460 2015-12-31      20.6   12.2    5.0  3.8  rain
# 4）通过线性插值填充
# 通过interpolate()方法进行线性插值填充。线性插值操作，就是用于在已知数据点之间估算未知数据点的值。interpolate方法支持多种插值方法，可通过method参数指定，常见的方法有：
# 'linear'：线性插值，基于两点之间的直线来估算缺失值，适用于数据呈线性变化的情况。
# 'time'：适用于时间序列数据，会考虑时间间隔进行插值。
# 'polynomial'：多项式插值，通过拟合多项式曲线来估算缺失值，可通过order参数指定多项式的阶数。
import pandas as pd
import numpy as np

# 创建包含缺失值的 Series
s = pd.Series([1, np.nan, 3, 4, np.nan, 6])
# 使用默认的线性插值方法填充缺失值
s_interpolated = s.interpolate()
print(s_interpolated)

# 0  1.0
# 1  2.0
# 2  3.0
# 3  4.0
# 4  5.0
# 5  6.0
# dtype: float64