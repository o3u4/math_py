import numpy as np


def admm_qp(A, q, B, b, C, d, beta=1.0, max_iter=100, tol=1e-4):
    """
    使用ADMM算法求解二次规划问题
    min (1/2) x^T A x + q^T x
    s.t. Bx = b, Cx <= d

    参数:
    A : ndarray
        对称正定矩阵 (n x n)
    q : ndarray
        线性项系数 (n,)
    B : ndarray
        线性约束矩阵 (m x n)
    b : ndarray
        线性约束右侧向量 (m,)
    C : ndarray
        不等式约束矩阵 (l x n)
    d : ndarray
        不等式约束右侧向量 (l,)
    beta : float
        ADMM的惩罚参数
    max_iter : int
        最大迭代次数
    tol : float
        收敛容限

    返回:
    x : ndarray
        最优解
    optimal_value : float
        最优目标函数值
    """
    # 初始化变量
    n = A.shape[0]
    x = np.zeros(n)
    y = np.zeros(b.shape[0] + d.shape[0])  # y的维度为b和d的维度之和
    lambda_ = np.zeros(B.shape[0] + C.shape[0])

    # 迭代过程
    for k in range(max_iter):
        # 计算z
        z = np.concatenate((b, d)) - np.dot(np.vstack([B, C]), x) - lambda_ / beta

        # 更新x
        A_hat = A + beta * (np.dot(np.vstack([B, C]).T, np.vstack([B, C])))
        b_hat = beta * np.dot(np.vstack([B, C]).T, z) - q
        x_new = np.linalg.solve(A_hat, b_hat)

        # 更新y
        P = np.concatenate((b, d)) - lambda_ / beta
        y_new = np.maximum(P, 0)  # 在非负部分上投影

        # 更新lambda
        lambda_ = lambda_ + beta * (np.dot(np.vstack([B, C]), x_new) + y_new - np.concatenate((b, d)))

        # 检查收敛
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new

    # 计算最优目标函数值
    optimal_value = 0.5 * np.dot(x.T, np.dot(A, x)) + np.dot(q, x)

    return x, optimal_value


if __name__ == '__main__':
    # 示例数据
    A = np.array([[2, 1], [1, 2]])
    q = np.array([-3, -4])
    B = np.array([[1, 1]])
    b = np.array([1])
    C = np.array([[-1, 0]])
    d = np.array([0])

    # 调用ADMM算法求解
    optimal_x, optimal_value = admm_qp(A, q, B, b, C, d)

    # 输出结果
    print("最优解 x:", optimal_x)
    print("最优值:", optimal_value)
