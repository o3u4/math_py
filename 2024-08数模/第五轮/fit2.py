import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from load_data.load_excel import ExcelLoader
from math import gamma
from scipy.optimize import curve_fit
from scipy.stats import kstest, gamma as gamma_dist

# 设置风格
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\data/第七轮死亡人口.csv"
el = ExcelLoader(path)
data = el.load_csv()
df = pd.DataFrame(data)


# 定义广义Gamma分布函数的PDF和CDF (PDF概率密度函数, CDF累积分布函数)
def generalized_gamma_pdf(x, c, a, d, p):
    return (c * p / (a ** d * gamma(d / p))) * (x ** (d - 1)) * np.exp(-(x / a) ** p)


def generalized_gamma_cdf(x, a, d, p):
    from scipy.special import gammainc
    return gammainc(d / p, (x / a) ** p)


# 定义Gamma分布函数的PDF和CDF
def gamma_normal_pdf(x, c, a, b):
    return c * b ** a / gamma(a) * (x ** (a - 1)) * np.exp(-b * x)


def gamma_normal_cdf(x, a, b):
    return gamma_dist.cdf(x, a, scale=1 / b)


# 拟合函数
def fit_pdf(x_, y1, y2):
    # 使用curve_fit拟合广义Gamma分布到数据
    initial_guess1 = [17542638.0, 18, 2, 3]  # 参数的初始猜测值
    initial_guess2 = [3264990, 18, 5, 17]  # 参数的初始猜测值

    params1, covariance1 = curve_fit(generalized_gamma_pdf, x_, y1, p0=initial_guess1)
    params2, covariance2 = curve_fit(generalized_gamma_pdf, x_, y2, p0=initial_guess2)
    return params1, params2


def fit_gamma_normal(x_, y1, y2):
    initial_guess1_ = [1475, 4, 11]
    initial_guess2_ = [1475, 4, 11]

    params1, _ = curve_fit(gamma_normal_pdf, x_, y1, p0=initial_guess1_)
    params2, _ = curve_fit(gamma_normal_pdf, x_, y2, p0=initial_guess2_)
    return params1, params2


def weibull(x, c, k, a):
    return c * k / a * (x / a) ** (k - 1) * np.exp(-(x / a) ** k)


def weibull_cdf(x, k, a):
    return 1 - np.exp(-(x / a) ** k)


def fit_weibull(x_, y1, y2):
    # 使用curve_fit拟合广义Gamma分布到数据
    initial_guess1_ = [1475, 1.5, 1.5]  # 参数的初始猜测值
    initial_guess2_ = [1475, 1.5, 1.5]  # 参数的初始猜测值

    params1, covariance1 = curve_fit(weibull, x_, y1, p0=initial_guess1_)
    params2, covariance2 = curve_fit(weibull, x_, y2, p0=initial_guess2_)
    return params1, params2


# 提取数据
age_labels = df['年龄段']
x = np.arange(len(age_labels))

y_male = df['男']
y_female = df['女']

# # Gamma分布拟合
# params1_gamma, params2_gamma = fit_gamma_normal(x, y_male, y_female)
# c_fit1, a_fit1, b_fit1 = params1_gamma
# c_fit2, a_fit2, b_fit2 = params2_gamma

# # Weibull分布拟合
# params1_wb, params2_wb = fit_weibull(x, y_male, y_female)
# c_fit1, k_fit1, a_fit1 = params1_wb
# c_fit2, k_fit2, a_fit2 = params2_wb

# 打印拟合的参数
# print(f"Gamma分布拟合参数: 男 -> c={c_fit1}, a={a_fit1}, b={b_fit1}")
# print(f"Gamma分布拟合参数: 女 -> c={c_fit2}, a={a_fit2}, b={b_fit2}")
# 打印拟合的参数
# print(f"Weibull分布拟合参数: 男 -> c={c_fit1}, k={k_fit1}, a={a_fit1}")
# print(f"Weibull分布拟合参数: 女 -> c={c_fit2}, k={k_fit2}, a={a_fit2}")
# 广义Gamma拟合
params1_gen_gamma, params2_gen_gamma = fit_pdf(x, y_male, y_female)
c_fit1, a_fit1, d_fit1, p_fit1 = params1_gen_gamma
c_fit2, a_fit2, d_fit2, p_fit2 = params2_gen_gamma
# 打印拟合的参数
print(f"拟合的参数: c1 = {c_fit1}, a1 = {a_fit1}, d1 = {d_fit1}, p1 = {p_fit1}")
print(f"拟合的参数: c2 = {c_fit2}, a2 = {a_fit2}, d2 = {d_fit2}, p2 = {p_fit2}")

# # 执行K-S检验 (比较CDF)
# ks_statistic_male_gamma, p_value_male_gamma = kstest(y_male, lambda x: gamma_normal_cdf(x, *params1_gamma[1: ]))
# ks_statistic_female_gamma, p_value_female_gamma = kstest(y_female, lambda x: gamma_normal_cdf(x, *params2_gamma[1: ]))

# ks_statistic_male_wb, p_value_male_wb = kstest(y_male, lambda x: weibull_cdf(x, *params1_wb[1:]))
# ks_statistic_female_wb, p_value_female_wb = kstest(y_female, lambda x: weibull_cdf(x, *params2_wb[1:]))

ks_statistic_male_gen_gamma, p_value_male_gen_gamma = (
    kstest(y_male,lambda x: generalized_gamma_cdf(x, *params1_gen_gamma[1:])))
ks_statistic_female_gen_gamma, p_value_female_gen_gamma = (
    kstest(y_female, lambda x: generalized_gamma_cdf(x, *params2_gen_gamma[1:])))

# 打印K-S检验结果
# print(f"K-S检验(Weibull) 男：统计量={ks_statistic_male_wb}, p值={p_value_male_wb}")
# print(f"K-S检验(Weibull) 女：统计量={ks_statistic_female_wb}, p值={p_value_female_wb}")
# print(f"K-S检验(Weibull) 男：统计量={ks_statistic_male_gamma}, p值={p_value_male_gamma}")
# print(f"K-S检验(Weibull) 女：统计量={ks_statistic_female_gamma}, p值={p_value_female_gamma}")
print(f"K-S检验(广义Gamma) 男：统计量={ks_statistic_male_gen_gamma}, p值={p_value_male_gen_gamma}")
print(f"K-S检验(广义Gamma) 女：统计量={ks_statistic_female_gen_gamma}, p值={p_value_female_gen_gamma}")
