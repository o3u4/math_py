import numpy as np


class IterSolve:
    """
    迭代求解方程组
    """

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def deter_conv(self, method=1):
        D = np.diag(np.diag(self.A))
        if method == 1:
            # 判断收敛
            G = np.linalg.inv(D) @ (D - self.A)
            eigvals = np.linalg.eig(G)[0]
            rho = max(eigvals)
            if rho >= 1:
                print(f"谱半径为: {rho}, jacobi法不收敛")
                return False
            else:
                return True
        if method == 2:
            D = np.diag(np.diag(self.A))
            L = -np.tril(self.A, -1)
            U = -np.triu(self.A, 1)
            bg = np.linalg.inv(D - L) @ U
            eigvals = np.linalg.eig(bg)[0]
            rho = max(eigvals)
            if rho >= 1:
                print(f"谱半径为: {rho}, gauss_seidel法不收敛")
                return False
            else:
                return True

    def jacobi_iter(self, x_init, eps):
        """
        jacobi迭代
        :param x_init: 初始迭代点
        :param eps: 精度控制
        :return:
        """
        n = len(x_init)
        x_k = x_init
        x_k_1 = np.zeros_like(x_k, dtype=np.float64)
        while 1:
            for i in range(n):
                delta_x = (self.b[i] - self.A[i] @ x_k) / self.A[i, i]
                x_k_1[i] = x_k[i] + delta_x
            if np.linalg.norm(x_k - x_k_1) < eps:
                return x_k_1
            else:
                x_k = np.copy(x_k_1)

    def gauss_seidel_iter(self, x_init, eps):
        n = len(x_init)
        x_k = x_init
        x_k_1 = np.zeros_like(x_k, dtype=np.float64)
        while 1:
            for i in range(n):
                delta_x = (self.b[i] - self.A[i, : i] @ x_k_1[: i]
                           - self.A[i, i:] @ x_k[i:]) / self.A[i, i]
                x_k_1[i] = x_k[i] + delta_x
            if np.linalg.norm(x_k - x_k_1) < eps:
                return x_k_1
            else:
                x_k = np.copy(x_k_1)


if __name__ == '__main__':
    # A = np.array([[8, -3, 2],
    #               [4, 11, -1],
    #               [2, 1, 4]])
    # b = np.array([20, 33, 12])
    A = np.array([[1, 2, -2],
                  [1, 1, 1],
                  [2, 2, 1]])
    b = np.array([1, 1, 1])
    solve = IterSolve(A, b)
    s1 = solve.jacobi_iter([0, 0, 0], 1e-5)
    print(s1)
    print(solve.deter_conv(2))
    # s2 = solve.gauss_seidel_iter([0, 0, 0], 1e-5)
