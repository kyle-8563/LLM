import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
label = ["猫", "狗"] # 标签
y_true = ["猫", "猫", "猫", "猫", "猫", "猫", "狗", "狗", "狗", "狗"] # 真实值
y_pred1 = ["猫", "猫", "狗", "猫", "猫", "猫", "猫", "猫", "狗", "狗"] # 预测值
matrix1 = confusion_matrix(y_true, y_pred1, labels=label) # 混淆矩阵
print(pd.DataFrame(matrix1, columns=label, index=label))
sns.heatmap(matrix1, annot=True, fmt='d', cmap='Greens')
plt.show()


from sklearn.metrics import recall_score

label = ["猫", "狗"] # 标签
y_true = ["猫", "猫", "猫", "猫", "猫", "猫", "狗", "狗", "狗", "狗"] # 真实值
y_pred1 = ["猫", "猫", "狗", "猫", "猫", "猫", "猫", "猫", "狗", "狗"] # 预测值
recall = recall_score(y_true, y_pred1, pos_label="猫") # pos_label指定正例
print(recall)


from sklearn.metrics import f1_score

label = ["猫", "狗"] # 标签
y_true = ["猫", "猫", "猫", "猫", "猫", "猫", "狗", "狗", "狗", "狗"] # 真实值
y_pred1 = ["猫", "猫", "狗", "猫", "猫", "猫", "猫", "猫", "狗", "狗"] # 预测值
f1 = f1_score(y_true, y_pred1, pos_label="猫") # pos_label指定正例
print(f1)


# from sklearn.metrics import classification_report

# report = classification_report(y_true, y_pred1, labels=[], target_names=None)
# y_true：真实标签
# y_pred：预测的标签
# labels：可选，指定需要计算的类别列表（默认计算所有出现过的类别）
# target_names：可选，类别名称（默认使用 labels 指定的类别号）

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 生成一个二分类数据集
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=100)

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# 训练一个逻辑回归模型
model = LogisticRegression()
model.fit(x_train, y_train)

# 预测
y_pred = model.predict(x_test)

# 生成分类报告
report = classification_report(y_test, y_pred)
print(report)