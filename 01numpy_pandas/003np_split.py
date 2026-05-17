# 对ndarray进行索引和切片
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0])#访问第一行
print(a[0][0])#访问第一行第一列
print(a[0, 0])#访问第一行第一列
print(a[:, 0])#访问第一列
print(a[0, :])#访问第一行
print(a[0:2, 0:2])#访问前两行前两列
print(a[::2, ::2])#访问每隔一行每隔一列