import numpy as np
from draw.draw import plot_line, scatter_plot
from draw import color
import matplotlib.pyplot as plt


class LSM:
    def __init__(self, x_real, y_real):
        self.x_real = x_real
        self.y_real = y_real

    def lsm(self, func, w=None):
        """
        最小二乘 y = a0 * f0(x) + a1 * f1(x) + ... + an * fn(x)
        :param func: 拟合函数列表
        :param w: 是否对每个点加权重
        :return:[a0, a1,..., an]
        """
        m = len(self.x_real)
        n = len(func)
        if type(self.x_real) is list:
            self.x_real = np.array(self.x_real)
        if type(self.y_real) is list:
            self.y_real = np.array(self.y_real)
        if w is None:
            w = np.identity(m)
        elif type(w) is list:
            w = np.diag(w)
        A = np.zeros([m, n])
        for i in range(n):
            A[:, i] = np.array([func[i](xi) for xi in self.x_real])
        A_bar = A.T @ w @ A
        y_bar = A.T @ w @ self.y_real
        x = np.linalg.solve(A_bar, y_bar)
        return x

    def plot_fit(self, func, w=None, ax=None, line_color='#509caf',
              line_label=None, linestyle='-'):
        x = self.lsm(func, w)
        x_min, x_max = np.min(self.x_real), np.max(self.x_real)
        x_plot = np.linspace(x_min, x_max, 100)
        fit_data = np.array([f(x_plot) for f in func])
        fit_data = x @ fit_data
        plot_line(x_plot, fit_data, line_color=line_color, ax=ax,
                  line_label=line_label, linestyle=linestyle)

    @staticmethod
    def polynomial(n):
        f_list = []
        for i in range(n + 1):
            f_list.append(lambda x, power=i: np.power(x, power))
        return f_list


if __name__ == '__main__':
    error = np.random.normal(loc=0, scale=1, size=200)
    x = np.linspace(1, 9, 200)
    y = 2 + x + 2 * x ** 2 + error
    lsm = LSM(x, y)
    poly2 = lsm.polynomial(2)
    # x_ = lsm.lsm(poly2)
    # print(x_)
    fig, ax = scatter_plot(x, y, point_color=color.red[0], point_label="真实值")
    lsm.plot_fit(poly2, line_color=color.blue1[0], line_label="拟合数据", ax=ax)
    plt.legend(fontsize='x-large')
    plt.show()

