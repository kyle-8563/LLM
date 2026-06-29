from sklearn.feature_selection import VarianceThreshold
import numpy as np

# 生成100行10列随机数据
X = np.random.uniform(0, 1, (100, 10))
# 低方差过滤
# 计算每列方差
var = X.var(axis=0)

# 低方差过滤
var_thresh = VarianceThreshold(threshold=0.08)
X_filtered = var_thresh.fit_transform(X)

print("每列方差:", var)
print("原始特征数量:", X.shape[1])
print("过滤后特征数量:", X_filtered.shape[1])