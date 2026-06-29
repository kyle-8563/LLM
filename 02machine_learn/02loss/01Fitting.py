import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams["axes.unicode_minus"] = False

def polynomial(x, degree):
  """构成多项式，返回 [x^1,x^2,x^3,...,x^n]"""
  return np.hstack([x**i for i in range(1, degree + 1)])

# 生成随机数据
X = np.linspace(-3, 3, 300).reshape(-1, 1)
y = np.sin(X) + np.random.uniform(-0.5, 0.5, 300).reshape(-1, 1)
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
ax[0].plot(X, y, "yo")
ax[1].plot(X, y, "yo")
ax[2].plot(X, y, "yo")

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 欠拟合
x_train1 = x_train
x_test1 = x_test
model.fit(x_train1, y_train) # 模型训练
y_pred1 = model.predict(x_test1) # 预测
ax[0].plot(np.array([[-3], [3]]), model.predict(np.array([[-3], [3]])), "c") # 绘制曲线
ax[0].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred1):.4f}")
ax[0].text(-3, 1.3, f"训练集均方误差：{mean_squared_error(y_train, model.predict(x_train1)):.4f}")

# 恰好拟合
x_train2 = polynomial(x_train, 5)
x_test2 = polynomial(x_test, 5)
model.fit(x_train2, y_train) # 模型训练
y_pred2 = model.predict(x_test2) # 预测
ax[1].plot(X, model.predict(polynomial(X, 5)), "k") # 绘制曲线
ax[1].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred2):.4f}")
ax[1].text(-3, 1.3, f"训练集均方误差：{mean_squared_error(y_train, model.predict(x_train2)):.4f}")

# 过拟合
x_train3 = polynomial(x_train, 20)
x_test3 = polynomial(x_test, 20)
model.fit(x_train3, y_train) # 模型训练
y_pred3 = model.predict(x_test3) # 预测
ax[2].plot(X, model.predict(polynomial(X, 20)), "r") # 绘制曲线
ax[2].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred3):.4f}")
ax[2].text(-3, 1.3, f"训练集均方误差：{mean_squared_error(y_train, model.predict(x_train3)):.4f}")
plt.show()