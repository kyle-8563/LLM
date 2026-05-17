#进行np的基本函数
import numpy as np
arr = np.array([[1.2, 2, 3], [4, 5, 6], [7, 8, -9]])
print(np.abs(arr))#计算数组中每个元素的绝对值
print(np.sqrt(arr))#计算数组中每个元素的平方根
print(np.exp(arr))#计算数组中每个元素的指数
print(np.log(arr))#计算数组中每个元素的自然对数
print(np.sin(arr))#计算数组中每个元素的正弦值
print(np.cos(arr))#计算数组中每个元素的余弦值
print(np.tan(arr))#计算数组中每个元素的正切值
print(np.arcsin(arr))#计算数组中每个元素的反正弦值
print(np.arccos(arr))#计算数组中每个元素的反余弦值
print(np.arctan(arr))#计算数组中每个元素的反正切值

print(np.sum(arr))#计算数组中所有元素的和
print(np.mean(arr))#计算数组中所有元素的平均值
print(np.median(arr))#计算数组中所有元素的中位数
print(np.std(arr))#计算数组中所有元素的标准差
print(np.min(arr))#计算数组中所有元素的最小值
print(np.max(arr))#计算数组中所有元素的最大值

print(np.argmin(arr))#计算数组中所有元素的最小值的索引
print(np.argmax(arr))#计算数组中所有元素的最大值的索引

print(np.sort(arr))#对数组中的元素进行排序
print(np.argsort(arr))#返回数组中元素排序后的索引

print(np.unique(arr))#返回数组中唯一的元素
print(np.count_nonzero(arr))#计算数组中非零元素的数量
print(np.where(arr > 0))#返回数组中满足条件的元素的索引
print(np.isfinite(arr))#返回一个布尔数组，表示数组中每个元素是否是有限的（即不是inf或NaN）
print(np.isnan(arr))#返回一个布尔数组，表示数组中每个元素是否是NaN

print(np.cumsum(arr))#计算数组中元素的累积和
print(np.cumprod(arr))#计算数组中元素的累积积

print(np.diff(arr))#计算数组中元素的离散差分
print(np.gradient(arr))#计算数组中元素的梯度

print(np.dot(arr, arr.T))#计算数组与其转置的点积
print(np.cross(arr, arr))#计算数组与自身的叉积 

print(np.linalg.norm(arr))#计算数组的范数
print(np.linalg.inv(arr))#计算数组的逆矩阵 
print(np.linalg.det(arr))#计算数组的行列式
print(np.linalg.eig(arr))#计算数组的特征值和特征向量
print(np.linalg.svd(arr))#计算数组的奇异值分解
print(np.linalg.solve(arr, arr))#解线性方程组Ax = B，其中A为arr，B为arr

# print(np.linalg.cholesky(arr))#计算数组的Cholesky分解
print(np.linalg.qr(arr))#计算数组的QR分解

print(np.linalg.slogdet(arr))#计算数组的行列式的符号和对数值
print(np.linalg.matrix_rank(arr))#计算数组的秩
print(np.linalg.norm(arr, ord=1))#计算数组的L1范数
print(np.linalg.norm(arr, ord=2))#计算数组的L2范数
print(np.linalg.norm(arr, ord=np.inf))#计算数组的无穷范数

print(np.linalg.eigvals(arr))#计算数组的特征值
print(np.linalg.eigvalsh(arr))#计算数组的特征值（仅适用于对称或Hermitian矩阵)

print(np.linalg.svd(arr, full_matrices=False))#计算数组的奇异值分解，返回U、S、Vh矩阵
print(np.linalg.svd(arr, full_matrices=False)[0])#返回U矩阵
print(np.linalg.svd(arr, full_matrices=False)[1])#返回S矩阵
print(np.linalg.svd(arr, full_matrices=False)[2])#返回Vh矩阵

print(np.rint(arr))#对数组中每个元素进行四舍五入
print(np.floor(arr))#对数组中每个元素进行向下取整
print(np.ceil(arr))#对数组中每个元素进行向上取整
print(np.round(arr, decimals=1))#对数组中每个元素进行四舍五入，保留小数点后1位

print(np.clip(arr, 0, 5))#将数组中每个元素限制在0和5之间

print(np.interp(2.5, [0, 1, 2, 3], [0, 1, 4, 9]))#在给定的x和y数组中进行线性插值，计算x=2.5时的y值

print(np.polyfit([0, 1, 2, 3], [0, 1, 4, 9], 2))#对给定的x和y数组进行多项式拟合，返回多项式的系数

print(np.polyval([1, 0, 0, 0], 2))#计算多项式在给定点的值，输入为多项式的系数和点的值

print(np.random.seed(0))#设置随机数种子，使得每次生成的随机数相同
print(np.multiply(arr, arr))#计算数组中每个元素的乘积
print(np.divide(arr, arr))#计算数组中每个元素的商
print(np.add(arr, arr))#计算数组中每个元素的和
print(np.subtract(arr, arr))#计算数组中每个元素的差 
