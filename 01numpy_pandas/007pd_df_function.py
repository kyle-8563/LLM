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

df=pd.DataFrame(data={"id": [101,102,103,104,105,106,101],"name":["ʊŎ","ʋȜ","ʌȞ","ʓȟ","ʔʕ","ʏʖ","ʊŎ"],"age": [10,20,30,40,None,60,10]},index=["aa","bb","cc","dd","ee","ff","aa"])
print(df)
print(df.head())#查看df的前5行
print(df.tail())#查看df的后5行
print(df.isin([10, 20]))#判断df的元素是否在给定的列表中
print(df.sum())#计算df中每列的元素之和
print(df.age.mean())#计算df中每列的元素的平均值
print(df.age.median())#计算df中每列的元素的中位数
print(df.age.mode())#计算df中每列的元素的众数   
print(df.age.quantile(0.25))#计算df中每列的元素的第25百分位数
print(df.age.quantile(0.5))#计算df中每列的元素的第50百分位数
print(df.age.quantile(0.75))#计算df中每列的元素的第75百分位数
print(df.age.value_counts())#计算df中age列每个唯一值的出现次数
print(df.age.unique())#返回df中age列唯一的元素
print(df.describe(include='all'))#查看df的统计信息
print(df.info())#查看df的基本信息
print(df[['age']].corr())#计算df中数值列之间的相关系数
print(df[['age']].cov())#计算df中数值列之间的协方差
print(df.equals(df))#判断df是否与自身相等
print(df.equals(df.T))#判断df是否与其转置相等
print(df.sample(frac=0.5, random_state=0))#随机抽取df的50%的行，设置随机种子为0
print(df.sample(n=3, random_state=0))#随机抽取df的3行，设置随机种子为0

print(df.cummax())#计算df中每列的累积最大值
print(df.cummin())#计算df中每列的累积最小值
print(df.age.cumsum())#计算df中每列的累积和
print(df.age.cumprod())#计算df中每列的累积积

print(df.age.diff())#计算df中每列的离散差分
print(df.age.pct_change())#计算df中每列的百分比变化

print(df.replace(10, 100))#将df中所有的10替换为100
print(df.rename(columns={'age': 'age_years'}))#将df中的列名
print(df.drop_duplicates())#删除df中的重复行
print(df.dropna())#删除df中的NA/null行

print(df.sort_values(by='age'))#按照age列的值进行排序
print(df.sort_values(by='age', ascending=False))#按照age列的值进行降序排序
print(df.sort_index())#按照行索引进行排序

print(df.groupby('age').size())#按照age列进行分组，并计算每个组的大小
print(df.nsmallest(3, 'age'))#返回df中age列最小的3行
print(df.nlargest(3, 'age'))#返回df中age列最大的3行