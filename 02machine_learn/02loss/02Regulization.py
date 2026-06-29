import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error

plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams["axes.unicode_minus"] = False

def polynomial(x, degree):
  """构成多项式，返回 [x^1,x^2,x^3,...,x^n]"""
  return np.hstack([x**i for i in range(1, degree + 1)])

# 生成随机数据
X = np.linspace(-3, 3, 300).reshape(-1, 1)
y = np.sin(X) + np.random.uniform(-0.5, 0.5, X.size).reshape(-1, 1)
fig, ax = plt.subplots(2, 3, figsize=(15, 8))
ax[0, 0].plot(X, y, "yo")
ax[0, 1].plot(X, y, "yo")
ax[0, 2].plot(X, y, "yo")

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
x_train1 = polynomial(x_train, 20)
x_test1 = polynomial(x_test, 20)

# 拟合
model = LinearRegression()
model.fit(x_train1, y_train) # 模型训练
y_pred3 = model.predict(x_test1) # 预测
ax[0, 0].plot(X, model.predict(polynomial(X, 20)), "r") # 绘制曲线
ax[0, 0].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred3):.4f}")
ax[1, 0].bar(np.arange(20), model.coef_.reshape(-1)) # 绘制所有系数

# L1正则化-Lasso回归
lasso = Lasso(alpha=0.01)
lasso.fit(x_train1, y_train) # 模型训练
y_pred3 = lasso.predict(x_test1) # 预测
ax[0, 1].plot(X, lasso.predict(polynomial(X, 20)), "r") # 绘制曲线
ax[0, 1].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred3):.4f}")
ax[0, 1].text(-3, 1.2, "Lasso回归")
ax[1, 1].bar(np.arange(20), lasso.coef_) # 绘制所有系数

# L2正则化-岭回归
ridge = Ridge(alpha=1)
ridge.fit(x_train1, y_train) # 模型训练
y_pred3 = ridge.predict(x_test1) # 预测
ax[0, 2].plot(X, ridge.predict(polynomial(X, 20)), "r") # 绘制曲线
ax[0, 2].text(-3, 1, f"测试集均方误差：{mean_squared_error(y_test, y_pred3):.4f}")
ax[0, 2].text(-3, 1.2, "岭回归")
ax[1, 2].bar(np.arange(20), ridge.coef_) # 绘制所有系数
plt.show()