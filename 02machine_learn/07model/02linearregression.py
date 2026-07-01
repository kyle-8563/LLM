from sklearn.linear_model import LinearRegression

# 自变量，每周学习时长
X = [[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]
# 因变量，数学考试成绩
y = [55, 65, 70, 75, 85, 50, 60, 72, 80, 58]
# 实例化线性回归模型
model = LinearRegression()
# 模型训练
model.fit(X, y)
# 系数，每周每学习1小时，成绩会增加多少分
print(model.coef_)
# 截距
print(model.intercept_)
# 预测,每周学习11小时，成绩可能是多少分
print(model.predict([[11]]))

#正规方程法
import sklearn
model = sklearn.linear_model.LinearRegression(fit_intercept=True)
model.fit([[0, 3], [1, 2], [2, 1]], [0, 1, 2])
# coef_: 系数
print(model.coef_)
# intercept_: 偏置
print(model.intercept_)


#梯度下降法
import numpy as np

def J(beta):
  """目标函数"""
  return np.sum((X @ beta - y) ** 2, axis=0).reshape(-1, 1) / n

def gradient(beta):
  """梯度"""
  return X.T @ (X @ beta - y) / n * 2

X = np.array([[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]) # 自变量，每周学习时长
y = np.array([[55], [65], [70], [75], [85], [50], [60], [72], [80], [58]]) # 因变量，数学考试成绩
beta = np.array([[1], [1]]) # 初始化参数
n = X.shape[0] # 样本数
X = np.hstack([np.ones((n, 1)), X]) # X添加一列1，与偏置项相乘
alpha = 1e-2 # 学习率
epoch = 0 # 迭代次数
while (j := J(beta)) > 1e-10 and (epoch := epoch + 1) <= 10000:
  grad = gradient(beta) # 求解梯度
  if epoch % 1000 == 0:
    print(f"beta={beta.reshape(-1)}\tJ={j.reshape(-1)}")
  beta = beta - alpha * grad # 更新参数

# 梯度下降法求解线性回归模型
model = sklearn.linear_model.SGDRegressor(
  loss="squared_error", # 损失函数，默认为均方误差
  fit_intercept=True, # 是否计算偏置
  learning_rate="constant", # 学习率策略
  eta0=0.1, # 初始学习率
  max_iter=1000, # 最大迭代次数
  tol=1e-8, # 损失值小于tol时停止迭代
)
model.fit([[0, 3], [1, 2], [2, 1]], [0, 1, 2])
# coef_: 系数
print(model.coef_)
# intercept_: 偏置
print(model.intercept_)



#案例
import pandas as pd
from sklearn.preprocessing import StandardScaler # 标准化
from sklearn.model_selection import train_test_split # 划分数据集
from sklearn.linear_model import LinearRegression, SGDRegressor # 线性回归-正规方程，线性回归-随机梯度下降
from sklearn.metrics import mean_squared_error # 均方误差

# 加载数据集
advertising = pd.read_csv(r"D:\learn\LLM\02machine_learn\data\advertising.csv")
advertising.drop(advertising.columns[0], axis=1, inplace=True)
advertising.dropna(inplace=True)
advertising.info()
print(advertising.head())

# 划分训练集与测试集
X = advertising.drop("Sales", axis=1)
y = advertising["Sales"]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 标准化
preprocessor = StandardScaler()
x_train = preprocessor.fit_transform(x_train) # 计算训练集的均值和标准差，并标准化训练集
x_test = preprocessor.transform(x_test) # 使用训练集的均值和标准差对测试集标准化

# 使用正规方程法拟合线性回归模型
normal_equation = LinearRegression()
normal_equation.fit(x_train, y_train)
print("正规方程法解得模型系数:", normal_equation.coef_)
print("正规方程法解得模型偏置:", normal_equation.intercept_)

# 使用随机梯度下降法拟合线性回归模型
gradient_descent = SGDRegressor()
gradient_descent.fit(x_train, y_train)
print("随机梯度下降法解得模型系数:", gradient_descent.coef_)
print("随机梯度下降法解得模型系数:", gradient_descent.intercept_)

# 使用均方误差评估模型
print("正规方程法均方误差:", mean_squared_error(y_test, normal_equation.predict(x_test)))
print("随机梯度下降法均方误差:", mean_squared_error(y_test, gradient_descent.predict(x_test)))