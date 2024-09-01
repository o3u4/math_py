import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 数据
data = {
    'AIC': [2267.6980, 2217.4450, 2216.7030, 2232.2590, 2216.0590, 2217.0980, 2227.8520, 2216.3660, 2220.2025],
    'p': [0, 0, 0, 1, 1, 1, 2, 2, 2],
    'q': [0, 1, 2, 0, 1, 2, 0, 1, 2]
}

df = pd.DataFrame(data)

# 创建一个pivot表格，以便生成热力图
pivot_table = df.pivot(index="p", columns="q", values="AIC")

# 自定义颜色映射，从浅蓝色到深蓝色
colors = ["#CBF2D1", "#60C26F", "#61C06F"]  # 定义渐变颜色
custom_cmap = LinearSegmentedColormap.from_list("custom_greens", colors)

# 绘制热力图，使用自定义配色方案
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, cmap=custom_cmap, fmt=".2f", annot_kws={"size": 14})
plt.title("AIC Heatmap for Different p and q Values")
plt.show()
