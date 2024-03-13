import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(4, 3))  # 只创建一个子图，将画布宽度减半

# fig.add_subplot(121, projection='3d')
# 121:将画布分成1行2列的子图，并选择第1个子图
ax = fig.add_subplot(111, projection='3d')  # 只创建一个子图


# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

z = x + y
bottom = np.zeros_like(z)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, z, shade=True)
ax.set_title('Shaded')

plt.show()
