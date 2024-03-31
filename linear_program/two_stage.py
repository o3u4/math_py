from linear_program.artificial_var import iter_add
from linear_program.simple_method import iterate
import sympy as sp

d = 3
A = [[1, 1, 1, 0, 7],
     [2, -5, 1, 1, 10]]
max_f = [2, 3, -5]


def two_stage_solve(matrix, target_f, process=False):
    dimension = len(target_f)
    matrix, lst = iter_add(matrix, dimension)  # 变换后矩阵及人工变量索引
    n = len(matrix[0])
    for i in range(len(target_f), n - 1):
        if i in lst:
            target_f.append(-1)
        else:
            target_f.append(0)
    stage1_f = []
    for i in range(n - 1):
        if i in lst:
            stage1_f.append(-1)
        else:
            stage1_f.append(0)
    print("----------------第一阶段----------------")
    matrix2, z = iterate(matrix, stage1_f, process)[0: 2]

    if z != 0:
        print("该问题无解, 检查可行域!")
    else:
        print("----------------第二阶段----------------")
        M = sp.Matrix(matrix2)
        stage2_f = [value for index, value in enumerate(target_f) if index not in lst]
        M = M[:, [i for i in range(M.shape[1]) if i not in lst]]
        M = M.tolist()
        iterate(M, stage2_f, process)


if __name__ == '__main__':
    two_stage_solve(A, max_f)
