from sklearn.model_selection import train_test_split
import pandas as pd

# 加载数据集
heart_disease = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\heart_disease.csv")
# 处理缺失值
# 划分特征和标签
X = heart_disease.drop("是否患有心脏病", axis=1) # 特征
y = heart_disease["是否患有心脏病"] # 标签
# 将数据集按7:3划分为训练数据与测试数据
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
print("训练数据集特征维度：", x_train.shape)
print("训练数据集标签维度：", y_train.shape)
print("测试数据集特征维度：", x_test.shape)
print("测试数据集标签维度：", y_test.shape)