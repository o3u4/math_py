import sympy as sp

dim = 2  # 目标函数决策变量个数
positive = [1, 1]  # 决策变量非负性, 1为非负, 0为任意, -1为非正
A = [[8, 4, -1, 360],  # 第 dim + 1 个元素为-1表示 <= , 0表示 = , 1表示 >
     [4, 5, -1, 200],
     [3, 10, -1, 250],
     [4, 6, -1, 200]]


def neg_to_positive(p, matrix):  # 标准化非正变量
    neg = []
    for pos in range(len(p)):  # 记下非正决策变量
        if p[pos] == -1:
            neg.append(pos)

    if len(neg) != 0:  # 替换非正变量
        for n in neg:
            for i in matrix:
                i[n] = - i[n]
            p[n] = 1  # 更新决策变量非负性
    return matrix


def add_col(matrix, row, col):
    M = sp.Matrix(matrix)
    m_ = len(matrix)
    if matrix[row][col] == 0:  # 目标符号为 =
        index = col
    elif matrix[row][col] == 1:
        col_1 = M.zeros(m_, 1)
        col_1[row, 0] = -1  # 第row个元素为-1, 其余全为0
        M = M.col_insert(col, col_1)  # 添加松弛变量
        index = col + 1
        matrix = M.tolist()
    else:
        col_1 = M.zeros(m_, 1)
        col_1[row, 0] = 1  # 第row个元素为1, 其余全为0
        M = M.col_insert(col, col_1)  # 添加剩余变量
        index = col + 1
        matrix = M.tolist()
    return matrix, index


def iter_add(matrix, dimension):
    m_ = len(matrix)
    mat = matrix  # 初始矩阵
    col_n = dimension  # 初始符号列
    for j in range(m_):  # 行迭代
        mat, col_n = add_col(mat, j, col_n)  # 更新变换后的矩阵和符号列索引
    mat = sp.Matrix(mat)
    mat.col_del(col_n)
    matrix = mat.tolist()
    return matrix


def normal(is_var_positive, matrix):
    matrix = neg_to_positive(is_var_positive, matrix)
    number = len(is_var_positive)  # 决策变量个数
    matrix = iter_add(matrix, number)
    print('----------------标准化矩阵为----------------')
    for i in range(len(matrix)):
        print(matrix[i])
    return number, matrix


if __name__ == '__main__':
    a, b = normal(positive, A)
    print(a, b)
