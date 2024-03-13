# 相关系数

import pandas as pd


# 返回系数表
def calculate_spearman_correlation(*args):
    # 将传入的参数组合成DataFrame
    df = pd.DataFrame(args).T

    # 计算Spearman相关系数
    corr_matrix = df.corr(method='spearman')

    return corr_matrix


def find_representative_variable(correlation_matrix):
    # 计算每个变量与其他变量的相关系数之和
    total_correlation = correlation_matrix.sum()

    # 找到和其余变量都很有关系的一个变量代表所有
    representative_variable = total_correlation.idxmax()

    return representative_variable


if __name__ == '__main__':
    # 假设有一些变量a, b, c, d
    a = [1, 3, 11, 4]
    b = [2, 5, 4, 5]
    c = [3, 1, 5, 6]
    d = [0, 5, 4, 7]
    data_name = ['a', 'b', 'c', 'd']
    data = [a, b, c, d]

    # 计算相关系数表
    corr_table = calculate_spearman_correlation(*data)
    print(corr_table)
    value = corr_table.iloc[0, 1]   # 获取表格数据, 类型为 numpy.float64

    # 找出代表所有变量的一个变量
    representative_index = find_representative_variable(corr_table)
    print(data_name[representative_index])
