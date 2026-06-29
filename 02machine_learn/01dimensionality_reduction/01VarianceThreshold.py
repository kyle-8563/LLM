from sklearn.feature_selection import VarianceThreshold
import pandas as pd
advertising = pd.read_csv(r"D:\\learn\\LLM\\02machine_learn\\data\\advertising.csv")
advertising.drop(advertising.columns[0], axis=1, inplace=True)
advertising.dropna(inplace=True)
X = advertising.drop("Sales", axis=1)
# 低方差过滤：删除方差低于 0.01 的特征
var_thresh = VarianceThreshold(threshold=223)
X_filtered = var_thresh.fit_transform(X)
print("原始方差:", X.var())
print("原始特征数量:", X.shape[1])
print("过滤后特征数量:", X_filtered.shape[1])
print("过滤后特征:", X.columns[var_thresh.get_support()])