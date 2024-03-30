from liner_program.artificial_var import iter_add
from liner_program.simple_method import iterate
import sympy as sp

d = 3
A = [[1, 1, 1, 0, 7],
     [2, -5, 1, 1, 10]]
max_f = [2, 3, -5]
M = 100  # 大M


def big_m_solve(matrix, target_f, var_m, process=False):
    dimension = len(target_f)
    matrix, lst = iter_add(matrix, dimension)  # 变换后矩阵及人工变量索引
    n = len(matrix[0])
    for i in range(len(target_f), n - 1):
        if i in lst:
            target_f.append(-var_m)
        else:
            target_f.append(0)
    Xb = iterate(matrix, target_f, process)[2]  # Xb为基向量下标
    lst = [k + 1 for k in lst]
    flag = True
    for i in lst:
        if i in Xb:
            flag = False
            break
    print('其中人工变量下标为:', lst)
    if not flag:
        print("无解, 检查可行域!")


if __name__ == '__main__':
    big_m_solve(A, max_f, 100, True)
