# 求解线性规划的单纯形法
import sympy as sp


def simplify(xb, A_):
    """
    根据基变量下标简化矩阵
    :param xb: 基变量下标列表
    :param A_: 变换的矩阵 (A|b)
    :return:
    变换后的矩阵 (A|b)
    """
    c = len(A_[0])
    M = sp.Matrix(A_)
    ori = [i for i in range(c)]
    d = [i - 1 for i in xb]
    tran = [i for i in ori if i not in d]
    for j in tran:
        d.append(j)
    a = [M.col(j) for j in d]
    M = a[0]
    for i in range(1, len(a)):
        M = M.row_join(a[i])
    # print(M.tolist())
    # 基向量放最前面

    M = M.rref()[0]  # 简化
    # print(M.tolist())

    # 换回原位
    b = [M.col(i) for i in range(c)]
    for i in range(c):
        M[:, d[i]] = b[i]

    return M.tolist()


def operation(Xb_, A_):
    """
    迭代一次
    :param Xb_: 目前基变量下标列表
    :param A_: 变换的矩阵
    :return:
    flag: 是否需要下一次迭代
    A_: 矩阵
    Xb_: 更新后的基变量下标
    Z: 目标函数值
    lam_lst: 检验系数列表
    theta_lst: θ值列表
    """
    flag = True
    Cb = sp.Matrix([max_f[x - 1] for x in Xb_])  # 基变量系数

    M = sp.Matrix(A_)

    b = M.col(n - 1)  # 约束右边项

    Z = Cb.dot(b)  # 目标函数值

    lam_lst = []  # 检验系数
    for j in range(n - 1):
        pi = M.col(j)
        lbd = max_f[j] - Cb.dot(pi)
        lam_lst.append(lbd)
    if max(lam_lst) <= 0:
        flag = False
    col_in_order = lam_lst.index(max(lam_lst))  # 入基变量的序数, 最大的检验系数
    col_in = M.col(col_in_order)

    theta_lst = []
    for k in range(m):
        if col_in[k] != 0:
            theta = b[k] / col_in[k]
        else:
            theta = 0
        theta_lst.append(theta)
    row_out_num = theta_lst.index(min([x for x in theta_lst if x > 0]))
    out_var = Xb_[row_out_num]  # 出基变量下标

    for x in range(len(Xb_)):  # 更新基变量
        if Xb_[x] == out_var:
            Xb_[x] = col_in_order + 1  # 入基变量的下标
    return flag, A_, Xb_, Z, lam_lst, theta_lst


if __name__ == '__main__':
    dimension = 3
    max_f = [2, 4, 5, 0, 0, 0]
    A = [[1, 3, -1, 1, 0, 0, 6],
         [0, 2, 2, 0, 1, 0, 4],
         [3, 1, 2, 0, 0, 1, 7]]
    m = len(A)
    n = len(A[0])
    X = [i + 1 for i in range(dimension, dimension + m)]  # 初始基变量下标
    while 1:
        a, b, c, d, e, f = operation(X, A)
        X = c
        if a:
            A = simplify(X, A)
        else:
            print('最终矩阵为:', b)
            print('最终基变量下标为', c)
            print('最优值为:', d)
            print('各项检验系数为:', e)
            break
