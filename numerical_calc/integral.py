import numpy as np


class Integral:
    C_1 = [1 / 2, 1 / 2]
    C_2 = [1 / 6, 4 / 6, 1 / 6]
    C_3 = [1 / 8, 3 / 8, 3 / 8, 1 / 8]
    C_4 = [7 / 90, 32 / 90, 12 / 90, 32 / 90, 7 / 90]
    C_5 = [19 / 288, 75 / 288, 50 / 288, 50 / 288, 75 / 288, 19 / 288]
    C_6 = [41 / 840, 216 / 840, 27 / 840, 272 / 840, 27 / 840, 216 / 840, 41 / 840]
    C_7 = [751 / 17280, 3577 / 17280, 1323 / 17280, 2989 / 17280, 2989 / 17280, 1323 / 17280, 3577 / 17280, 751 / 17280]
    C_n = [C_1, C_2, C_3, C_4, C_5, C_6, C_7]

    def __init__(self, func):
        self.func = func

    def Newton_Cotes(self, a, b, n):
        """
        区间数值积分
        :param a: 区间
        :param b: 区间
        :param n: 等分次数, 1, 2, 3,... 对应 梯形求积, Simpson求积, Cotes求积
        :return: 积分值
        """
        x = np.linspace(a, b, n + 1)
        c_n = np.array(self.C_n[n - 1])
        s = c_n @ self.func(x)
        return (b - a) * s

    def complex_integral(self, a, b, d, n):
        """
        复合求积法(先对区间分段, 每段使用Cotes积分)
        :param a:
        :param b:
        :param d: 将大区间分成d段
        :param n: 每个小区间等分次数, 1, 2, 3,... 对应 梯形求积, Simpson求积, Cotes求积
        :return:
        """
        interval_point = np.linspace(a, b, d + 1)
        s = 0
        for i in range(d):
            a_i = interval_point[i]
            b_i = interval_point[i + 1]
            s += self.Newton_Cotes(a_i, b_i, n)
        return s

    def auto_step_integral(self, a, b, n, eps):
        """
        自动步长复合求积
        :param eps: 精度
        :param a:
        :param b:
        :param n: 等分次数, 1, 2, 3,... 对应 梯形求积, Simpson求积, Cotes求积
        :return: 积分值, 分割段数, 误差
        """
        m = (2 * n) ** 2 - 1  # 系数
        s1 = self.complex_integral(a, b, 1, n)  # 不分段(分段数为1)
        delta = np.inf
        d = 1
        while delta > eps:
            d *= 2  # 步长缩短一半(分段数*2)
            sd = self.complex_integral(a, b, d, n)
            delta = abs(s1 - sd) / m  # 计算相邻两次积分差
            s1 = sd
        return s1, d, delta

    def romberg(self, a, b, eps, m=5):
        """
        Romberg求积
        :param a:
        :param b:
        :param eps:
        :param m: 加速次数, 矩阵阶数
        :return:
        """
        matrix = np.zeros((m + 1, m + 1), dtype=np.float64)
        matrix[0, 0] = self.complex_integral(a, b, 1, 1)

        for i in range(1, m + 1):
            matrix[i, 0] = self.complex_integral(a, b, 2 ** i, 1)
            s = matrix[i, 0]
            if abs(s - matrix[i - 1, 0]) <= eps:    # 第一列前后比较
                # print(matrix)
                return s
            for j in range(1, i + 1):
                matrix[i, j] = (4 ** j * matrix[i, j - 1] - matrix[i - 1, j - 1]) / (4 ** j - 1)
            s = matrix[i, i]    # 对角线
            if abs(s - matrix[i, i - 1]) <= eps:    # 对角线相邻比较
                # print(matrix)
                return s
        print("未达到精度")

    def integral(self, a, b, eps):  # 默认函数简化函数名
        answer = self.romberg(a, b, eps)
        return answer


if __name__ == '__main__':
    def func(x):
        return np.where(x == 0, 1, np.sin(x) / x)


    Itg = Integral(func)
    ans = Itg.integral(0, 1, 1e-06)
    print(ans)
