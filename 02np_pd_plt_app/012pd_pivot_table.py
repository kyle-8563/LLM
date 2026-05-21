# 1）统计不同睡眠时间，不同压力等级下的睡眠质量
import pandas as pd
df = pd.read_csv(r"D:\Code\learn\LLM\02np_pd_plt_app\data\sleep.csv")
sleep_duration_stage = pd.cut(df["sleep_duration"], [0, 5, 6, 7, 8, 9, 10, 11, 12]) # 对睡眠时间进行划分
stress_level_stage = pd.cut(df["stress_level"], 4) # 对压力等级进行划分
print(df.pivot_table(values="sleep_quality", index=[sleep_duration_stage, stress_level_stage], aggfunc="mean"))
#                sleep_quality
# sleep_duration stress_level
# (0, 5]     (0.991, 3.25]    6.781818
#        (3.25, 5.5]     6.161538
#        (5.5, 7.75]     5.677778
#        (7.75, 10.0]    6.082353


# 2）添加职业作为列维度
print(
  df.pivot_table(
    values="sleep_quality", index=[sleep_duration_stage, stress_level_stage], columns=["occupation"], aggfunc="mean"
  )
)
# occupation          Manual Labor Office Worker  Retired  Student
# sleep_duration stress_level
# (0, 5]     (0.991, 3.25]   6.900000    6.350000 6.720000 6.750000
#        (3.25, 5.5]    3.300000    7.966667 6.060000 5.650000
#        (5.5, 7.75]    4.833333    6.900000 3.200000 6.533333
#        (7.75, 10.0]    7.200000    5.977778 5.225000 7.150000
# (5, 6]     (0.991, 3.25]   5.220000    6.433333 5.700000 6.533333
#        (3.25, 5.5]    5.000000    7.050000 6.900000 9.000000
#        (5.5, 7.75]    6.050000    5.300000 5.300000 7.200000
#        (7.75, 10.0]    6.475000    4.050000    NaN 7.100000
# 3）添加性别作为第二个列维度
print(
  df.pivot_table(
    values="sleep_quality",
    index=[sleep_duration_stage, stress_level_stage],
    columns=["occupation", "gender"],
    aggfunc="mean",
  )
)
# occupation          Manual Labor      Office Worker     Retired       Student
# gender               Female   Male    Female  Male  Female    Male  Female   Male
# sleep_duration stress_level
# (0, 5]     (0.991, 3.25]     6.75 7.300000   6.700000 6.000    NaN  6.720000 6.100000 7.400000
#        (3.25, 5.5]      3.30    NaN   7.100000 9.700 4.850000  6.866667 5.300000 6.700000
#        (5.5, 7.75]      4.55 5.400000   5.900000 7.900    NaN  3.200000 6.850000 5.900000
#        (7.75, 10.0]     8.40 6.000000   5.180000 6.975 6.600000  4.766667 7.150000    NaN
# (5, 6]     (0.991, 3.25]     5.50 4.800000   8.200000 5.550 5.700000    NaN 8.150000 3.300000
#        (3.25, 5.5]      5.00    NaN   6.600000 7.500 6.700000  7.100000 9.000000    NaN
#        (5.5, 7.75]      6.60 5.500000   4.900000 6.100 4.450000  7.000000 7.066667 7.600000
#        (7.75, 10.0]     6.15 6.800000      NaN 4.050    NaN    NaN 7.266667 6.975000