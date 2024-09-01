import matplotlib.pyplot as plt
import numpy as np
from load_data.load_excel import ExcelLoader
import pandas as pd
from fitting.func_fit import Fit
from scipy.stats import norm
from scipy.optimize import curve_fit
from math import gamma


def normal_cdf(x, mu, sigma):
    return norm.cdf(x, loc=mu, scale=sigma)


def normal_pdf(x, mu, sigma):
    return norm.pdf(x, loc=mu, scale=sigma)


def generalized_gamma_pdf(x, a, d, p):
    return p / (a ** d * gamma(d / p)) * (x ** (d - 1)) * np.exp(-(x / a) ** p)


def generalized_gamma_cdf(x, a, d, p):
    from scipy.special import gammainc
    return gammainc(d / p, (x / a) ** p)


def generalized_gamma_mean(a, d, p):
    return a * (gamma((d + 1) / p) / gamma(d / p))


def generalized_gamma_std(a, d, p):
    mean = generalized_gamma_mean(a, d, p)
    mean_squared = a * a * (gamma((d + 2) / p) / gamma(d / p))
    variance = mean_squared - mean ** 2
    return np.sqrt(variance)


path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\data\第七轮死亡人口.csv"
el = ExcelLoader(path)
data = el.load_csv()
df = pd.DataFrame(data)
x_label = df["年龄段"]
x = np.arange(len(x_label))
df["总计"] = df["男"] + df["女"]
total = sum(df["总计"])
print(total)
df["占比"] = df["总计"] / total
y = df["占比"]
print(df.head())
lst = []
s = 0
for i in range(0, len(x_label)):
    s += y[i]
    lst.append(s)
series = pd.Series(lst)
df["累计"] = series
print(df.head())
z = df["累计"]

init = [18, 2, 3]
params, cov = curve_fit(generalized_gamma_cdf, x, z, p0=init)
print(params)

popt, pcov = curve_fit(normal_cdf, x, z, p0=[np.mean(x), np.std(x)])
# 从拟合中获取参数
mu, sigma = popt
print(mu, sigma)
print("正态分布真实参数:", {"均值": mu * 100 / 21, "标准差": sigma * 100 / 21})
real_mu = mu * 100 / 21
real_sigma = sigma * 100 / 21
mu_gamma = generalized_gamma_mean(*params)
sigma_gamma = generalized_gamma_mean(*params)
real_mu_gamma = mu_gamma * 100 / 21
real_sigma_gamma = sigma_gamma * 100 / 21
print("gamma分布参数:", f"a = {params[0]}, d = {params[1]}, p = {params[2]}")
print(f"拟合均值为:{mu_gamma}",
      f"拟合标准差为:{sigma_gamma}")
print(f"真实均值为:{real_mu_gamma}",
      f"真实标准差为:{real_sigma_gamma}")

# 使用拟合的参数绘制拟合曲线
x_fit = np.linspace(min(x), max(x), 100)
z_fit = normal_cdf(x_fit, mu, sigma)
y_fit = normal_pdf(x_fit, mu, sigma)

z_fit_ = generalized_gamma_cdf(x_fit, *params)
y_fit_ = generalized_gamma_pdf(x_fit, *params)

f = Fit("")
f_, ax = scatter_plot(x, y)
f_.suptitle('不同年龄段死亡人数占死亡总数比率', fontsize=16)
f_, ax = scatter_plot(x, z, point_label="真实值")
ax.plot(x_fit, z_fit, label="normal拟合值")
ax.set_xticks(x[::3])  # 每隔3个年龄段设置一个x轴刻度
ax.set_xticklabels(x_label[::3], rotation=0)
ax.legend()
f_.suptitle('不同年龄段寿命(死亡率)累计分布(正态分布拟合)', fontsize=16)

f2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(x, y, color="#7db3c6", label="真实值")
ax2.plot(x_fit, y_fit, label="normal拟合值")
ax2.plot()
ax2.set_xticks(x[::3])
ax2.set_xticklabels(x_label[::3], rotation=0)
ax2.legend()
f2.suptitle('不同年龄段寿命(死亡率)概率密度分布(正态分布拟合)', fontsize=16)

f_3, ax_3 = scatter_plot(x, z, point_label="真实值")
ax_3.plot(x_fit, z_fit_, label="gamma拟合值")
ax_3.set_xticks(x[::3])  # 每隔3个年龄段设置一个x轴刻度
ax_3.set_xticklabels(x_label[::3], rotation=0)
ax_3.legend()
f_3.suptitle('不同年龄段寿命(死亡率)累计分布(Gamma分布拟合)', fontsize=16)

f3, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(x, y, color="#7db3c6", label="真实值")
ax3.plot(x_fit, y_fit_, label="gamma拟合值")
ax3.set_xticks(x[::3])
ax3.set_xticklabels(x_label[::3], rotation=0)
ax3.legend()
f3.suptitle('不同年龄段寿命(死亡率)概率密度分布(Gamma分布拟合)', fontsize=16)
real_x = np.linspace(0, 100, 100)  # X 轴范围从 0 到 100

f4, ax4 = plt.subplots(figsize=(10, 6))
ax4.plot(x_fit, y_fit_, label="gamma拟合值")
ax4.axvline(x=mu_gamma + 0.5, color='#7db3c6', linestyle='--', label='均值')
ax4.text(mu_gamma + 0.5, 0.15, f'均值=71', color='black', ha='center')
ax4.axvline(x=13, color='#b6a999', linestyle='--', label='领保年龄')
ax4.text(11, 0.15, f'领保年龄=60', color='black', ha='center')
ax4.axvline(x=17, color='#8a72a5', linestyle='--', label='保险点')
ax4.text(19, 0.15, f'保险点=80', color='black', ha='center')
ax4.set_xticks(x[::3])
# print(x[::3])
ax4.set_xticklabels([int(i * 100 / 21) for i in x[::3]], rotation=0)
# # 设置 x 轴刻度，从 0 到 100，每隔 20 显示一个刻度
# ax4.set_xticks(real_x[::20])
# # 设置 x 轴标签，每隔 20 显示一个标签
# ax4.set_xticklabels(real_x[::20], rotation=0)

ax4.fill_between(x_fit, y_fit_,
                 where=((x_fit >= mu_gamma + 0.5) & (x_fit <= 17)), color='gray', alpha=0.5,
                 label="还款区间")
# be9574
ax4.fill_between(x_fit, y_fit_,
                 where=((x_fit >= 0) & (x_fit <= mu_gamma + 0.5)), color='#ffeace', alpha=0.5,
                 label="小于预期寿命")
ax4.fill_between(x_fit, y_fit_,
                 where=((x_fit >= 17) & (x_fit <= 22)), color='#5ea7c2', alpha=0.5,
                 label="赤字区间")

ax4.legend()
f4.suptitle('寿命分布的均值与保险点设置', fontsize=16)
plt.show()
