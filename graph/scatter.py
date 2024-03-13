# 散点图

import matplotlib.pyplot as plt

lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 7, 11, 9, 8]

# 数据点形状
# 'o': 圆圈
# '^': 上三角形
# 's': 正方形
# 'd': 菱形
# 'x': X形
# '*': 星形
plt.scatter(lst1, lst2, color='green', marker='s', label="what")
plt.legend()
plt.show()
