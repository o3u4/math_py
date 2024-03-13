import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

np.random.seed(19680801)

plt.style.use('seaborn-v0_8')  # 风格

fig, ax = plt.subplots()
path = 'relate.xlsx'
sheet = '2000'
df = pd.read_excel(path, sheet_name=sheet)
data = np.array(df.iloc[0:12, 0])
# print(data)
#
# # 生成一列随机数据
# data = np.random.normal(0, 1, 1000)

# 正态分布检验
k2, p = stats.normaltest(data)
alpha = 0.05
if p < alpha:  # 如果p值小于0.05，则数据不满足正态分布
    print("数据不满足正态分布")
else:
    print("数据满足正态分布")
    mean = np.mean(data)
    std = np.std(data)
    print("均值：", mean)
    print("标准差：", std)

# 183.18, 0.08717797887081379
# 绘制原始数据的直方图
ax.hist(np.random.normal(183.18, 0.08717797887081379, size=50),
        histtype="stepfilled", bins=25, alpha=0.8, density=True, label='origin data')
# plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

ax.hist(np.random.normal(183.18, 0.08717797887081379, size=10000),
        histtype="stepfilled", bins=25, alpha=0.8, density=True,
        label='Normal distribution fitting curve')

plt.legend()
plt.xlabel('water level')
plt.ylabel('frequency')
plt.title('Normality test')
plt.show()
