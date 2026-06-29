# 3.11Pandas时间序列
# 3.11.1Python中的日期与时间工具
# Python基本的日期与时间功能都在标准库的datetime模块中。
from datetime import datetime
import pandas as pd
date1 = datetime(year=2000, month=1, day=1)
date2 = datetime.now()
print(date1) # 2000-01-01 00:00:00
print(date2) # 2025-01-01 00:00:00
print(date1.year) # 2000
print(date1.month) # 1
print(date1.day) # 1
print(date2.weekday()) # 5
print(date2.strftime("%A")) # Saturday
print(date2 - date1) # 18263 days, 0:00:00
# 3.11.2pandas中的日期与时间
# pandas的日期时间类型默认是datetime64[ns]。
# 针对时间戳数据，pandas提供了Timestamp类型。它本质上是Python原生datetime类型的替代品，但是在性能更好的numpy.datetime64类型的基础上创建。对应的索引数据结构是DatetimeIndex。
# 针对时间周期数据，pandas提供了Period类型。这是利用numpy.datetime64类型将固定频率的时间间隔进行编码。对应的索引数据结构是PeriodIndex。
# 针对时间增量或持续时间，pandas提供了Timedelta类型。Timedelta是一种代替Python原生datetime.timedelta类型的高性能数据结构，同样是基于numpy.timedelta64类型。对应的索引数据结构是TimedeltaIndex。
# 1）datetime64
# to_datetime()可以解析许多日期与时间格式。对to_datetime()传递一个日期会返回一个Timestamp类型，传递一个时间序列会返回一个DatetimeIndex类型。
# 注意：Timestamp 是 pandas 对 datetime64 数据类型的一个封装。datetime64 是 NumPy 中的一种数据类型，用于表示日期和时间，而 pandas 基于 datetime64 构建了 Timestamp 类，以便更方便地在 pandas 的数据结构（如 DataFrame 和 Series）中处理日期时间数据。当 pd.to_datetime 接收单个日期时间值时，会返回 Timestamp 对象。不过，要是使用 dtype 属性查看，得到的却是 datetime64[ns]，这是因为 dtype 反映的是底层存储的数据类型，而 Timestamp 对象底层存储的数据类型就是 datetime64[ns]。
print(pd.to_datetime("2015-01-01"))
# 2015-01-01 00:00:00
print(pd.to_datetime(["4th of July, 2015", "2015-Jul-6", "07-07-2015", "20150708"], format="mixed"))
# DatetimeIndex(['2015-07-04', '2015-07-06', '2015-07-07', '2015-07-08'], dtype='datetime64[ns]', freq=None)
# 在加载数据时，可以通过to_datetime()将数据中的列解析为datetime64。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
print(df["date"].tail())
# 1456  2015-12-27
# 1457  2015-12-28
# 1458  2015-12-29
# 1459  2015-12-30
# 1460  2015-12-31
# Name: date, dtype: object
print(pd.to_datetime(df["date"]).tail())
# 1456  2015-12-27
# 1457  2015-12-28
# 1458  2015-12-29
# 1459  2015-12-30
# 1460  2015-12-31
# Name: date, dtype: datetime64[ns]
# 在加载数据时也可以通过parse_dates参数将指定列解析为datetime64。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv", parse_dates=[0])
print(df["date"].tail())
# 1456  2015-12-27
# 1457  2015-12-28
# 1458  2015-12-29
# 1459  2015-12-30
# 1460  2015-12-31
# Name: date, dtype: datetime64[ns]
# 2）提取日期的各个部分
# （1）提取Timestamp
d = pd.Timestamp("2015-01-01 09:08:07.123456")
print(d.year) # 2015
print(d.month) # 1
print(d.day) # 1
print(d.hour) # 9
print(d.minute) # 8
print(d.second) # 7
print(d.microsecond) # 123456
# （2）对于Series对象，需要使用dt访问器
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv", parse_dates=[0])
df_date = pd.to_datetime(df["date"])
df["year"] = df_date.dt.year
df["month"] = df_date.dt.month
df["day"] = df_date.dt.day
print(df[["date", "year", "month", "day"]].tail())
#      date year month day
# 1456 2015-12-27 2015   12  27
# 1457 2015-12-28 2015   12  28
# 1458 2015-12-29 2015   12  29
# 1459 2015-12-30 2015   12  30
# 1460 2015-12-31 2015   12  31
# 3）period
# 可以通过to_period()方法和一个频率代码将datetime64类型转换成period类型。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
df["quarter"] = pd.to_datetime(df["date"]).dt.to_period("Q") # 将 年-月-日 转换为 年季度
print(df[["date", "quarter"]].head())
#     date quarter
# 0 2012-01-01 2012Q1
# 1 2012-01-02 2012Q1
# 2 2012-01-03 2012Q1
# 3 2012-01-04 2012Q1
# 4 2012-01-05 2012Q1
# 4）timedelta64
# 当用一个日期减去另一个日期，返回的结果是timedelta64类型。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv", parse_dates=[0])
df_date = pd.to_datetime(df["date"])
timedelta = df_date - df_date[0]
print(timedelta.head())
# 0  0 days
# 1  1 days
# 2  2 days
# 3  3 days
# 4  4 days
# Name: date, dtype: timedelta64[ns]
# 3.11.3使用时间作为索引
# 1）DatetimeIndex
# 将datetime64类型的数据设置为索引，得到的就是DatetimeIndex。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
df["date"] = pd.to_datetime(df["date"]) # 将date列转换为datetime64类型
df.set_index("date", inplace=True) # 将date列设置为索引
df.info()
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 1461 entries, 2012-01-01 to 2015-12-31
# 将时间作为索引后可以直接使用时间进行切片取值。
print(df.loc["2013-01":"2013-06"]) # 获取2013年1~6月的数据
#       precipitation temp_max temp_min wind weather
# date
# 2013-01-01      0.0    5.0   -2.8  2.7   sun
# 2013-01-02      0.0    6.1   -1.1  3.2   sun
# ...          ...    ...    ...  ...   ...
# 2013-06-29      0.0   30.0   18.3  1.7   sun
# 2013-06-30      0.0   33.9   17.2  2.5   sun
print(df.loc["2015"]) # 获取2015年所有数据
#       precipitation temp_max temp_min wind weather
# date
# 2015-01-01      0.0    5.6   -3.2  1.2   sun
# 2015-01-02      1.5    5.6    0.0  2.3  rain
# ...          ...    ...    ...  ...   ...
# 2015-12-30      0.0    5.6   -1.0  3.4   sun
# 2015-12-31      0.0    5.6   -2.1  3.5   sun
# 也可以通过between_time()和at_time()获取某些时刻的数据。
df.between_time("9:00", "11:00") # 获取9:00到11:00之间的数据
df.at_time("3:33") # 获取3:33的数据
# 2）TimedeltaIndex
# 将timedelta64类型的数据设置为索引，得到的就是TimedeltaIndex。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv", parse_dates=[0])
df_date = pd.to_datetime(df["date"])
df["timedelta"] = df_date - df_date[0] # 得到timedelta64类型的数据
df.set_index("timedelta", inplace=True) # 将timedelta列设置为索引
df.info()
# <class 'pandas.core.frame.DataFrame'>
# TimedeltaIndex: 1461 entries, 0 days to 1460 days
# 将时间作为索引后可以直接使用时间进行切片取值。
print(df.loc["0 days":"5 days"])
#         date precipitation temp_max temp_min wind weather
# timedelta
# 0 days  2012-01-01      0.0   12.8    5.0  4.7 drizzle
# 1 days  2012-01-02      10.9   10.6    2.8  4.5   rain
# 2 days  2012-01-03      0.8   11.7    7.2  2.3   rain
# 3 days  2012-01-04      20.3   12.2    5.6  4.7   rain
# 4 days  2012-01-05      1.3    8.9    2.8  6.1   rain
# 5 days  2012-01-06      2.5    4.4    2.2  2.2   rain
# 3.11.4生成时间序列
# 为了能更简便地创建有规律的时间序列，pandas提供了date_range()方法。
# 1）date_range()
# date_range()通过开始日期、结束日期和频率代码（可选）创建一个有规律的日期序列，默认的频率是天。
print(pd.date_range("2015-07-03", "2015-07-10"))
# DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-05', '2015-07-06',
#        '2015-07-07', '2015-07-08', '2015-07-09', '2015-07-10'],
#        dtype='datetime64[ns]', freq='D')
# 此外，日期范围不一定非是开始时间与结束时间，也可以是开始时间与周期数periods。
print(pd.date_range("2015-07-03", periods=5))
# DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-05', '2015-07-06',
#        '2015-07-07'],
#        dtype='datetime64[ns]', freq='D')
# 可以通过freq参数设置时间频率，默认值是D。此处改为h，按小时变化的时间戳。
print(pd.date_range("2015-07-03", periods=5, freq="h"))
# DatetimeIndex(['2015-07-03 00:00:00', '2015-07-03 01:00:00',
#        '2015-07-03 02:00:00', '2015-07-03 03:00:00',
#        '2015-07-03 04:00:00'],
#        dtype='datetime64[ns]', freq='h')
# 2）时间频率与偏移量
# （1）可通过freq参数设置时间频率
# 下表为常见时间频率代码与说明：
# 代码	说明
# D	天（calendar day，按日历算，含双休日）
# B	天（business day，仅含工作日）
# W	周（weekly）
# ME / M	月末（month end）
# BME	月末（business month end，仅含工作日）
# MS	月初（month start）
# BMS	月初（business month start，仅含工作日）
# QE / Q	季末（quarter end）
# BQE	季末（business quarter end，仅含工作日）
# QS	季初（quarter start）
# BQS	季初（business quarter start，仅含工作日）
# YE / Y	年末（year end）
# BYE	年末（business year end，仅含工作日）
# YS	年初（year start）
# BYS	年初（business year start，仅含工作日）
# h	小时（hours）
# bh	小时（business hours，工作时间）
# min	分钟（minutes）
# s	秒（seconds）
# ms	毫秒（milliseonds）
# us	微秒（microseconds）
# ns	纳秒（nanoseconds）
# （2）偏移量
# 可以在频率代码后面加三位月份缩写字母来改变季、年频率的开始时间。
# QE-JAN、BQE-FEB、QS-MAR、BQS-APR等
# YE-JAN、BYE-FEB、YS-MAR、BYS-APR等
# print(pd.date_range("2015-07-03", periods=10, freq="QE-JAN")) # 设置1月为季度末
# DatetimeIndex(['2015-07-31', '2015-10-31', '2016-01-31', '2016-04-30',
#        '2016-07-31', '2016-10-31', '2017-01-31', '2017-04-30',
#        '2017-07-31', '2017-10-31'],
#        dtype='datetime64[ns]', freq='QE-JAN')
# 同理，也可以在后面加三位星期缩写字母来改变一周的开始时间。
# W-SUN、W-MON、W-TUE、W-WED等
# print(pd.date_range("2015-07-03", periods=10, freq="W-WED")) # 设置周三为一周的第一天
# DatetimeIndex(['2015-07-08', '2015-07-15', '2015-07-22', '2015-07-29',
#        '2015-08-05', '2015-08-12', '2015-08-19', '2015-08-26',
#        '2015-09-02', '2015-09-09'],
#        dtype='datetime64[ns]', freq='W-WED')
# 在这些代码的基础上，还可以将频率组合起来创建的新的周期。例如，可以用小时（h）和分钟（min）的组合来实现2小时30分钟。
print(pd.date_range("2015-07-03", periods=10, freq="2h30min"))
# DatetimeIndex(['2015-07-03 00:00:00', '2015-07-03 02:30:00',
#        '2015-07-03 05:00:00', '2015-07-03 07:30:00',
#        '2015-07-03 10:00:00', '2015-07-03 12:30:00',
#        '2015-07-03 15:00:00', '2015-07-03 17:30:00',
#        '2015-07-03 20:00:00', '2015-07-03 22:30:00'],
#        dtype='datetime64[ns]', freq='150min')
# 3.11.5重新采样
# 处理时间序列数据时，经常需要按照新的频率（更高频率、更低频率）对数据进行重新采样。可以通过resample()方法解决这个问题。resample()方法以数据累计为基础，会将数据按指定的时间周期进行分组，之后可以对其使用聚合函数。
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\weather.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
# print(df[["temp_max", "temp_min"]].resample("YE").mean()) # 将数据按年分组,并计算每年的平均最高最低温度
#       temp_max temp_min
# date
# 2012-12-31 15.276776 7.289617
# 2013-12-31 16.058904 8.153973
# 2014-12-31 16.995890 8.662466
# 2015-12-31 17.427945 8.835616