import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y']
y_ticks = [3, 2, 1, 0]   # 在指定坐标显示2d图   年份
for c, k in zip(colors, y_ticks):
    # 生成数据
    xs = np.arange(20)          # x的取值范围
    ys = np.random.rand(20)     # 改成真实数据, 为高度
    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(y_ticks)

plt.show()
