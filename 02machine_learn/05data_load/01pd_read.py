import pandas as pd

# 加载数据集
heart_disease = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\heart_disease.csv")
# 处理缺失值
heart_disease.dropna()
heart_disease.info()
heart_disease.head()