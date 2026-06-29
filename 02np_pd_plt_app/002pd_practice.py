import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv(r"D:\code\02np_pd_plt_app\data\employees.csv")
print(df.head()) # 查看前5行
df.info()# 查看数据信息
print(df.describe()) # 查看统计信息
print(df.shape) # 查看数据形状


print(df[df["salary"] == df["salary"].min()]) # 找出最低薪资的员工
print(df.loc[df["salary"] == df["salary"].min()]) # 找出最低薪资的员工
print(df.loc[df["salary"] == df["salary"].max()]) # 找出最高薪资的员工

print(df.sort_values("salary").head(1)) # 使用排序的方法找出最低薪资的员工
print(df.sort_values("salary", ascending=False).head(1)) # 使用排序的方法找出最高薪资的员工

# 4）找出薪资最高的10名员工
print(df.nlargest(10, "salary")) # 薪资最高的10名员工
# 5）查看所有部门id
print(df["department_id"].unique()) # 所有部门id
# 6）查看每个部门的员工数
print(df.groupby("department_id")["employee_id"].count().rename("employee_count")) # 查看每个部门的员工数
# 7）绘图
df.groupby("department_id")["employee_id"].count().rename("employee_count").plot(kind="bar")
# plt.show()

# 8）薪资的分布
print(df["salary"].mean()) # 平均值
print(df["salary"].std()) # 标准差
print(df["salary"].median()) # 中位数
# 9）找出平均薪资最高的部门id
print(df.groupby("department_id")["salary"].mean().nlargest(1)) # 平均薪资最高的部门