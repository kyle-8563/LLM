import pandas as pd
import numpy as np

# 创建示例数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 75000, 55000],
    'date': pd.date_range('2024-01-01', periods=4)
}
df = pd.DataFrame(data)
print(df)
#日期类型
df["ymd"] = pd.to_datetime(df["date"])
print(df)
# 获取年月日
df["yy"],df["mm"],df["dd"] = df['ymd'].dt.year,df['ymd'].dt.month,df['ymd'].dt.day
print(df)
# df获取统计周期
df["dayofweek"] = df['ymd'].dt.dayofweek  # 0=Monday, 6=Sunday
df["quarter"] = df['ymd'].dt.quarter
df["week"] = df['ymd'].dt.isocalendar().week
print(df)
# 转换为period类型
df["period"] = df['ymd'].dt.to_period('M')  # M=Month, D=Day, Y=Year, Q=Quarter
print(df)



