import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Fixing random state for reproducibility
plt.style.use('seaborn-v0_8')  # 风格

file = 'Problem_D_Great_Lakes.xlsx'
sheet = "St. Mary's River"

df = pd.read_excel(file, sheet_name=sheet)

data = []  # 月份数据
mean = []
for i in range(15, 28):
    month = df.iloc[i, 1: 13]
    row_mean = month.mean()
    mean.append(row_mean)
    new_df = month - row_mean
    data.append(np.array(new_df))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y', '#845EC2', '#FF6F91', '#2C73D2', '#845EC2', '#B0A8B9', '#FEFEDF', '#936C00', '#4FFBDF']
years = [j for j in range(2009, 2022, 2)]  # 年份

for c, year, ys in zip(colors, years, data):
    xs = np.arange(12)  # 月份作为x轴
    cs = [c] * len(xs)  # 柱状图颜色

    # 绘制柱状图
    ax.bar(xs, ys, zs=year, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('Month')
ax.set_ylabel('Year')
ax.set_zlabel('Flow Rate(Distance from mean)')

ax.legend([str(mean[j]) for j in range(0, 13, 2)])
ax.set_title(f"{sheet}'s Flow")

# 设置y轴刻度为年份
ax.set_yticks(years)

plt.show()
