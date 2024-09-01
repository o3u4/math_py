import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import probplot
from load_data.load_excel import ExcelLoader
from math import gamma
from scipy.optimize import curve_fit

# 设置风格
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 定义广义Gamma分布函数的PDF和CDF
def generalized_gamma_pdf(x, c, a, d, p):
    return (c * p / (a ** d * gamma(d / p))) * (x ** (d - 1)) * np.exp(-(x / a) ** p)


# 定义Gamma分布函数的PDF和CDF
def gamma_normal_pdf(x, c, a, b):
    return c * b ** a / gamma(a) * (x ** (a - 1)) * np.exp(-b * x)


def weibull(x, c, k, a):
    return c * k / a * (x / a) ** (k - 1) * np.exp(-(x / a) ** k)


p0 = [1475, 1.5, 1.5]
# 提取数据
path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\data/第七轮年龄、男女人口数据.xlsx"
el = ExcelLoader(path)
data = el.load_excel()
df = pd.DataFrame(data)

age_labels = df['年龄段']
x = np.arange(len(age_labels))

y_male = df['男'] / 10 ** 4
y_female = df['女'] / 10 ** 4

# 拟合
params1_gamma, params2_gamma = curve_fit(weibull, x, y_male, p0=p0), curve_fit(weibull, x, y_female, p0=[1475, 4, 11])
# params1_gen_gamma, params2_gen_gamma = curve_fit(generalized_gamma_pdf, x, y_male, p0=[17542638.0, 5, 2, 3]), curve_fit(generalized_gamma_pdf, x, y_female, p0=[286300206, 12.9, 2, 3])

# 计算拟合值
y_male_fit_gamma = weibull(x, *params1_gamma[0])
y_female_fit_gamma = weibull(x, *params2_gamma[0])
# y_male_fit_gen_gamma = generalized_gamma_pdf(x, *params1_gen_gamma[0])
# y_female_fit_gen_gamma = generalized_gamma_pdf(x, *params2_gen_gamma[0])

# 残差计算
residuals_male_gamma = y_male - y_male_fit_gamma
residuals_female_gamma = y_female - y_female_fit_gamma
# residuals_male_gen_gamma = y_male - y_male_fit_gen_gamma
# residuals_female_gen_gamma = y_female - y_female_fit_gen_gamma

# 绘制残差图
plt.figure(figsize=(8, 6))

plt.scatter(x, residuals_male_gamma, color='#5433AB',
            facecolors='none', label='男', marker='o', s=15, linewidths=1)
plt.scatter(x, residuals_female_gamma, color='#C35540',
            facecolors='none', label='女', marker='o', s=15, linewidths=1)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.xticks(x[::3], age_labels[::3], rotation=0)  # 每隔一个标签显示一次  # 设置x轴为年龄段标签
plt.title('Weibull分布拟合残差')
plt.xlabel('年龄段')
plt.ylabel('残差')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
#
# 创建一个新的图形和轴
# 绘制QQ图
plt.figure(figsize=(12, 6))

# 男性Gamma分布 QQ图
plt.subplot(1, 2, 1)

# 使用 probplot 生成 QQ 图的数据
osm_male, osr_male = probplot(residuals_male_gamma, dist="norm")


# 绘制 QQ 图
plt.scatter(osm_male[0], osm_male[1],
            color='#5433AB', facecolors='none', label='男',
            marker='o', s=15, linewidths=1)

# 添加 QQ 图的参考线
slope, intercept = np.polyfit(osm_male[0], osm_male[1], 1)
plt.plot(osm_male[0], slope * osm_male[0] + intercept,
         color='#509caf', linestyle='--', label='参考线')

# 设置图的标题和标签
plt.title('Weibull拟合残差Q-Q图(男性)')
plt.xlabel('理论分位数')
plt.ylabel('实际分位数')
plt.legend()
# 调整网格样式
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
osm_female, osr_female = probplot(residuals_female_gamma, dist="norm")
# 绘制 QQ 图
plt.scatter(osm_female[0], osm_female[1],
            color='#C35540', facecolors='none', label='女',
            marker='o', s=15, linewidths=1)
# 添加 QQ 图的参考线
slope, intercept = np.polyfit(osm_female[0], osm_female[1], 1)
plt.plot(osm_female[0], slope * osm_female[0] + intercept,
         color='#8a72a5', linestyle='--', label='参考线')
# 设置图的标题和标签
plt.title('Weibull拟合残差Q-Q图(女性)')
plt.xlabel('理论分位数')
plt.ylabel('实际分位数')
# 添加图例
plt.legend()

# 调整网格样式
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
# 显示图形
plt.show()
