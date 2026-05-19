import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#读取csv文件
weather =  pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather.csv")

print(weather)

print(weather.shape)

print(weather[["date","temp_max","temp_min"]])

print(weather.iloc[:,0:2])

print(weather.iloc[[1,10,100]])

print(weather.loc[1, "precipitation"]) # 获取行标签为1，列标签为precipitation的数据
print(weather.loc[:, "precipitation"]) # 获取所有行，列标签为precipitation的数据
print(weather.iloc[:, [3, 5, -1]]) # 获取所有行，列位置为3，5，最后一位的数据
print(weather.iloc[:10, 2:6]) # 获取前10行，列位置为2、3、4、5的数据
print(weather.loc[:10, ["date", "precipitation", "temp_max", "temp_min"]]) # 通过行列标签获取数据

weather["month"] = pd.to_datetime(weather["date"]).dt.to_period("M").astype(str) # 将date转换为 年-月 的格式

df_groupby_date = weather.groupby("month") # 按month分组，返回一个分组对象(DataFrameGroupBy)
month_temp = df_groupby_date[["temp_max", "temp_min"]] # 从分组对象中选择特定的列
month_temp_mean = month_temp.mean() # 对每个列求平均值

# 以上代码可以写在一起
month_temp_mean = weather.groupby("month")[["temp_max", "temp_min"]].mean()

weather.groupby("month")["weather"].nunique()

weather.groupby("month")[["temp_max", "temp_min"]].mean().plot() # 使用plot绘制折线图
# plt.show()

weather.describe() # 查看常用统计信息
weather.describe().T # 行列转置
weather.describe(include="all") # 统计所有列
weather.describe(include=["float64"]) # 只统计数据类型为float64的列

df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\weather.csv")
df.nlargest(30, "temp_max") #通过nlargest()找出temp_max最大的30条数据。

df.nlargest(30, "temp_max").nsmallest(5, "temp_min")#通过nlargest()找出temp_min最小的5条数据。

df["year"] = pd.to_datetime(df["date"]).dt.to_period("Y").astype(str) # 将date转换为 年 格式
df_sort = df.sort_values(["year", "temp_max"], ascending=[True, False]) # 按year升序，temp_max降序排序
df_sort.drop_duplicates(subset="year") # 按year去重