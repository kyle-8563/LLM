from sklearn.preprocessing import MinMaxScaler

X = [[2, 1], [3, 1], [1, 4], [2, 6]]
# 归一化，区间设置为(-1,1)
X = MinMaxScaler(feature_range=(-1, 1)).fit_transform(X)
print(X)

from sklearn.preprocessing import StandardScaler

X = [[2, 1], [3, 1], [1, 4], [2, 6]]
# 标准化
X = StandardScaler().fit_transform(X)
print(X)