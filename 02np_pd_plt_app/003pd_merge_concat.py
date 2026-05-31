import pandas as pd
s1 = pd.Series(["A", "B"], index=[1, 2])
s2 = pd.Series(["D", "E"], index=[4, 5])
s3 = pd.Series(["G", "H"], index=[7, 8])

print(pd.concat([s1,s2,s3]))
#按照行的方向连接
print(pd.concat([s1,s2,s3],axis=0))
#按照列的方向连接
print(pd.concat([s1,s2,s3],axis=1))


df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
s1 = pd.Series(data=[7, 10], index=[1, 2], name="a")

print(pd.concat([df1, s1])) # 按行连接
#   a  b
# 1  1 4.0
# 2  2 5.0
# 1  7 NaN
# 2 10 NaN

print(pd.concat([df1, s1], axis=1)) # 按列连接
#  a b  a
# 1 1 4  7
# 2 2 5 10

df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])

print(pd.concat([df1, df2])) # 按行连接
#  a  b
# 1 1  4
# 2 2  5
# 1 7 10
# 2 8 11

print(pd.concat([df1, df2], axis=1)) # 按列连接


df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])

print(pd.concat([df1, df2], ignore_index=True)) # 重置索引


# 5）类似join的连接
# 默认的合并方式是对其他轴进行并集合并（join=outer），可以用join=inner实现其他轴上的交集合并。
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"b": [7, 8], "c": [10, 11]}, index=[2, 3])

print(pd.concat([df1, df2]))
#   a b   c
# 1 1.0 4  NaN
# 2 2.0 5  NaN
# 2 NaN 7 10.0
# 3 NaN 8 11.0

print(pd.concat([df1, df2], join="inner"))
#  b
# 1 4
# 2 5
# 2 7
# 3 8



df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
print(df1)
#  employee    group
# 0   Bob  Accounting
# 1   Jake Engineering
# 2   Lisa Engineering
# 3   Sue      HR
print(df2)
#  employee hire_date
# 0   Lisa    2004
# 1   Bob    2008
# 2   Jake    2012
# 3   Sue    2014
# 通过相同的字段名employee进行关联的
df3 = pd.merge(df1, df2,how="inner",on="employee")

print(df3)


# （2）多对一连接
# 在需要连接的两个列中，有一列的值有重复。通过多对一连接获得的结果将会保留重复值。
df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"group": ["Accounting", "Engineering", "HR"], "supervisor": ["Carly", "Guido", "Steve"]})
print(df1)
#  employee    group
# 0   Bob  Accounting
# 1   Jake Engineering
# 2   Lisa Engineering
# 3   Sue      HR
print(df2)
#     group supervisor
# 0  Accounting   Carly
# 1 Engineering   Guido
# 2      HR   Steve
df3 = pd.merge(df1, df2)
print(df3)
#  employee    group supervisor
# 0   Bob  Accounting   Carly
# 1   Jake Engineering   Guido
# 2   Lisa Engineering   Guido
# 3   Sue      HR   Steve
# 在supervisor列中有些值会因为输入数据的对应关系而有所重复。
# （3）多对多连接
# 如果左右两个输入的共同列都包含重复值，那么合并的结果就是一种多对多连接。
df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame(
  {
    "group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR"],
    "skills": ["math", "spreadsheets", "coding", "linux", "spreadsheets", "organization"],
  }
)
print(df1)
#  employee    group
# 0   Bob  Accounting
# 1   Jake Engineering
# 2   Lisa Engineering
# 3   Sue      HR
print(df2)
#     group    skills
# 0  Accounting     math
# 1  Accounting spreadsheets
# 2 Engineering    coding
# 3 Engineering     linux
# 4      HR spreadsheets
# 5      HR organization
df3 = pd.merge(df1, df2)
print(df3)
#  employee    group    skills
# 0   Bob  Accounting     math
# 1   Bob  Accounting spreadsheets
# 2   Jake Engineering    coding
# 3   Jake Engineering     linux
# 4   Lisa Engineering    coding
# 5   Lisa Engineering     linux
# 6   Sue      HR spreadsheets
# 7   Sue      HR organization


df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
print(df1)
#  employee    group
# 0   Bob  Accounting
# 1   Jake Engineering
# 2   Lisa Engineering
# 3   Sue      HR
print(df2)
#  employee hire_date
# 0   Lisa    2004
# 1   Bob    2008
# 2   Jake    2012
# 3   Sue    2014
df3 = pd.merge(df1, df2, on="employee")
print(df3)
#  employee    group hire_date
# 0   Bob  Accounting    2008
# 1   Jake Engineering    2012
# 2   Lisa Engineering    2004
# 3   Sue      HR    2014
# （2）两对象列名不同，通过left_on和right_on分别指定列名
df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "salary": [70000, 80000, 120000, 90000]})
print(df1)
#  employee    group
# 0   Bob  Accounting
# 1   Jake Engineering
# 2   Lisa Engineering
# 3   Sue      HR
print(df2)
#  name salary
# 0  Bob  70000
# 1 Jake  80000
# 2 Lisa 120000
# 3  Sue  90000
df3 = pd.merge(df1, df2, left_on="employee", right_on="name")
print(df3)
#  employee    group name salary
# 0   Bob  Accounting  Bob  70000
# 1   Jake Engineering Jake  80000
# 2   Lisa Engineering Lisa 120000
# 3   Sue      HR  Sue  90000
# （3）通过left_index和right_index设置合并的索引
# 通过设置merge()中的left_index、right_index参数将索引设置为键来实现合并。
df1 = pd.DataFrame(
  {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
df1.set_index("employee", inplace=True)
df2.set_index("employee", inplace=True)
print(df1)
#         group
# employee
# Bob    Accounting
# Jake   Engineering
# Lisa   Engineering
# Sue        HR
print(df2)
#      hire_date
# employee
# Lisa      2004
# Bob      2008
# Jake      2012
# Sue      2014
# 设置索引后，如果不指定关联列会报错，建议通过以下方式指定，on="employee"也可#以实现，但是不同的解释器可能效果不一样，因为设置索引后，employee就不算是列了
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
#         group hire_date
# employee
# Bob    Accounting    2008
# Jake   Engineering    2012
# Lisa   Engineering    2004
# Sue        HR    2014
# DataFrame实现了join()方法，可以按照索引进行数据合并。但要求没有重叠的列，或通过lsuffix、rsuffix指定重叠列的后缀。
import pandas as pd

df1 = pd.DataFrame({
  'key': ['A', 'B', 'C'],
  'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
  'key': ['B', 'C', 'D'],
  'value2': [4, 5, 6]
})

# 合并两个 DataFrame，并处理列名冲突，如果通过on指定列，只是指定的df1。会用
# df1指定的列和df2的索引连接，会报错。除非df2.set_index指定索引。
df1.join(df2,lsuffix='_left',rsuffix='_right')
# 3）设置数据连接的集合操作规则
# 当一个值出现在一列，却没有出现在另一列时，就需要考虑集合操作规则了。
df1 = pd.DataFrame({"name": ["Peter", "Paul", "Mary"], "food": ["fish", "beans", "bread"]}, columns=["name", "food"])
df2 = pd.DataFrame({"name": ["Mary", "Joseph"], "drink": ["wine", "beer"]}, columns=["name", "drink"])
print(df1)
#   name  food
# 0 Peter  fish
# 1  Paul beans
# 2  Mary bread
print(df2)
#   name drink
# 0  Mary wine
# 1 Joseph beer
print(pd.merge(df1, df2))
#  name  food drink
# 0 Mary bread wine
# 合并两个数据集，在name列中只有一个共同的值Mary。默认情况下，结果中只会包含两个输入集合的交集，这种连接方式被称为内连接（inner join）。
# 我们可以通过how参数设置连接方式，默认值为inner。how参数支持的数据连接方式还有outer、left和right。外连接（outer join）返回两个输入列的并集，所有缺失值都用 NaN 填充。
print(pd.merge(df1, df2, how="outer"))
#   name  food drink
# 0 Joseph  NaN beer
# 1  Mary bread wine
# 2  Paul beans  NaN
# 3  Peter  fish  NaN
# 左连接（left join）和右连接（right join）返回的结果分别只包含左列和右列。
print(pd.merge(df1, df2, how="left"))
#   name  food drink
# 0 Peter  fish  NaN
# 1  Paul beans  NaN
# 2  Mary bread wine
# 4）重复列名的处理
# 可能会遇到两个输入DataFrame有重名列的情况，merge()会自动为其增加后缀_x和_y，也可以通过suffixes参数自定义后缀名。
df1 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [1, 2, 3, 4]})
df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [3, 1, 4, 2]})
print(df1)
#  name rank
# 0  Bob   1
# 1 Jake   2
# 2 Lisa   3
# 3  Sue   4
print(df2)
#  name rank
# 0  Bob   3
# 1 Jake   1
# 2 Lisa   4
# 3  Sue   2
print(pd.merge(df1, df2, on="name")) # 不指定后缀名，默认为_x和_y
#  name rank_x rank_y
# 0  Bob    1    3
# 1 Jake    2    1
# 2 Lisa    3    4
# 3  Sue    4    2
print(pd.merge(df1, df2, on="name", suffixes=("_df1", "_df2"))) # 通过suffixes指定后缀名
#  name rank_df1 rank_df2
# 0  Bob     1     3
# 1 Jake     2     1
# 2 Lisa     3     4
# 3  Sue     4     2