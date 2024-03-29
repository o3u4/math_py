import sympy as sp

d = 3
A = [[1, 1, 1, 0, 7],
     [2, -5, 1, 1, 10]]


def add_col(matrix, row, col):
    """
    根据需要判断的符号行列定位，对矩阵某一列加入剩余,松弛变量和人工变量
    :param matrix: 矩阵
    :param row: 目标符号所在行号
    :param col: 目标符号所在列号
    :return:
    matrix: 变换后的矩阵
    index: 变换后符号列所在列
    var: 人工变量所在列索引
    """
    M = sp.Matrix(matrix)
    m_ = len(matrix)
    if matrix[row][col] == 0:  # 目标符号为 =
        col_1 = M.zeros(m_, 1)
        col_1[row, 0] = 1  # 第row个元素为1, 其余全为0
        M = M.col_insert(col, col_1)
        index = col + 1
        matrix = M.tolist()
        var = col
    elif matrix[row][col] == 1:
        col_1 = M.zeros(m_, 1)
        col_1[row, 0] = -1  # 第row个元素为-1, 其余全为0
        col_2 = M.zeros(m_, 1)
        col_2[row, 0] = 1  # 第row个元素为1, 其余全为0
        M = M.col_insert(col, col_1)  # 添加松弛变量
        M = M.col_insert(col + 1, col_2)  # 添加人工变量
        index = col + 2
        matrix = M.tolist()
        var = col + 1
    else:
        col_1 = M.zeros(m_, 1)
        col_1[row, 0] = 1  # 第row个元素为1, 其余全为0
        M = M.col_insert(col, col_1)  # 添加剩余变量
        index = col + 1
        matrix = M.tolist()
        var = -1
    return matrix, index, var


def iter_add(matrix, dimension):
    """
    添加人工变量, 输出人工变量所在列索引
    :param matrix: 矩阵
    :param dimension: 初始决策变量个数
    :return:
    matrix: 变换后的矩阵
    at_var: 人工变量所在列索引列表
    """
    m = len(matrix)
    mat = matrix  # 初始矩阵
    col_n = dimension  # 初始符号列
    at_var = []
    for j in range(m):  # 行迭代
        mat, col_n, v = add_col(mat, j, col_n)  # 更新变换后的矩阵和符号列索引
        if v != -1:
            at_var.append(v)
    mat = sp.Matrix(mat)
    mat.col_del(col_n)
    matrix = mat.tolist()
    return matrix, at_var


if __name__ == '__main__':
    ma, lst = iter_add(A, d)
    print(ma)
    print(lst)
