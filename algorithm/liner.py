# 线性回归

import pandas as pd
from scipy.stats import linregress


def linear_regression(df, x_column, y_column):
    # 提取自变量和应变量的数据
    x_column_data = df.iloc[:, x_column]
    # row_mean_x = x_column_data.mean()
    y_column_data = df.iloc[:, y_column]
    # row_mean_y = y_column_data.mean()
    # new_df_x = x_column_data - row_mean_x
    # new_df_y = y_column_data - row_mean_y

    x = list(x_column_data[0: 6])
    y = list(y_column_data[0: 6])

    # 进行线性回归
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    # 返回线性回归的关系式
    return round(slope, 5), round(intercept, 5)


def create_regression_function(slope, intercept):
    # 创建线性回归的函数
    def regression_function(x):
        return slope * x + intercept

    return regression_function


def gen_func():
    func_lst = []
    # 读取包含数据的Excel文件
    f = pd.read_excel('dt.xlsx')
    for item in range(1, 18):
        # 调用线性回归函数
        a, b = linear_regression(f, 0, item)
        print(f'{item}: y = {a}x + {b}')
        # 调用创建线性回归函数的函数
        regression_func = create_regression_function(a, b)
        func_lst.append((a, b))
    return func_lst


if __name__ == '__main__':
    lst = gen_func()
