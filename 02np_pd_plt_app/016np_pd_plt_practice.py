import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.sans-serif"] = ["SimHei"] # 指定中文字体

# 读取 CSV 文件
data = pd.read_csv(r'D:\Code\learn\LLM\02np_pd_plt_app\data\house_sales.csv')
print('数据基本信息：')
data.info()
# 2）代码说明
# 使用pandas的read_csv函数读取house_sales.csv文件，将数据存储在DataFrame对象data中，方便后续处理，并查看数据基本信息。
# 4.4.2数据清洗
# 1）代码
# 检查缺失值
missing_values = data.isnull().sum()
print('各列缺失值数量：')
print(missing_values)

# 处理缺失值，这里简单地删除包含缺失值的行
data = data.dropna()

# 检查异常值，以房价为例，使用 IQR 方法
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['price'] >= lower_bound) & (data['price'] <= upper_bound)]

# 2）代码说明
# 缺失值处理：使用isnull().sum()统计各列缺失值数量，然后用dropna()删除包含缺失值的行。
# 异常值处理：使用 IQR（Inter - Quartile Range，四分位距）方法来检测和处理房价数据中的异常值。以房价为例，通过计算第一四分位数Q1、第三四分位数Q3和四分位距IQR，确定上下限，筛选出合理范围内的数据。
# data['price'].quantile(0.25)：quantile是pandas中用于计算分位数的方法。这里0.25表示计算 25% 分位数，也就是第一四分位数Q1。第一四分位数意味着有 25% 的数据小于这个值。
# data['price'].quantile(0.75)：同理，0.75表示计算 75% 分位数，即第三四分位数Q3。有 75% 的数据小于这个值。
# 四分位距IQR是第三四分位数Q3与第一四分位数Q1的差值。它衡量了数据中间 50% 的数据的分散程度。
# lower_bound：通过Q1 - 1.5 * IQR计算出异常值的下限。如果某个数据点小于这个下限，就可能被视为异常值。
# upper_bound：通过Q3 + 1.5 * IQR计算出异常值的上限。如果某个数据点大于这个上限，也可能被视为异常值。
# 这里的1.5是一个常用的系数，在很多情况下可以有效地识别出大部分异常值，但在某些特殊场景下可能需要调整。
# 使用布尔索引来筛选数据。(data['price'] >= lower_bound) & (data['price'] <= upper_bound)表示筛选出price列中值大于等于下限且小于等于上限的数据，将这些数据重新赋值给data，从而去除了可能的异常值。
# 4.4.3数据类型转换
# 1）代码
# 将日期列转换为日期类型
data['date'] = pd.to_datetime(data['date'])
# 2）代码说明
# 使用pandas的to_datetime函数将date列转换为日期类型，便于进行时间序列分析。
# 4.4.4创建新的特征
# 1）代码
# 计算房屋的使用年限
data['age'] = data['date'].dt.year - data['yr_built']
# 创建新特征：是否翻新
data['is_renovated'] = data['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)
# 2）代码说明
# 计算房屋使用年限：通过销售日期的年份减去建造年份，得到房屋的使用年限，存储在新列age中，这个特征可能会对房价产生影响。
# 创建是否翻新特征：使用apply方法和lambda函数对yr_renovated列进行判断，若值大于 0 则表示房屋已翻新，将is_renovated列对应的值设为 1，否则设为 0，以便后续分析翻新因素对房价的影响。
# 4.4.5数据探索性分析-描述性统计
# 1）代码
# 选择数值型列
numeric_columns = data.select_dtypes(include=[np.number]).columns
# 计算描述性统计信息
description = data[numeric_columns].describe(percentiles=[0.25, 0.5, 0.75])
print('数值型列的描述性统计：')
print(description)
# 2）代码说明
data.select_dtypes(include=[np.number])#选择数据集中的数值型列，并获取其列名存储在numeric_columns中。
data[numeric_columns].describe(percentiles=[0.25, 0.5, 0.75])#计算数值型列的描述性统计信息，包括均值、中位数、标准差、最小值、最大值、四分位数等，并将结果存储在description中，帮助我们了解各数值特征的分布情况。
# 4.4.6数据探索性分析-相关性统计
# 1）代码
# 计算不同特征与房价的相关性
correlation = data[numeric_columns].corr()
print('各特征与房价的相关性：')
print(correlation['price'])
# 2）代码说明
# 对数值型列使用corr方法计算相关系数矩阵，提取price列得到各特征与房价的相关性。
# 4.4.7按照邮政编码分组分析
# 1）代码
# 按邮政编码分组，计算每组的平均房价、平均居住面积、平均卧室数量
zipcode_stats = data.groupby('zipcode').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
zipcode_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('不同邮政编码区域的统计信息：')
print(zipcode_stats)
# 2）代码说明
# 使用data.groupby('zipcode')按邮政编码对数据进行分组。
# agg方法对分组后的数据进行聚合操作，分别计算每组的平均房价、平均居住面积和平均卧室数量。
# 对结果的列名进行重命名，使其更具可读性，并打印输出，可对比不同邮政编码区域的房屋特征情况。
# 4.4.8按照是否翻新分组分析
# 1）代码
# 按是否翻新分组，计算每组的平均房价、平均居住面积、平均卧室数量
renovation_stats = data.groupby('is_renovated').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
renovation_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('是否翻新分组的统计信息：')
print(renovation_stats)
# 2）代码说明
# 按is_renovated特征对数据进行分组，分析翻新和未翻新房屋在房价、居住面积和卧室数量等方面的差异。同样使用agg方法进行聚合计算，得到相应的统计信息并打印。
# 4.4.9按照房龄分组分析
# 1）代码
# 按房屋使用年限分组（简单分为 5 个区间）
data['age_group'] = pd.cut(data['age'], bins=5)
age_stats = data.groupby('age_group').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
print('按房屋使用年限分组的统计信息：')
print(age_stats)
# 2）代码说明
# 使用pd.cut函数将房屋使用年限age划分为 5 个区间，创建新列age_group。
# 按age_group分组，计算每组的平均房价、平均居住面积和平均卧室数量，了解不同使用年限房屋的特征差异。
# 4.4.10时间序列分析-每年平均房价
# 1）代码
# 按年份分组，计算每年的平均房价
yearly_avg_price = data.groupby(data['date'].dt.year)['price'].mean()
print('每年的平均房价：')
print(yearly_avg_price)
# 2）代码说明
# 使用data.groupby(data['date'].dt.year)按销售日期的年份对数据进行分组。
# 对每组的price列计算均值，得到每年的平均房价，并存储在yearly_avg_price中进行打印输出，可观察房价随时间的变化趋势。
# 4.4.11时间序列分析-不同翻新情况平均房价
# 1）代码
# 按年份和是否翻新分组，计算每年不同翻新情况的平均房价
yearly_renovation_avg_price = data.groupby([data['date'].dt.year, 'is_renovated'])['price'].mean()
print('每年不同翻新情况的平均房价：')
print(yearly_renovation_avg_price)
# 2）代码说明
# 按销售年份和是否翻新进行分组，计算每年翻新和未翻新房屋的平均房价，能让我们看到在不同年份，翻新因素对房价的影响变化。
# 4.4.12可视化
# 1）房价分布直方图
# 房价分布直方图
plt.figure(figsize=(10, 6))
plt.hist(data['price'], bins=30, edgecolor='k')
plt.title('房价分布直方图')
plt.xlabel('房价')
plt.ylabel('频数')
plt.show()
# 使用plt.hist函数绘制房价的分布直方图，bins=30控制柱子的数量，edgecolor='k'为柱子添加黑色边框。添加标题和坐标轴标签，使图形更易理解，最后使用plt.show()显示图形。
# 2）卧室数量与房价的散点图
# 卧室数量与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['bedrooms'], data['price'])
plt.title('卧室数量与房价的关系')
plt.xlabel('卧室数量')
plt.ylabel('房价')
plt.show()
# 使用plt.scatter函数绘制卧室数量与房价的散点图，直观展示两者之间的关系。
# 3）各特征与房价的相关性热力图
# 各特征与房价的相关性热力图
plt.figure(figsize=(12, 8))
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title('各特征与房价的相关性热力图')
plt.show()
# 使用plt.imshow函数绘制相关性热力图，cmap='coolwarm'设置颜色映射，interpolation='nearest'控制插值方式。添加颜色条和坐标轴标签，显示各特征与房价的相关性，最后显示图形。
# 4）不同邮政编码区域平均房价的柱状图
# 不同邮政编码区域平均房价的柱状图
plt.figure(figsize=(12, 6))
plt.bar(zipcode_stats.index.astype(str), zipcode_stats['avg_price'])
plt.title('不同邮政编码区域的平均房价')
plt.xlabel('邮政编码')
plt.ylabel('平均房价')
plt.xticks(rotation=45)
plt.show()
# 使用plt.bar函数绘制不同邮政编码区域平均房价的柱状图，将zipcode转换为字符串类型。设置图形标题和坐标轴标签，旋转 x 轴标签避免重叠后显示图形。
# 5）每年平均房价的折线图
# 每年平均房价的折线图
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_price.index, yearly_avg_price)
plt.title('每年平均房价趋势')
plt.xlabel('年份')
plt.ylabel('平均房价')
plt.show()
# 使用plt.plot函数绘制每年平均房价的折线图，展示房价随时间的变化趋势。
# 6）不同翻新情况的房价箱线图
# 不同翻新情况的房价箱线图
plt.figure(figsize=(10, 6))
data.boxplot(column='price', by='is_renovated')
plt.title('不同翻新情况的房价箱线图')
plt.xlabel('是否翻新')
plt.xticks([1, 2], ['未翻新', '已翻新'])
plt.ylabel('房价')
plt.suptitle('') # 去掉默认的标题
plt.show()
# 使用data.boxplot方法绘制不同翻新情况的房价箱线图，展示翻新和未翻新房屋房价的分布情况
# 7）房屋使用年限与房价的散点图
# 房屋使用年限与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['price'])
plt.title('房屋使用年限与房价的关系')
plt.xlabel('房屋使用年限')
plt.ylabel('房价')
plt.show()
# 使用plt.scatter函数绘制房屋使用年限与房价的散点图，观察两者之间的关系。
# 4.4.13完整代码
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.sans-serif"] = ["SimHei"] # 指定中文字体

# 读取 CSV 文件
data = pd.read_csv(r'D:\Code\learn\LLM\02np_pd_plt_app\data\house_sales.csv')
print('数据基本信息：')
data.info()

# 检查缺失值
missing_values = data.isnull().sum()
print('各列缺失值数量：')
print(missing_values)

# 处理缺失值，这里简单地删除包含缺失值的行
data = data.dropna()

# 检查异常值，以房价为例，使用 IQR 方法
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['price'] >= lower_bound) & (data['price'] <= upper_bound)]

# 将日期列转换为日期类型
data['date'] = pd.to_datetime(data['date'])

# 计算房屋的使用年限
data['age'] = data['date'].dt.year - data['yr_built']
# 创建新特征：是否翻新
data['is_renovated'] = data['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)

# 选择数值型列
numeric_columns = data.select_dtypes(include=[np.number]).columns
# 计算描述性统计信息
description = data[numeric_columns].describe(percentiles=[0.25, 0.5, 0.75])
print('数值型列的描述性统计：')
print(description)

# 计算不同特征与房价的相关性
correlation = data[numeric_columns].corr()
print('各特征与房价的相关性：')
print(correlation['price'])

# 按邮政编码分组，计算每组的平均房价、平均居住面积、平均卧室数量
zipcode_stats = data.groupby('zipcode').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
zipcode_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('不同邮政编码区域的统计信息：')
print(zipcode_stats)

# 按是否翻新分组，计算每组的平均房价、平均居住面积、平均卧室数量
renovation_stats = data.groupby('is_renovated').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
renovation_stats.columns = ['avg_price', 'avg_sqft_living', 'avg_bedrooms']
print('是否翻新分组的统计信息：')
print(renovation_stats)

# 按房屋使用年限分组（简单分为 5 个区间）
data['age_group'] = pd.cut(data['age'], bins=5)
age_stats = data.groupby('age_group').agg({
  'price': 'mean',
  'sqft_living': 'mean',
  'bedrooms': 'mean'
})
print('按房屋使用年限分组的统计信息：')
print(age_stats)

# 按年份分组，计算每年的平均房价
yearly_avg_price = data.groupby(data['date'].dt.year)['price'].mean()
print('每年的平均房价：')
print(yearly_avg_price)

# 按年份和是否翻新分组，计算每年不同翻新情况的平均房价
yearly_renovation_avg_price = data.groupby([data['date'].dt.year, 'is_renovated'])['price'].mean()
print('每年不同翻新情况的平均房价：')
print(yearly_renovation_avg_price)

# 房价分布直方图
plt.figure(figsize=(10, 6))
plt.hist(data['price'], bins=30, edgecolor='k')
plt.title('房价分布直方图')
plt.xlabel('房价')
plt.ylabel('频数')
plt.show()

# 卧室数量与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['bedrooms'], data['price'])
plt.title('卧室数量与房价的关系')
plt.xlabel('卧室数量')
plt.ylabel('房价')
plt.show()

# 各特征与房价的相关性热力图
plt.figure(figsize=(12, 8))
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title('各特征与房价的相关性热力图')
plt.show()

# 不同邮政编码区域平均房价的柱状图
plt.figure(figsize=(12, 6))
plt.bar(zipcode_stats.index.astype(str), zipcode_stats['avg_price'])
plt.title('不同邮政编码区域的平均房价')
plt.xlabel('邮政编码')
plt.ylabel('平均房价')
plt.xticks(rotation=45)
plt.show()

# 每年平均房价的折线图
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_price.index, yearly_avg_price)
plt.title('每年平均房价趋势')
plt.xlabel('年份')
plt.ylabel('平均房价')
plt.show()

# 不同翻新情况的房价箱线图
plt.figure(figsize=(10, 6))
data.boxplot(column='price', by='is_renovated')
plt.title('不同翻新情况的房价箱线图')
plt.xlabel('是否翻新')
plt.xticks([1, 2], ['未翻新', '已翻新'])
plt.ylabel('房价')
plt.suptitle('') # 去掉默认的标题
plt.show()

# 房屋使用年限与房价的散点图
plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['price'])
plt.title('房屋使用年限与房价的关系')
plt.xlabel('房屋使用年限')
plt.ylabel('房价')
plt.show()
