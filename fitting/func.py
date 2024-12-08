import numpy as np
from scipy.stats import norm, gamma, chi2, t, f


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


def chi2_pdf(x, df):
    return chi2.pdf(x, df)


def chi2_cdf(x, df):
    return chi2.cdf(x, df)


def t_pdf(x, df):
    return t.pdf(x, df)


def t_cdf(x, df):
    return t.cdf(x, df)


def f_pdf(x, df):
    return f.pdf(x, df)


def f_cdf(x, df):
    return f.cdf(x, df)


def period_envelope_func(t, f1, f2, period=1, init_phase=0):
    """
    生成包络震荡函数
    :param t:
    :param f1: 下包络
    :param f2: 上包络
    :param period: 震荡周期
    :param init_phase: 初相
    :return:
    """
    return (f1(t) + (f2(t) - f1(t)) *
            (1 + np.sin(2 * np.pi * (t + init_phase) / period)) / 2)
