# 创建数组的方式
import numpy as np
from pyparsing import line
data = [1, 2, 3]
print(id(data))
a = np.array(data)
print(id(a))
# 不创建同一地址
print(id(np.asarray(a)))#将输入数据转换为数组

# zeros()#创建一个全为0的数组
a = np.zeros((2, 3))#创建一个2行3列的全为0的数组
print(a)
# ones()#创建一个全为1的数组
print(np.ones((2, 3)))#创建一个2行3列的全为1的数组
# empty()#创建一个未初始化的数组
print(np.empty((2, 3)))#创建一个2行3列的未初始化的数组
zerolikes = np.zeros_like(a)#创建一个与a形状相同的全为0的数组
print(zerolikes)
oneslikes = np.ones_like(a)#创建一个与a形状相同的全为1的数组
print(oneslikes)
empty_likes = np.empty_like(a)#创建一个与a形状相同的未初始化的数组
print(empty_likes)

# full()#创建一个全为指定值的数组
print(np.full((2, 3), 7))#创建一个2行3列的全为7的数组
full_likes = np.full_like(a, 7)#创建一个与a形状相同的全为7的数组
print(full_likes)

# arange(0, 10, 2)
print(np.arange(0, 10, 2))#创建一个从0到10（不包括10）步长为2的数组

print(np.linspace(0, 1, 5))#创建一个从0到1（包括1）等间隔的5个数的数组
print(np.linspace(0, 1, 5, endpoint=False))#创建一个从0到1（不包括1）等间隔的5个数的数组
print(np.linspace(0, 1, 5, retstep=True))#创建一个从0到1（包括1）等间隔的5个数的数组，并返回步长

import numpy as np

print(np.logspace(0, 1, 5))
# 创建一个从10^0到10^1（包括10^1）等比间隔的5个数的数组，默认底数为10

print(np.logspace(0, 1, 5, endpoint=False))
# 创建一个从10^0到10^1（不包括10^1）等比间隔的5个数的数组，默认底数为10

print(np.logspace(2, 10, 5, base=2))
# 创建一个从2^2到2^10（包括2^10）等比间隔的5个数的数组，底数为2

print(np.random.rand(2, 3))#创建一个2行3列的随机数数组，数值在[0, 1)之间
print(np.random.randn(2, 3))#创建一个2行3列的随机数数组，数值服从标准正态分布
print(np.random.randint(0, 10, (2, 3)))#创建一个2行3列的随机整数数组，数值在[0, 10)之间
print(np.random.uniform(0, 1, (2, 3)))#创建一个2行3列的随机数数组，数值在[0, 1)之间，服从均匀分布
print(np.random.seed(0))#设置随机数种子，使得每次生成的随机数相同

#matrix为ndarray的子类，专门用于处理矩阵运算
print(np.matrix([[1, 2], [3, 4]]))#创建一个矩阵对象
print(np.asmatrix([[1, 2], [3, 4]]))#将输入数据转换为矩阵对象

print(np.array([[1, 2], [3, 4]],dtype=np.float32))#创建一个二维数组对象
a  = np.array([[1, 2], [3, 4]], dtype=np.float32)
print(a.dtype)#查看数组的数据类型
a=a.astype(np.int32)#将数组的数据类型转换为int32
print(a.dtype)#查看数组的数据类型
