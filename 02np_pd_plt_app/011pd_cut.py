# 参数	说明
# x	要分箱的数组或Series，通常是数值型数据。
# bins	切分区间的数值列表或者整数。如果是整数，则表示将数据均匀地分成多少个区间。如果是列表，则需要指定每个区间的边界。
# right	默认True，表示每个区间的右端点是闭区间，即包含右端点。如果设置为False，则左端点为闭区间。
# labels	传入一个列表指定每个区间的标签。
import pandas as pd
import numpy as np
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 加载员工数据

salary = pd.cut(df.iloc[9:16]["salary"], 3)
print(salary)
# 9   (8366.667, 11000.0]
# 10  (5733.333, 8366.667]
# 11  (5733.333, 8366.667]
# 12  (5733.333, 8366.667]
# 13  (5733.333, 8366.667]
# 14   (8366.667, 11000.0]
# 15   (3092.1, 5733.333]
# Name: salary, dtype: category
# Categories (3, interval[float64, right]): [(3092.1, 5733.333] < (5733.333, 8366.667] <
#                      (8366.667, 11000.0]]

salary = pd.cut(df.iloc[9:16]["salary"], [0, 10000, 20000])
print(salary)
# 9     (0, 10000]
# 10    (0, 10000]
# 11    (0, 10000]
# 12    (0, 10000]
# 13    (0, 10000]
# 14  (10000, 20000]
# 15    (0, 10000]
# Name: salary, dtype: category
# Categories (2, interval[int64, right]): [(0, 10000] < (10000, 20000]]

salary = pd.cut(df.iloc[9:16]["salary"], 3, labels=["low", "medium", "high"])
print(salary)
# 9    high
# 10  medium
# 11  medium
# 12  medium
# 13  medium
# 14   high
# 15    low
# Name: salary, dtype: category
# Categories (3, object): ['low' < 'medium' < 'high']
# 3.9.2分组聚合
# df.groupby("分组字段")["要聚合的字段"].聚合函数()
# df.groupby(["分组字段", "分组字段2", ...])[["要聚合的字段", "要聚合的字段2", ...]].聚合函数()
# 1）常用聚合函数
# 方法	说明
# sum()	求和
# mean()	平均值
# min()	最小值
# max()	最大值
# var()	方差
# std()	标准差
# median()	中位数
# quantile()	指定位置的分位数，如quantile(0.5)
# describe()	常见统计信息
# size()	所有元素的个数
# count()	非空元素的个数
# first	第一行
# last	最后一行
# nth	第n行
# 2）一次计算多个统计值
# 可以通过agg()或aggregate()进行更复杂的操作，如一次计算多个统计值。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
# 按department_id分组，计算salary的最小值，中位数，最大值
print(df.groupby("department_id")["salary"].agg(["min", "median", "max"]))
#          min  median   max
# department_id
# 10.0      4400.0  4400.0  4400.0
# 20.0      6000.0  9500.0 13000.0
# 30.0      2500.0  2850.0 11000.0
# 40.0      6500.0  6500.0  6500.0
# 50.0      2100.0  3100.0  8200.0
# 3）多个列计算不同的统计值
# 也可以在agg()中传入字典，对多个列计算不同的统计值。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
# 按department_id分组，统计job_id的种类数，commission_pct的平均值
print(df.groupby("department_id").agg({"job_id": "nunique", "commission_pct": "mean"}))
#        job_id commission_pct
# department_id
# 10.0        1       NaN
# 20.0        2       NaN
# 30.0        2       NaN
# 40.0        1       NaN
# 50.0        3       NaN
# 4）重命名统计值
# 可以在agg()后通过rename()对统计后的列重命名。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
# 按department_id分组，统计job_id的种类数，commission_pct的平均值
print(
  df.groupby("department_id")
  .agg(
    {"job_id": "nunique", "commission_pct": "mean"},
  )
  .rename(
    columns={"job_id": "工种数", "commission_pct": "佣金比例平均值"},
  )
)
#        工种数 佣金比例平均值
# department_id
# 10.0       1   NaN
# 20.0       2   NaN
# 30.0       2   NaN
# 40.0       1   NaN
# 50.0       3   NaN
# 5）自定义函数
# 可以向agg()中传入自定义函数进行计算。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据

def f(x):
  """统计每个部门员工last_name的首字母"""
  result = set()
  for i in x:
    result.add(i[0])
  return result

print(df.groupby("department_id")["last_name"].agg(f))
# department_id
# 10.0                          {W}
# 20.0                        {F, H}
# 30.0                  {B, T, R, C, K, H}
# 40.0                          {M}
# 50.0   {O, E, K, S, W, L, P, D, C, V, B, T, M, J, F, ...
# 3.9.3分组转换
# 聚合操作返回的是对组内全量数据缩减过的结果，而转换操作会返回一个新的全量数据。数据经过转换之后，其形状与原来的输入数据是一样的。
# 1）通过transform()将每一组的样本数据减去各组的均值，实现数据标准化
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
print(df.groupby("department_id")["salary"].transform(lambda x: x - x.mean()))
# 0   4666.666667
# 1   -2333.333333
# 2   -2333.333333
# 3   3240.000000
# 4    240.000000
# 2）通过transform()按分组使用平均值填充缺失值
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
na_index = pd.Series(df.index.tolist()).sample(30) # 随机挑选30条数据
df.loc[na_index, "salary"] = pd.NA # 将这30条数据的salary设置为缺失值
print(df.groupby("department_id")["salary"].agg(["size", "count"])) # 查看每组数据总数与非空数据数

def fill_missing(x):
  # 使用平均值填充，如果平均值也为NaN，用0填充
  if np.isnan(x.mean()):
    return 0
  return x.fillna(x.mean())

df["salary"] = df.groupby("department_id")["salary"].transform(fill_missing)
print(df.groupby("department_id")["salary"].agg(["size", "count"])) # 查看每组数据总数与非空数据数
# 3.9.4分组过滤
# 过滤操作可以让我们按照分组的属性丢弃若干数据。
# 例如，我们可能只需要保留commission_pct不包含空值的分组的数据。
commission_pct_filter = df.groupby("department_id").filter(
  lambda x: x["commission_pct"].notnull().all()
) # 按department_id分组，过滤掉commission_pct包含空值的分组
print(commission_pct_filter)