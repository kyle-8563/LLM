# solver: 优化算法
#  lbfgs: 拟牛顿法（默认），仅支持L2正则化
#  newton-cg: 牛顿法，仅支持L2正则化
#  liblinear: 坐标下降法，适用于小数据集，支持L1和L2正则化
#  sag: 随机平均梯度下降，适用于大规模数据集，仅支持L2正则化
#  saga: 改进的随机梯度下降，适用于大规模数据，支持L1、L2和ElasticNet正则化
# penalty: 正则化类型，可选l1、l2和elasticnet
# C: 正则化强度，C越小，正则化强度越大
# class_weight: 类别权重，balanced表示自动平衡类别权重，让模型在训练时更关注少数类，从而减少类别不平衡带来的偏差
import sklearn


model = sklearn.linear_model.LogisticRegression(solver="lbfgs", penalty="l2", C=1, class_weight="balanced")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

# 加载数据集
heart_disease = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\heart_disease.csv")
heart_disease.dropna(inplace=True)

# 划分为训练集与测试集
X = heart_disease.drop("是否患有心脏病", axis=1) # 特征
y = heart_disease["是否患有心脏病"] # 标签
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# 特征工程
# 数值型特征
numerical_features = ["年龄", "静息血压", "胆固醇", "最大心率", "运动后的ST下降", "主血管数量"]
# 类别型特征
categorical_features = ["胸痛类型", "静息心电图结果", "峰值ST段的斜率", "地中海贫血"]
# 二元特征
binary_features = ["性别", "空腹血糖", "运动性心绞痛"]
# 创建列转换器
preprocessor = ColumnTransformer(
  transformers=[
    # 对数值型特征进行标准化
    ("num", StandardScaler(), numerical_features),
    # 对类别型特征进行独热编码，使用drop="first"避免多重共线性
    ("cat", OneHotEncoder(drop="first"), categorical_features),
    # 二元特征不进行处理
    ("binary", "passthrough", binary_features),
  ]
)
# 执行特征转换
x_train = preprocessor.fit_transform(x_train) # 计算训练集的统计信息并进行转换
x_test = preprocessor.transform(x_test) # 使用训练集计算的信息对测试集进行转换

# 模型训练
model = LogisticRegression()
model.fit(x_train, y_train)

# 模型评估，计算准确率
print(model.score(x_test, y_test))


# from sklearn.linear_model import LogisticRegression

# model = LogisticRegression(multi_class="ovr")

# # 或

# from sklearn.multiclass import OneVsRestClassifier

# model = OneVsRestClassifier(LogisticRegression())


# from sklearn.linear_model import LogisticRegression

# model = LogisticRegression(multi_class="multinomial")

# # 对于多分类问题，LogisticRegression会自动使用multinomial，因此multi_class参数可省略

# model = LogisticRegression()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

# 加载数据集
digit = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\train.csv")
# plt.imshow(digit.iloc[10, 1:].values.reshape(28, 28), cmap="gray")
# plt.show()
# 划分训练集和测试集
X = digit.drop("label", axis=1) # 特征
y = digit["label"] # 标签
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# 归一化
preprocessor = MinMaxScaler()
x_train = preprocessor.fit_transform(x_train)
x_test = preprocessor.transform(x_test)

# 模型训练
model = LogisticRegression(max_iter=500)
model.fit(x_train, y_train)

# 模型评估
model.score(x_test, y_test)

# 预测
plt.imshow(digit.iloc[123, 1:].values.reshape(28, 28), cmap="gray")
plt.show()
print(model.predict(digit.iloc[123, 1:].values.reshape(1, -1)))