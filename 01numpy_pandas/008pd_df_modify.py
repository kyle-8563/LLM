#对pd进行修改
import pandas as pd
df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]})
print(df)

print(df[df.age>25])#选择年龄大于25的
print(df*2)
df1 = df

df.age = df.age*2
print(df)

print(df+df1)#进行相加

#指定行索引
# 创建
df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]},index = [1,2,3,4])
print(df)

# 指定行做索引
df.set_index("id",inplace=True)
print(df)

df.reset_index#进行索引重置
print(df)

df.columns = ["年龄","名称"]
print(df)
#删除列
df.drop(columns=["年龄"],inplace = True)
print(df)
#插入列
df.insert(0,"age",df["名称"])
print(df)
#删除列
del df["age"]
print(df)


