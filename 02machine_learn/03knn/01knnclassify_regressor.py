#分类
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=2) # KNN分类模型，K值为2
X = [[2, 1], [3, 1], [1, 4], [2, 6]] # 特征
y = [0, 0, 1, 1] # 标签
knn.fit(X, y) # 模型训练
print(knn.predict([[4, 9]])) # 预测

#回归
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=2) # KNN回归模型，K值为2
X = [[2, 1], [3, 1], [1, 4], [2, 6]] # 特征
y = [0.5, 0.33, 4, 3] # 标签
knn.fit(X, y) # 模型训练
print(knn.predict([[4, 9]])) # 预测