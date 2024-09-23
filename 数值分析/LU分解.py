import numpy as np


def LU(matrix):
    """
    普通的LU分解
    :param matrix:
    :return:
    """
    # 提取系数矩阵和增广矩阵的右侧
    n = matrix.shape[0]
    U = np.zeros((n, n))
    L = np.eye(n)  # 初始化L为单位矩阵

    # LU分解
    for j in range(n):
        for i in range(j + 1):
            U[i, j] = matrix[i, j] - L[i, :i] @ U[:i, j]
            print("U", U)
        for i in range(j + 1, n):
            L[i, j] = (matrix[i, j] - L[i, :j] @ U[:j, j]) / U[j, j]
            print("L", L)
    return L, U


def extract_LU(matrix, n):
    """
    从紧凑型Doolittle方法的矩阵里提取LU
    :param matrix:
    :param n:
    :return:
    """
    # 初始化L和U
    U = np.zeros((n, n))
    L = np.eye(n)  # 对角线为1的单位矩阵

    # 从A中提取U和L
    for i in range(n):
        for j in range(i, n):
            U[i, j] = matrix[i, j]  # U的上三角部分
        for j in range(i + 1, n):
            L[j, i] = matrix[j, i]  # L的下三角部分（对角线为1已在L中设置）
    return L, U


def Doolittle(Ab, eps, verbose=False):
    """
    紧凑型Doolittle方法, 直接在初始矩阵上求解
    :param Ab:
    :param eps:
    :param verbose:
    :return:
    """
    n = Ab.shape[0]

    # 第0列除以a00
    Ab[1:, 0] = Ab[1:, 0] / Ab[0, 0]

    if verbose:
        print("-----------------------LU分解-----------------------")
        print("第1步(第1行、第1列)")
        print(Ab)

    for r in range(1, n):
        for i in range(r, n + 1):
            left = Ab[r, :r]
            right = Ab[:r, i]
            Ab[r, i] = Ab[r, i] - left @ right

        if abs(Ab[r, r]) <= eps:
            if verbose:
                print("分解失败")
            break

        # 计算L的第r列元素
        if r < n - 1:
            for i in range(r + 1, n):
                left = Ab[i, :r]
                right = Ab[:r, r]
                Ab[i, r] = (Ab[i, r] - left @ right) / Ab[r, r]

        if verbose:
            print(f"第{r + 1}步(第{r + 1}行、第{r + 1}列)")
            print(Ab)

    if verbose:
        print("--------------------------------------------------")
        print("最终LU分解结果")
        print(Ab)

    # 解方程Ux=y
    if verbose:
        print("-----------------------解方程-----------------------")

    Ab[n - 1, n] = Ab[n - 1, n] / Ab[n - 1, n - 1]
    if verbose:
        print("解x_n")
        print(Ab)

    for k in range(n - 2, -1, -1):
        left_a = Ab[k, k + 1: n]
        right_x = Ab[k + 1: n, n]
        Ab[k, n] = (Ab[k, n] - left_a @ right_x) / Ab[k, k]

        if verbose:
            print(f"解x_{k + 1}")
            print(Ab)

    if verbose:
        print("--------------------------------------------------")
        print("最终解")
        print(Ab)

    x = Ab[:, -1]

    if verbose:
        print("解为:")
        print(x)

    L, U = extract_LU(Ab, n)
    return L, U, x


if __name__ == '__main__':
    B = np.array([[2, 10, 0, -3, 10],
                  [-3, -4, -12, 13, 5],
                  [1, 2, 3, -4, -2],
                  [4, 14, 9, -13, 7]], dtype=np.float64)
    l, u, x = Doolittle(B, 0.00001)
    # print(l)
    # print(u)
    # print(x)
    l1, u1 = LU(B)
    # print(l1)
    # print(u1)
