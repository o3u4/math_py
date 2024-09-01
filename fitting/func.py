import numpy as np
from scipy.stats import kstest, norm, gamma

# 一些常用分布  cdf: Cumulative Distribution Function 累积分布函数
# pdf: Probability Density Function 概率密度函数 = 累积分布函数的积分
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


def weibull_pdf(x, a, k):
    return k / a * (x / a) ** (k - 1) * np.exp(-(x / a) ** k)


def weibull_cdf(x, a, k):
    return 1 - np.exp(-(x / a) ** k)
