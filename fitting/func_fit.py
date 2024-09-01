from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import kstest
from scipy.stats import probplot
from draw.draw import plot_line, scatter_plot, plot_horizontal_line


def cweibull(x, c, k, a):
    return c * k / a * (x / a) ** (k - 1) * np.exp(-(x / a) ** k)


class Fit:
    plt.style.use('seaborn-v0_8')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    def __init__(self, function):
        self.function = function

    def fit_scatter(self, x, y, init_guess):
        """
        拟合散点
        :param init_guess: 初始猜测参数 (列表)
        :param x: x (numpy数组)
        :param y: y (numpy数组)
        :return:
        param: 返回迭代后最优拟合参数, 初始值不好可能非最优
        """
        params, covariance = curve_fit(self.function, x, y, p0=init_guess)
        return params

    def plot_fitting(self, x, y, params, ax=None,
                     point_color='#5433AB', fit_color='#509caf',
                     no_fill_point=True, point_label=None,
                     fit_label=None, shape="o", point_size=15,
                     line_width=1, smooth=True):
        """ 颜色: #5433AB, #509caf, #C35540, #7db3c6, #8a72a5, #ffeace, #5ea7c2
        画出散点和拟合图
        :param ax: 目标 Axes 对象, 可在目标子图内作图
        :param x:
        :param y:
        :param params: 参数
        :param point_color: 散点颜色
        :param fit_color: 拟合颜色
        :param no_fill_point: 不填充点
        :param point_label: 散点标签
        :param fit_label: 拟合标签
        :param shape: 散点形状
        :param point_size: 点大小
        :param line_width: 点轮廓粗细
        :param smooth: 拟合图是否平滑
        :return:
        fig, ax:
        fig.suptitle('这是整个图形的标题', fontsize=16)
        ax 用法：
            ax.set_xlabel('年龄')  # 设置x轴标签
            ax.set_ylabel('概率密度')  # 设置y轴标签
            ax.set_title('概率密度函数图')  # 设置子图标题
        每隔3个标签显示一个，rotation=0表示标签不旋转
            ax.set_xticks(x[::3])  # 每隔3个年龄段设置一个x轴刻度
            ax.set_xticklabels(age_labels[::3], rotation=0)  # 设置x轴刻度标签并不旋转
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
        else:
            fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象

        face = "none"
        if not no_fill_point:
            face = None

        ax.scatter(x, y, color=point_color, facecolors=face, label=point_label,
                   marker=shape, s=point_size, linewidths=line_width)

        if smooth:
            if len(x) < 100:
                x_ = np.linspace(np.min(x), np.max(x), 100)
                ax.plot(x_, self.function(x_, *params), label=fit_label, color=fit_color)
        else:
            ax.plot(x, self.function(x, *params), label=fit_label, color=fit_color)

        ax.legend()  # 显示图例（如果有）
        # 调整布局
        plt.tight_layout()
        # plt.show()
        return fig, ax  # 返回 Figure 和 Axes 对象

    @staticmethod
    def k_s_test(cdf_func, y, params):
        """
        k-s检验查看拟合显著性
        :param cdf_func: 分布函数, 概率密度函数的积分
        :param y: 随机变量观察列
        :param params:
        :return:
        """
        ks_statistic, p_value = kstest(y, lambda x: cdf_func(x, *params))
        return ks_statistic, p_value

    def residual_plot(self, x, y, params, ax=None,
                      color='#5433AB', no_fill_point=True,
                      point_label=None, shape="o",
                      point_size=15, line_width=1):
        """
        画出残差图
        :param x: x
        :param y: y
        :param params: 拟合函数参数
        :param ax: 子图
        :param color: 颜色
        :param no_fill_point: 不填充点
        :param point_label: 点的标签
        :param shape: 点的形状
        :param point_size: 点的大小
        :param line_width: y=0这条线的粗细
        :return:
        residuals: 残差
        [fig, ax]: [画布, 子图]
        """
        y_fit = self.function(x, *params)
        residuals = y - y_fit
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 6))  # 如果没有传入 ax, 则创建新的
        else:
            fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象

        fig, ax = scatter_plot(x, residuals, ax=ax, point_color=color,
                               no_fill_point=no_fill_point,
                               point_label=point_label, shape=shape,
                               point_size=point_size, line_width=line_width)
        fig, ax = plot_horizontal_line(0, ax=ax, linewidth=1)
        return residuals, [fig, ax]

    @staticmethod
    def qq_plot(residuals, ax=None, no_fill_point=True,
                point_color='#5433AB', point_label=None, shape="o",
                point_size=15, point_line_width=1, line_color='#509caf',
                line_label='参考线', linestyle='--'):
        """
        画出拟合的qq图
        'osm: order statistic medians'
        'osr: ordered responses'
        :param residuals: 残差
        :param ax: 子图
        :param no_fill_point: 不填充点
        :param point_color: 点颜色
        :param point_label: 点标签
        :param shape: 点形状
        :param point_size: 点大小
        :param point_line_width: 点轮廓粗细
        :param line_color: 参考线颜色
        :param line_label: 参考线标签
        :param linestyle: 参考线样式
        :return:
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 6))  # 如果没有传入 ax, 则创建新的
        else:
            fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象

        osm, osr = probplot(residuals, dist="norm")
        fig, ax = scatter_plot(osm[0], osm[1], ax=ax, point_color=point_color,
                               no_fill_point=no_fill_point, point_label=point_label,
                               shape=shape, point_size=point_size, line_width=point_line_width)
        slope, intercept = np.polyfit(osm[0], osm[1], 1)
        fig, ax = plot_line(osm[0], slope * osm[0] + intercept, ax=ax, line_color=line_color,
                            line_label=line_label, linestyle=linestyle)
        return fig, ax


if __name__ == '__main__':
    from load_data.load_excel import ExcelLoader
    import pandas as pd
    from func import weibull_pdf, weibull_cdf

    # path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\data\death.xlsx"
    # el = ExcelLoader(path)
    # data = el.load_excel()
    # df = pd.DataFrame(data)
    # print(df.head())
    # age_labels = df['年龄段']
    # x = np.arange(len(age_labels))  # 将年龄段转化为数字序列
    # y = df['生存率']
    # f = Fit("")
    # fig_, ax_ = f.scatter_plot(x, y, point_label="生存率")
    # f.scatter_plot(x, 1 - y, point_label="1-生存率", ax=ax_)
    # ax_.plot(x, 1 - y, linestyle="-")
    # ax_.set_xticks(x[::3])  # 每隔3个年龄段设置一个x轴刻度
    # ax_.set_xticklabels(age_labels[::3], rotation=0)  # 设置x轴刻度标签并不旋转
    # plt.show()

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

    wb_fit = Fit(cweibull)
    params1_wb = wb_fit.fit_scatter(x, y_male, p0)
    params2_wb = wb_fit.fit_scatter(x, y_female, p0)
    res1, [_, ax] = wb_fit.residual_plot(x, y_male, params1_wb, color='#5433AB',
                                         point_label='男')
    res2, [fig, ax] = wb_fit.residual_plot(x, y_female, params2_wb, ax=ax,
                                           color='#C35540', point_label='女')
    fig.suptitle('Weibull分布拟合残差', fontsize=16)
    ax.set_xlabel('年龄段')  # 设置x轴标签
    ax.set_ylabel('残差')  # 设置y轴标签
    ax.set_xticks(x[::3])  # 每隔3个年龄段设置一个x轴刻度
    ax.set_xticklabels(age_labels[::3], rotation=0)  # 设置x轴刻度标签并不旋转
    ax.legend()

    fig2, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    wb_fit.qq_plot(res1, ax=axs[0], point_color='#5433AB', point_label='男')
    wb_fit.qq_plot(res2, ax=axs[1], point_color='#C35540', point_label='女')
    fig2.suptitle('Weibull分布拟合残差', fontsize=16)
    axs[0].set_title('Weibull拟合残差Q-Q图(男性)')
    axs[1].set_title('Weibull拟合残差Q-Q图(女性)')
    axs[0].set_xlabel('理论分位数')
    axs[0].set_ylabel('实际分位数')
    axs[1].set_xlabel('理论分位数')
    axs[1].set_ylabel('实际分位数')
    axs[0].legend()
    axs[1].legend()

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
