import pandas as pd
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\employees.csv") # 读取员工数据
print(df.groupby("department_id")) # 按department_id分组，返回DataFrameGroupBy对象
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024FCBAFD700>
# 这个对象可以看成是一种特殊形式的 DataFrame，里面隐藏着若干组数据，但是在没有应用累计函数之前不会计算。GroupBy对象是一种非常灵活的抽象类型。在大多数场景中，可以将它看成是DataFrame的集合。
# 1）查看分组
# 通过groups属性查看分组结果，返回一个字典，字典的键是分组的标签，值是属于该组的所有索引的列表。
print(df.groupby("department_id").groups) # 查看分组结果
# {10.0: [100], 20.0: [101, 102], 30.0: [14, 15, 16, 17, 18, 19]...
# 通过get_group()方法获取分组。
print(df.groupby("department_id").get_group(50)) # 获取分组为50的数据
#   employee_id first_name  last_name   email...
# 20     120  Matthew    Weiss  MWEISS...
# 21     121    Adam    Fripp  AFRIPP...
# 22     122   Payam   Kaufling PKAUFLIN...
# 2）按列取值
print(df.groupby("department_id")["salary"]) # 按department_id分组，取salary列
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x0000022456D6F2F0>
# 这里从原来的DataFrame中取某个列名作为一个Series组。与GroupBy对象一样，直到我们运行累计函数，才会开始计算。
print(df.groupby("department_id")["salary"].mean()) # 计算每个部门平均薪资
# department_id
# 10.0   4400.000000
# 20.0   9500.000000
# 30.0   4150.000000
# 3）按组迭代
# GroupBy对象支持直接按组进行迭代，返回的每一组都是Series或DataFrame。
for dept_id,group in df.groupby("department_id"):
  print(f"当前组为{dept_id}，组里的数据情况{group.shape}:")
  print(group.iloc[:,0:3])
  print("-------------------")
# 当前组为10.0，组里的数据情况(1, 10):
#   employee_id first_name last_name
# 100     200  Jennifer  Whalen
# -------------------
# 当前组为20.0，组里的数据情况(2, 10):
#   employee_id first_name last_name
# 101     201  Michael Hartstein
# 102     202    Pat    Fay
...
# 4）按多字段分组
salary_mean = df.groupby(["department_id", "job_id"])[
  ["salary", "commission_pct"]
].mean() # 按department_id和job_id分组
print(salary_mean.index) # 查看分组后的索引
# MultiIndex([( 10.0,  'AD_ASST'),
#       ( 20.0,   'MK_MAN'),
#       ( 20.0,   'MK_REP'),
#       ( 30.0,  'PU_CLERK'),
#       ( 30.0,   'PU_MAN'),
#       ...
print(salary_mean.columns) # 查看分组后的列
# Index(['salary', 'commission_pct'], dtype='object')
# 按多个字段分组后得到的索引为复合索引。
# 可通过reset_index()方法重置索引。
print(salary_mean.reset_index())
#   department_id   job_id    salary commission_pct
# 0      10.0   AD_ASST  4400.000000       NaN
# 1      20.0   MK_MAN 13000.000000       NaN
# 2      20.0   MK_REP  6000.000000       NaN
# 3      30.0  PU_CLERK  2780.000000       NaN
# 4      30.0   PU_MAN 11000.000000       NaN
# 也可以在分组的时候通过as_index = False参数（默认是True）重置索引。
salary_mean = df.groupby(["department_id", "job_id"], as_index=False)[
  ["salary", "commission_pct"]
].mean() # 按department_id和job_id分组
print(salary_mean)
#   department_id   job_id    salary commission_pct
# 0      10.0   AD_ASST  4400.000000       NaN
# 1      20.0   MK_MAN 13000.000000       NaN
# 2      20.0   MK_REP  6000.000000       NaN
# 3      30.0  PU_CLERK  2780.000000       NaN
# 4      30.0   PU_MAN 11000.000000       NaN