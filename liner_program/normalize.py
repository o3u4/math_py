# 化为标准型, 矩阵 <=, >=, 0的顺序从上到下
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


def add_var(matrix, d):  # 标准化
    m = len(matrix)
    neg_num = 0  # 松弛变量个数
    pos_num = 0  # 剩余变量个数
    for it in matrix:
        if it[d] == -1:
            neg_num += 1
        if it[d] == 1:
            pos_num += 1

    ma = sp.Matrix(matrix)
    ma.col_del(d)  # 去除符号项

    if m > neg_num > 0:  # 添加松弛变量
        i = sp.eye(neg_num)
        a = sp.zeros((m - neg_num), neg_num)
        slack = i.row_insert(neg_num, a)
        ma = ma.col_insert(d, slack)

    elif neg_num == m:
        ma = ma.col_insert(d, sp.eye(neg_num))

    if m > pos_num > 0:  # 添加剩余变量
        i = sp.eye(pos_num)
        a = sp.zeros((m - pos_num), pos_num)
        slack = i.row_insert(pos_num, a)
        ma = ma.col_insert(d, slack)
    elif pos_num == m:
        ma = ma.col_insert(d, sp.eye(pos_num))

    # ma = ma.col_insert(d + neg_num + pos_num, sp.zeros(m, 1))
    ma = ma.tolist()
    return ma


def normal(is_var_positive, matrix):
    matrix = neg_to_positive(is_var_positive, matrix)
    number = len(is_var_positive)       # 决策变量个数
    matrix = add_var(matrix, number)
    print('----------------标准化矩阵为----------------')
    for i in range(len(matrix)):
        print(matrix[i])
    return number, matrix


if __name__ == '__main__':
    a, b = normal(positive, A)
    print(a, b)
    A = neg_to_positive(positive, A)
    print(A)
    m = add_var(A, 2)
    print(m)
