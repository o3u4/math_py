import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from load_data.load_excel import ExcelLoader
from math import gamma
from scipy.optimize import curve_fit
from scipy.stats import kstest
from fitting.func_fit import Fit

plt.style.use('seaborn-v0_8')  # 风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\data/第七轮死亡人口.xlsx"
csv = r'C:\Users\WIN10\Desktop\数模\第五轮\C题/data/第七轮年龄、男女人口数据.csv'
el = ExcelLoader(csv)
data = el.load_csv()
# el.trans_to_csv(data, csv)
print(data.head())

df = pd.DataFrame(data)


# 定义广义Gamma分布函数
def generalized_gamma_pdf(x, c, a, d, p):
    return (c * p / (a ** d * gamma(d / p))) * (x ** (d - 1)) * np.exp(-(x / a) ** p)


def fit_pdf(x_, y1, y2):
    # 使用curve_fit拟合广义Gamma分布到数据
    initial_guess1 = [17542638.0, 18, 2, 3]  # 参数的初始猜测值
    initial_guess2 = [3264990, 18, 5, 17]  # 参数的初始猜测值

    params1, covariance1 = curve_fit(generalized_gamma_pdf, x_, y1, p0=initial_guess1)
    params2, covariance2 = curve_fit(generalized_gamma_pdf, x_, y2, p0=initial_guess2)
    return params1, params2


def gamma_normal(x, c, a, b):
    return c * b ** a / gamma(a) * (x ** (a - 1)) * np.exp(-b * x)


def weibull(x, c, k, a):
    return c * k / a * (x / a) ** (k - 1) * np.exp(-(x / a) ** k)


def fit_gamma_normal(x_, y1, y2):
    # 使用curve_fit拟合广义Gamma分布到数据
    initial_guess1_ = [1475, 1.5, 1.5]  # 参数的初始猜测值
    initial_guess2_ = [1475, 1.5, 1.5]  # 参数的初始猜测值

    params1, covariance1 = curve_fit(gamma_normal, x_, y1, p0=initial_guess1_)
    params2, covariance2 = curve_fit(gamma_normal, x_, y2, p0=initial_guess2_)
    return params1, params2


def fit_weibull(x_, y1, y2):
    # 使用curve_fit拟合广义Gamma分布到数据
    initial_guess1_ = [1475, 1.5, 1.5]  # 参数的初始猜测值
    initial_guess2_ = [1475, 1.5, 1.5]  # 参数的初始猜测值

    params1, covariance1 = curve_fit(weibull, x_, y1, p0=initial_guess1_)
    params2, covariance2 = curve_fit(weibull, x_, y2, p0=initial_guess2_)
    return params1, params2


# 提取数据
age_labels = df['年龄段']
x = np.arange(len(age_labels))  # 将年龄段转化为数字序列

y_male = df['男'] / 10 ** 4
y_female = df['女'] / 10 ** 4

# params1, params2 = fit_weibull(x, y_male, y_female)
# c_fit1, k_fit1, a_fit1 = params1
# c_fit2, k_fit2, a_fit2 = params2
# # 打印拟合的参数
# print(f"拟合的参数: c1 = {c_fit1}, k1 = {k_fit1}, a1 = {a_fit1}")
# print(f"拟合的参数: c2 = {c_fit2}, k2 = {k_fit2}, a2 = {a_fit2}")
#
# plt.figure(figsize=(10, 6))
# x_ = np.linspace(0, len(age_labels), 100)
# plt.scatter(x, y_male, color='#5433AB', facecolors='none', label='男',
#             marker='o', s=15, linewidths=1)
# plt.scatter(x, y_female, color='#C35540', facecolors='none', label='女',
#             marker='o', s=15, linewidths=1)
#
# plt.plot(x_, weibull(x_, *params1), label='男(Weibull拟合)', color='#509caf')
# plt.plot(x_, weibull(x_, *params2), label='女(Weibull拟合)', color='#8a72a5')
#
# # 设置图例和标签
# plt.xticks(x[::3], [int(i * 100 / 21) for i in x[::3]], rotation=0)  # 每隔一个标签显示一次  # 设置x轴为年龄段标签
# plt.xlabel('年龄段')
# plt.ylabel('人口数')
# plt.title('不同年龄段的男女人口数')
# plt.legend()
# plt.grid(True)

plt.scatter(x, y_male, color='#5433AB', facecolors='none', label='男',
            marker='o', s=15, linewidths=1)
plt.scatter(x, y_female, color='#C35540', facecolors='none', label='女',
            marker='o', s=15, linewidths=1)
plt.xticks(x[::3], [int(i * 100 / 21) for i in x[::3]], rotation=0)  # 每隔一个标签显示一次  # 设置x轴为年龄段标签
plt.xlabel('年龄段')
plt.ylabel('人口数(*10^4)')
plt.title('不同年龄段的男女人口数')
plt.legend()
plt.grid(True)
# 显示图表
plt.show()
