def J(x):
  """目标函数"""
  return (x**2 - 2) ** 2

def gradient(x):
  """梯度"""
  return 4 * x**3 - 8 * x

x = 1 # x的初始值
alpha = 0.1 # 学习率
while (j := J(x)) > 1e-30: # 当目标函数的值小于10的-30次幂时停止计算
  print(f"x={x}\tJ={j}")
  grad = gradient(x) # 求解梯度
  x = x - alpha * grad # 更新参数