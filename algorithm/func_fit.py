# 自定义函数拟合

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# 定义拟合函数
def sin_function(x, a, b, c, d):
    return a * np.sin(b * x + c) + d


def point_fit(f, x, y):
    # 准备数据

    # 使用 curve_fit 进行拟合
    popt, pcov = curve_fit(f, x, y)

    # 输出拟合得到的参数
    # print("拟合参数:", popt)
    return list(popt)
    # # 绘制原始数据和拟合曲线
    # plt.scatter(x, y, label='Original data')
    # x = np.linspace(1, 12, 1000)
    # plt.plot(x, smooth_function(x, *popt), 'r-', label='Fitted curve')
    # plt.legend()
    # plt.show()


if __name__ == '__main__':
    x = np.arange(1, 13)
    y = [-0.020000000000038654, -0.10000000000002274, -0.10000000000002274, -0.060000000000030695,
         -0.020000000000038654,
         0.05999999999997385, 0.14999999999997726, 0.12999999999996703, 0.08999999999997499, 0.01999999999995339,
         -0.03000000000002956, -0.12000000000003297]
    paras = point_fit(sin_function, x, y)
    print(paras)
    x = np.linspace(1, 12, 1000)
    plt.plot(x, sin_function(x, *paras), 'r-', label='Fitted curve')
    plt.legend()
    plt.show()
