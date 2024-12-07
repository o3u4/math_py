import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matlab.engine

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

    @classmethod
    def implicit_ode2_Explicit(cls, equations):
        """
        隐式微分方程组转为显式
        :param equations:隐式方程组的等式
            def equations(dy, y):
                # dy 为需要求解的微分项, y为原始项
                eq1 = dy[0] - y[1]  # dy1/dt = y2
                eq2 = dy[1] - y[2]  # dy2/dt = y3
                ...
                return [eq1, eq2, ...]

        :return: 显式方程系统 (函数)
        """
        def Explicit_system(t, y):
            """
            隐方程组通过求解得到每个y下对应的微分组dy
            :param t:
            :param y:
            :return: 显式微分方程组, dy=f(y)
            """
            sys = fsolve(lambda dy: equations(dy, y), np.zeros_like(y))
            return sys
        return Explicit_system

    @classmethod
    def use_matlab(cls, file_path):
        """
        用matlab求解
        :param file_path: .m文件所在文件夹路径
        :return: 解, t
        """
        eng = matlab.engine.start_matlab()
        eng.cd(file_path)  # .m 文件所在路径
        t, y = eng.implicit_ode_solve(nargout=2)    # implicit_ode_solve为.m函数名
        t = np.array(t)
        y = np.array(y)
        eng.quit()
        return y, t

    def phase_diagram(self, x_span, y_span, z_span=None, num=20, ax=None):
        """
        2维3维向量场相图
        :param x_span:(min, max) 范围
        :param y_span:
        :param z_span:
        :param num:分点数
        :param ax: 画布
        :return:
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        else:
            fig = ax.figure
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
        return fig, ax

    def quiver(self, solution, t_span, vector_num=3, ax=None):
        """
        每个解曲线画运动方向箭头
        :param solution:不同初始点的解曲线
        :param t_span: t的范围 np.array()
        :param vector_num: 箭头的个数
        :param ax: 画布
        :return:
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        else:
            fig = ax.figure
        n = len(t_span)
        for i in range(vector_num):
            point = int(i * n / vector_num)
            u, v = self.sys(0, [solution[0][point], solution[1][point]])
            ax.quiver(solution[0][point], solution[1][point],
                      u, v, angles='xy', scale_units='xy', color='red')
        return fig, ax


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
    fig, ax = plt.subplots()
    s.phase_diagram((0, 4), (0, 4), ax=ax)
    for result in results:
        ax.plot(result[0], result[1], color='green')
        s.quiver(result, t, ax=ax)
    plt.show()
    # y, t = ODESystem.use_matlab(r'D:\matlab_file\隐式微分方程')
    # # 绘制结果
    # plt.plot(t, y[:, 0], label='y1')
    # plt.plot(t, y[:, 1], label='y2')
    # plt.plot(t, y[:, 2], label='y3')
    # plt.plot(t, y[:, 3], label='y4')
    # plt.xlabel('Time t')
    # plt.ylabel('Solutions y1, y2, y3, y4')
    # plt.title('Solution of Implicit ODE')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

