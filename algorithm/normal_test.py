# 正态分布检验

import numpy as np
from scipy import stats

np.random.seed(19680801)
# 生成一列随机数据
data = np.random.normal(0, 1, 1000)

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
