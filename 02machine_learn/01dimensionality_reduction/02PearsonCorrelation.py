import pandas as pd
advertising = pd.read_csv(r"D:\\learn\\LLM\\02machine_learn\\data\\advertising.csv")

advertising.drop(advertising.columns[0], axis=1, inplace=True)
advertising.dropna(inplace=True)
X = advertising.drop("Sales", axis=1)
y = advertising["Sales"]
# 计算皮尔逊相关系数

print(X.corrwith(y, method="pearson"))
# TV           0.782224
# Radio        0.576223
# Newspaper    0.228299
# dtype: float64
# 使用pandas.DataFrame.corr(method="pearson")计算皮尔逊相关系数矩阵。
import seaborn as sns
import matplotlib.pyplot as plt

# 计算皮尔逊相关系数矩阵
corr_matrix = advertising.corr(method="pearson")
# 可视化热力图
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()