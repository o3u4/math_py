import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.style.use('seaborn-v0_8')    # 风格


def plot_normal_hist(ax_, a, b):
    ax_.hist(np.random.normal(a, b, size=10000),    # a均值为曲线中心, b标准差为曲线的宽窄, size数量
             histtype="stepfilled", bins=25, alpha=0.8, density=True)


fig, ax = plt.subplots()
plot_normal_hist(ax, 10, 10)
plot_normal_hist(ax, 4, 12)
plot_normal_hist(ax, 50, 12)
plot_normal_hist(ax, 6, 55)
ax.legend(['(10, 10)', '(4, 12)', '(50, 12)', '(6, 55)'])  # 添加图例
ax.set_title("'bmh' style sheet")

plt.show()
