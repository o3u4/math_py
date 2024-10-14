# Runge 高阶插值大误差现象
import numpy as np
from draw.draw import plot_line
import matplotlib.pyplot as plt
from draw import color
from fit import Interpolation


# 1/(1+x)^2 [-5, 5]
def func(x_):
    return 1 / (1 + x_ ** 2)


x = np.linspace(-5, 5, 100)
y = func(x)
fig, ax = plot_line(x, y, line_label="$\\frac{1}{(1+x)^2}$")

x_1 = np.linspace(-5, 5, 6)     # 5等分
x_2 = np.linspace(-5, 5, 11)     # 10等分
y_1 = func(x_1)
y_2 = func(x_2)

itp = Interpolation(x_1, y_1)
f1 = itp.Lagrange_fit()  # Lagrange插值函数
y1 = np.array([f1(i) for i in x])
plot_line(x, y1, line_color=color.red[0], ax=ax, line_label="$L_5$", linestyle="--")

itp2 = Interpolation(x_2, y_2)
f2 = itp2.Lagrange_fit()
y2 = np.array([f2(i) for i in x])
plot_line(x, y2, line_color=color.green[0], ax=ax, line_label="$L_{10}$", linestyle="--")

plt.legend(loc=(0.7, 0.7), fontsize="x-large")
plt.show()

