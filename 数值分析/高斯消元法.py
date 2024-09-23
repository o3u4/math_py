def gaussian_elimination(A, b, method=0):
    n = len(b)

    # 构建增广矩阵
    Ab = [row[:] + [b[i]] for i, row in enumerate(A)]  # 增广矩阵

    # 消元过程
    for i in range(n):
        # 0 为普通消元, 否则为列主元消元
        if method == 0:
            pass
        else:
            # 列主元选取
            max_row_index = max(range(i, n), key=lambda r: abs(Ab[r][i]))
            # 行交换
            if max_row_index != i:
                Ab[i], Ab[max_row_index] = Ab[max_row_index], Ab[i]

        # 对于当前主元素所在的列进行消元
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]  # 计算消元因子
            for k in range(i, n + 1):  # 更新当前行
                Ab[j][k] -= factor * Ab[i][k]

    # 回代求解
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i][n] - sum(Ab[i][j] * x[j] for j in range(i + 1, n))) / Ab[i][i]

    return x


# 示例
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

solution = gaussian_elimination(A, b)
print("普通高斯消去法解:", solution)

solution2 = gaussian_elimination(A, b, 1)
print("列主元高斯消去法解:", solution2)
