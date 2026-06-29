import pandas as pd
import os
import pymysql

os.makedirs("data",exist_ok=True)
df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]})


df.set_index("id",inplace = True)
#保存为csv
df.to_csv("data/test.csv")
#保存为json
df.to_json("data/test.json")

#将df数据保存到剪切板
df.to_clipboard()

#换房df数据导出到Mysql
conn = pymysql.connect(
    host="127.0.0.1",
    port=3336,
    user="root",
    passwd="123456",
    db="atguigu",
    charset="utf-8",
)
df.to_sql("t_test",conn)
