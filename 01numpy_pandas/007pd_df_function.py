import pandas as pd
s = pd.Series([1, 2, 3, 4, 5])
s1 = s.apply(lambda x: x**2)#对s的每个元素应用一个函数，这里是平方函数
s2 = s.apply(lambda x: x**3)#对s的每个元素应用一个函数，这里是立方函数

df = pd.DataFrame({'s': s, 's_squared': s1, 's_cubed': s2})#创建一个DataFrame对象，包含s、s_squared和s_cubed三列
print(df)

df = pd.DataFrame({'s': s, 's_squared': s1, 's_cubed': s2}, index=[0,1,2,3,4],columns=['s', 's_squared', 's_cubed'])#创建一个带有索引的DataFrame对象，包含s、s_squared和s_cubed三列
print(df)

print(df.shape)#查看df的形状
print(df.ndim)#查看df的维数
print(df.size)#查看df的元素个数
print(df.dtypes)#查看df中每列的数据类型
print(df.head(3))#查看df的前3行
print(df.tail(2))#查看df的后2行
print(df.describe())#查看df的统计信息
print(df.sum())#计算df中每列的元素之和
print(df.mean())#计算df中每列的元素的平均值
print(df.median())#计算df中每列的元素的中位数
print(df.mode())#计算df中每列的元素的众数
print(df.loc[0])#通过标签索引访问df的行
print(df.iloc[0])#通过位置索引访问df的行
print(df.loc[0:2])#通过标签索引访问df的行，包含结束标签
print(df.iloc[0:3])#通过位置索引访问df的行，不包含结束位置
print(df.loc[0, 's'])#通过标签索引访问df的元素
print(df.iloc[0, 0])#通过位置索引访问df的元素  
print(df.at[0, 's'])#使用标签进行访问单个元素
print(df.iat[0, 0])#使用位置进行访问单个元素

print(df.T)#转置df
print(df.values)#查看df的值
print(df.columns)#查看df的列索引
print(df.index)#查看df的行索引
