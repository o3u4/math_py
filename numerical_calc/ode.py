import numpy as np
from draw.draw import plot_line
from draw.color import *
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


class OdeSolver:
    def __init__(self, func):
        """
        y'(x) = f(x, y)
        :param func: f
        """
        self.func = func

    def euler(self, a, y0, b, n):
        """
        y(a) = y0 初值条件
        :param a: x0
        :param y0: y0
        :param b: [a, b] 区间
        :param n: 区间等分个数
        :return:
        """
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n
        y = np.zeros_like(x)
        y[0] = y0
        for i in range(n):
            y[i + 1] = y[i] + h * self.func(x[i], y[i])
        return [x, y]

    def euler_adv(self, a, y0, b, n):
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n
        y = np.zeros_like(x)
        y[0] = y0
        for i in range(n):
            y_ = y[i] + h * self.func(x[i], y[i])
            y[i + 1] = (y[i] + h / 2 *
                        (self.func(x[i], y[i]) +
                         self.func(x[i + 1], y_)))
        return [x, y]


if __name__ == '__main__':
    def f(x, y):
        return y / x + x * np.exp(x)


    def yx(x):
        return x * (np.exp(x) - np.exp(1))


    eq = OdeSolver(f)
    [x1, y1] = eq.euler(1, 0, 2, 100)
    [x2, y2] = eq.euler_adv(1, 0, 2, 100)
    x3 = np.linspace(1, 2, 101)
    fig, ax = plot_line(x3, yx(x3), line_color=red[1],
                        line_label="解析解")
    plot_line(x1, y1, ax=ax, linestyle="--", line_color=blue1[1],
              line_label="Euler法")
    plot_line(x2, y2, ax=ax, linestyle="--", line_color=green[1],
              line_label="改进Euler法")

    axins = ax.inset_axes((0.7, 0.15, 0.2, 0.25))
    axins.plot(x3, yx(x3), color=red[1])
    axins.plot(x1, y1, color=blue1[1], linestyle="--")
    axins.plot(x2, y2, color=green[1], linestyle="--")
    axins.set_xlim(1.50, 1.52)
    axins.set_ylim(2.55, 2.9)
    mark_inset(ax, axins, loc1=3, loc2=2,
               fc="none", ec="grey", lw=1.5, linestyle="--")
    ax2 = ax.inset_axes((0.5, 0.7, 0.2, 0.2))
    ax2.plot(x3, yx(x3), color=red[1])
    ax2.plot(x1, y1, color=blue1[1], linestyle="--")
    ax2.plot(x2, y2, color=green[1], linestyle="--")
    ax2.set_xlim(1.94+7e-4, 1.94+7.5e-4)
    ax2.set_ylim(8.238, 8.241)
    mark_inset(ax, ax2, loc1=4, loc2=1,
               fc="none", ec="grey", lw=1.5, linestyle="--")

    plt.legend(fontsize=15)
    plt.show()
