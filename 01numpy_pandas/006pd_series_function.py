import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))#查看s的类型
print(s.values)#查看s的值
print(s.index)#查看s的索引

s  = pd.Series(data = [1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e' ])#创建一个带有索引的Series对象
print(s)
s=pd.Series([1,2,3,4],index=['a','b','c','d'])#创建一个带有索引的Series对象
print(s)
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}#创建一个字典对象
s = pd.Series(dict)#创建一个Series对象，索引为字典的键，值为字典的值
print(s)    

print(pd.Series(5, index=['a', 'b', 'c', 'd'], name="Series Name"))#创建一个带有索引的Series对象，值为5


print(s.ndim)#查看s的维数
print(s.shape)#查看s的形状
print(s.size)#查看s的元素个数
print(s.dtype)#查看s的数据类型
print(s.name)#查看s的名称
print(s.head(3))#查看s的前3个元素
print(s.tail(2))#查看s的后2个元素
print(s.describe())#查看s的统计信息
print(s.sum())#计算s的元素之和
print(s.mean())#计算s的元素的平均值
print(s.median())#计算s的元素的中位数
print(s.mode())#计算s的元素的众数
print(s.loc["c"])#通过标签索引访问s的元素
print(s.iloc[2])#通过位置索引访问s的元素
print(s.loc["b":"d"])#通过标签索引访问s的元素，包含结束标签
print(s.iloc[1:4])#通过位置索引访问s的元素，不包含结束位置
print(s.iat[2])#使用位置进行访问单个元素
print(s.at["c"])#使用标签进行访问单个元素

print(s.isin([2, 3]))#判断s的元素是否在给定的列表中
print(s[s.isin([2, 3])])#筛选s的元素，保留在给定的列表中的元素

print(s.apply(lambda x: x**2))#对s的每个元素应用一个函数，这里是平方函数 
print(s.mean())#计算s的元素的平均值
print(s.std())#计算s的元素的标准差
print(s.var())#计算s的元素的方差
print(s.min())#计算s的元素的最小值
print(s.max())#计算s的元素的最大值
print(s.value_counts())#计算s中每个唯一值的出现次数
print(s.unique())#返回s中唯一的元素

print(s.sum())#计算s的元素之和
print(s.cumsum())#计算s的元素的累积和q
print(s.cumprod())#计算s的元素的累积积
print(s.diff())#计算s的元素的离散差分
print(s.pct_change())#计算s的元素的百分比变化

print(s.quantile(0.25))#计算s的元素的第25百分位数
print(s.quantile(0.5))#计算s的元素的第50百分位数
print(s.quantile(0.75))#计算s的元素的第75百分位数

print(s.describe())#查看s的统计信息
print(len(s))#计算s的元素个数
print(s.count())#计算s的非NA/null元素个数

print(s.dropna())#返回一个新的Series对象，删除s中的NA/null元素
print(s.fillna(0))#返回一个新的Series对象，将s中的NA/null元素替换为0
print(s.isna())#返回一个布尔Series对象，表示s中的元素是否是NA/null
print(s.notna())#返回一个布尔Series对象，表示s中的元素是否不是NA/null

print(s.drop_duplicates())#返回一个新的Series对象，删除s中的重复元素
print(s.duplicated())#返回一个布尔Series对象，表示s中的元素是否是重复的 

print(s.sample(frac=0.5))#从s中随机抽取50%的元素
print(s.sample(n=2))#从s中随机抽取2个元素

print(s.sort_values())#返回一个新的Series对象，按照值进行排序
print(s.sort_index())#返回一个新的Series对象，按照索引进行排序
print(s.replace(2, 20))#返回一个新的Series对象，将s中的值2替换为20
print(s.rename("New Series Name"))#返回一个新的Series对象，重命名s的名称为"New Series Name"

print(s.astype(float))#返回一个新的Series对象，将s的元素类型转换为float
print(s.astype(str))#返回一个新的Series对象，将s的元素类型转换为str

print(s.copy())#返回s的一个副本
print(s.view())#返回s的一个视图，修改视图会影响原始Series对象

print(s.to_frame())#将s转换为一个DataFrame对象
print(s.to_dict())#将s转换为一个字典对象

print(s.equals(s.copy()))#判断s是否与其副本相等
print(s.equals(s.view()))#判断s是否与其视图相等
print(s.keys())#返回s的索引标签

print(s.corr(s))#计算s与自身的相关系数
print(s.corr(s + 1))#计算s与s+1的相关系数
print(s.corr(s * 2))#计算s与s*2的相关系

print(s.cov(s))#计算s与自身的协方差
print(s.cov(s + 1))#计算s与s+1的协方差
from matplotlib import pyplot as plt    
s.hist(bins=3)#绘制s的直方图
# plt.show()#显示图形
s.plot(kind='line')#绘制s的折线图
# plt.show()#显示图形

s.plot(kind='bar')#绘制s的柱状图
# plt.show()#显示图形

s.plot(kind='barh')#绘制s的水平柱状图
# plt.show()#显示图形
for i,v in s.items():
    print(i,v)

print(s[s > 2])#筛选s的元素，保留大于2的元素
print(s[s>s.mean()])#筛选s的元素，保留大于s的平均值的元素

print(s+s)#对s进行元素级的加法运算
print(s-s)#对s进行元素级的减法运算
print(s*s)#对s进行元素级的乘法运算
print(s/s)#对s进行元素级的除法运算