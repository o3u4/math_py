import numpy as np


class Interpolation:
    def __init__(self, x_lst, y_lst):
        self.x_lst = x_lst
        self.y_lst = y_lst

    def base_func(self, i):
        def li(x_):
            l = np.prod([x_ - factor for factor in self.x_lst if factor != self.x_lst[i]])
            l_ = np.prod([self.x_lst[i] - factor for factor in self.x_lst if factor != self.x_lst[i]])
            l = l / l_
            return l

        return li

    def Lagrange_fit(self):
        n = len(self.x_lst)

        def Lagrange_fit_function(x_):
            s = 0
            for i in range(n):
                s += self.y_lst[i] * self.base_func(i)(x_)
            return s

        return Lagrange_fit_function

    @staticmethod
    def diff_div(f1, f2, x1, x2):
        return (f2 - f1) / (x2 - x1)

    def newton_linear(self):  # Newton 线性插值
        n = len(self.x_lst)
        A = np.zeros((n, n), dtype=np.float64)
        A[:, 0] = self.y_lst
        for j in range(1, n):
            for i in range(j, n):
                A[i, j] = self.diff_div(A[i, j - 1], A[i - 1, j - 1], self.x_lst[i], self.x_lst[i - j])
        coe = A.diagonal()  # Newton 多项式系数

        def newton_fit_function(x_):
            p = coe[0]
            for i in range(1, n):
                p += coe[i] * np.prod([(x_ - factor) for factor in self.x_lst[:i]])
            return p

        return newton_fit_function, A

    def two_order_fit(self, x_):  # 分段二阶插值(取三点)
        n = len(self.x_lst)
        n_ = 0
        if x_ <= self.x_lst[0]:
            n_ = 0
        elif x_ >= self.x_lst[-1]:
            n_ = n
        for i in range(n - 1):
            if (x_ >= self.x_lst[i]) & (x_ <= self.x_lst[i + 1]):
                n_ = i
        use_x = self.x_lst[n_: n_ + 3]
        use_y = self.y_lst[n_: n_ + 3]
        if (x_ - self.x_lst[n_]) < (self.x_lst[n_ + 1] - x_):
            use_x = self.x_lst[n_ - 1: n_ + 2]
            use_y = self.y_lst[n_ - 1: n_ + 2]
        y_ = use_y[0] * (x_ - use_x[1]) * (x_ - use_x[2]) / ((use_x[0] - use_x[1]) * (use_x[0] - use_x[2])) \
             + use_y[1] * (x_ - use_x[0]) * (x_ - use_x[2]) / ((use_x[1] - use_x[0]) * (use_x[1] - use_x[2])) \
             + use_y[2] * (x_ - use_x[0]) * (x_ - use_x[1]) / ((use_x[2] - use_x[0]) * (use_x[2] - use_x[1]))
        return y_


if __name__ == '__main__':
    x = [0.4, 0.5, 0.6, 0.7, 0.8]
    y = [-0.9163, -0.6931, -0.5108, -0.3567, -0.2231]
    y_ = [np.log(i) for i in x]
    fit_class = Interpolation(x, y)
    f, a = fit_class.newton_linear()
    print("Newton插值", f(0.54), "真实值", np.log(0.54))
    print("分段二阶插值", fit_class.two_order_fit(0.54))
    print("Lagrange插值", fit_class.Lagrange_fit()(0.54))
