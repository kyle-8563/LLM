from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pandas as pd

# 加载数据集
heart_disease = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\heart_disease.csv")
# 处理缺失值
heart_disease = heart_disease.dropna()
# 划分特征和标签
X = heart_disease.drop("是否患有心脏病", axis=1) # 特征
y = heart_disease["是否患有心脏病"] # 标签
# 将数据集按7:3划分为训练数据与测试数据
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
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
# 使用K近邻分类模型，K=3
knn = KNeighborsClassifier(n_neighbors=3)
# 模型训练
knn.fit(x_train, y_train)
# 模型评估，计算准确率
print("模型准确率：", knn.score(x_test, y_test))


import joblib

joblib.dump(knn, "knn_heart_disease")
# 加载先前保存的模型：
# 加载模型
knn_loaded = joblib.load("knn_heart_disease")
# 预测
y_pred = knn_loaded.predict(x_test[10:11])
# 打印真实值与预测值
print(y_test.iloc[10], y_pred)