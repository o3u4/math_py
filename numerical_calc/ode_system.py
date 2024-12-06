import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False


class ODESystem:
    def __init__(self, sys):
        self.sys = sys

    def solve(self, t_span, init_list, num=500):
        """
        对多初始值进行求解
        :param t_span: 时间区间 (t_min, t_max)
        :param init_list:不同初始值
        :param num:分点数
        :return: [解的列表, 时间尺度]
        """
        t_eval = np.linspace(t_span[0], t_span[1], num)
        solutions = []
        for init in init_list:
            solution = solve_ivp(self.sys, t_span, init, t_eval=t_eval)
            solutions.append(solution.y)
        return solutions, t_eval

    def phase_diagram(self, x_span, y_span, z_span=None, num=20):
        """
        2维3维向量场相图
        :param x_span:(min, max) 范围
        :param y_span:
        :param z_span:
        :param num:分点数
        :return:
        """
        if z_span is None:
            x = np.linspace(x_span[0], x_span[1], num)
            y = np.linspace(y_span[0], y_span[1], num)
            X, Y = np.meshgrid(x, y)
            # 计算每个网格点的矢量方向
            U = np.zeros_like(X)
            V = np.zeros_like(Y)
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    dxdt, dydt = self.sys(0, [X[i, j], Y[i, j]])
                    U[i, j] = dxdt
                    V[i, j] = dydt
            plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', color='blue')
        else:
            x = np.linspace(x_span[0], x_span[1], num)
            y = np.linspace(y_span[0], y_span[1], num)
            z = np.linspace(z_span[0], z_span[1], num)
            X, Y, Z = np.meshgrid(x, y, z)
            # 计算每个网格点的矢量方向
            U = np.zeros_like(X)
            V = np.zeros_like(Y)
            W = np.zeros_like(Z)
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    dxdt, dydt, dzdt = self.sys(0, [X[i, j], Y[i, j], Z[i, j]])
                    U[i, j] = dxdt
                    V[i, j] = dydt
                    W[i, j] = dzdt
            plt.quiver(X, Y, Z, U, V, W, angles='xyz', scale_units='xyz', color='blue')


if __name__ == '__main__':
    def lotka_volterra(t, z):
        x, y = z
        dxdt = x * (3 - x - 2 * y)
        dydt = y * (2 - x - y)
        return [dxdt, dydt]
    init_lists = [[3, 1], [1e-4, 0], [0, 1e-4], [0.01, 0.03], [0.01, 0.0455]]
    s = ODESystem(lotka_volterra)
    results, t = s.solve((0, 15), init_lists)
    for result in results:
        plt.plot(t, result[0], color='blue')
        plt.plot(t, result[1], color='red')
plt.xlabel('时间 t')
plt.ylabel('种群数量')
plt.legend(["兔子 (x)", "羊 (y)"])
plt.title('洛特卡-沃尔特拉方程组的数值解')
plt.show()
