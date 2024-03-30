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


def operation(Xb_, A_, tar_f):
    """
    迭代一次
    :param tar_f: 目标函数系数
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
    Cb = sp.Matrix([tar_f[x - 1] for x in Xb_])  # 基变量系数

    M = sp.Matrix(A_)
    n__ = len(A_[0])

    b = M.col(n__ - 1)  # 约束右边项

    Z = Cb.dot(b)  # 目标函数值

    lam_lst = []  # 检验系数
    for j in range(n__ - 1):
        pi = M.col(j)
        lbd = tar_f[j] - Cb.dot(pi)
        lam_lst.append(lbd)
    if max(lam_lst) <= 0:
        flag = False
    col_in_order = lam_lst.index(max(lam_lst))  # 入基变量的序数, 最大的检验系数
    col_in = M.col(col_in_order)

    theta_lst = []
    m__ = len(A_)
    for k in range(m__):
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


def found_base(matrix):
    """
    找现成的单位矩阵, 按顺序返回变量下标
    :param matrix: 操作的矩阵
    :return:
    X: 基向量下标
    """
    M = sp.Matrix(matrix)
    m = len(matrix)
    n = len(matrix[0])
    X = []
    for i in range(m):
        for j in range(n):
            col = M.col(j)
            cl = sp.Matrix.zeros(m, 1)
            cl[i, 0] = 1
            if col == cl:
                X.append(j + 1)
    return X


def iterate(matrix, max_function, process_=False):
    """
    总体运行函数
    :param matrix: 矩阵
    :param max_function: 目标函数 max的系数
    :param process_: 是否输出过程
    :return:
    b_: 变换之后最后的矩阵
    d_: 迭代之后的最值
    c_: 迭代之后的基向量下标
    """
    m_ = len(matrix)
    X_ = found_base(matrix)  # 初始基变量下标
    r_ = 0  # 迭代次数
    while 1:
        a_, b_, c_, d_, e_, f_ = operation(X_, matrix, max_function)
        r_ += 1
        if process_:
            print(f'----------------第{r_}次迭代----------------')
            print('矩阵A为:')
            for item in range(m_):
                print(b_[item])
            print('更新后基变量下标为:', c_)
            print('最值Z为:', d_)
            print('各项检验系数λ为:', e_)
            print('θ值为:', f_)
        X_ = c_
        if a_:
            matrix = simplify(X_, matrix)
        else:
            print(f'----------------最终迭代{r_}次----------------')
            print('最终矩阵A为:')
            for item in range(m_):
                print(b_[item])
            print('最终基变量下标为', c_)
            print('最优值Z为:', d_)
            print('各项检验系数λ为:', e_)
            n = len(b_[0]) - 1
            B = sp.Matrix(b_)[:, -1].tolist()
            print('----------------最终变量值为----------------')
            for i in range(n):
                if i + 1 in c_:
                    index = c_.index(i + 1)
                    print(f'x{i + 1} = {B[index][0]}')
                else:
                    print(f"x{i + 1} = 0")
            break
    return b_, d_, c_


if __name__ == '__main__':
    dimension = 3
    max_f = [2, 4, 5, 0, 0, 0]
    A = [[1, 3, -1, 1, 0, 0, 6],
         [0, 2, 2, 0, 1, 0, 4],
         [3, 1, 2, 0, 0, 1, 7]]
    M = iterate(A, max_f, True)[0]
    print(M)
