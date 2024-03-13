# 层次分析法

import numpy as np


def weight_calc(determinate):
    A = np.array(determinate)
    n = A.shape[0]

    # 特征值和特征向量
    eig_val, eig_vec = np.linalg.eig(A)
    Max_eig = max(eig_val)

    # 一致性检验
    CI = (Max_eig - n) / (n - 1)

    # RI为标准对照表, 不用修改
    RI = [0, 0.0001, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
    CR = CI / RI[n - 1]
    print('一致性指标CI=', CI)
    print('一致性比例CR=', CR)

    if CR < 0.1:
        print('因为CR<0.1, 判断矩阵A的一致性可以接受')
    else:
        print('CR>=0.1, 需要修改判断矩阵')

    # 算术平均求权重
    A_sum = np.sum(A, axis=0)

    # 归一化
    Stand_A = A / A_sum

    # 各列相加到同一行
    A_sum_r = np.sum(Stand_A, axis=1)

    # 求权重
    weights = A_sum_r / n
    return weights


if __name__ == '__main__':
    pass
