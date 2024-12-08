from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False


# 字体设置:
# 宋体 (SimSun)
# 黑体 (SimHei)
# 微软雅黑 (Microsoft YaHei)
# 楷体 (KaiTi)
# 仿宋 (FangSong)
# 隶书 (LiSu)
# 华文细黑 (STXihei)
# 华文楷体 (STKaiti)
# 华文宋体 (STSong)

def plot_line(x, y, ax=None, line_color='#509caf',
              line_label=None, linewidth=2, linestyle='-'):
    """
    画折线图, 点够多就是平滑图
    :param x: x
    :param y: y
    :param ax: 子图
    :param line_color: 线的颜色
    :param line_label: 线的标签
    :param linewidth: 线的粗细, 默认为2
    :param linestyle: 线的类型
    :return:
    fig, ax: 画布, 子图
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象

    ax.plot(x, y, color=line_color, label=line_label, linewidth=linewidth,
            linestyle=linestyle)
    return fig, ax


def plot_vertical_line(x, ax=None, color='#7db3c6', label=None,
                       linestyle='--', linewidth=2):
    """
    画垂直于x轴的线
    :param linewidth: 线的粗细, 默认为2
    :param x: 垂线x坐标
    :param ax: 子图
    :param color: 颜色
    :param label: 标签
    :param linestyle:线的样式
    :return:
    fig, ax: 画布, 子图
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象
    ax.axvline(x=x, color=color, linestyle=linestyle, label=label, linewidth=linewidth)
    return fig, ax


def plot_horizontal_line(y, ax=None, color='#7db3c6', label=None,
                         linestyle='--', linewidth=2):
    """
    画平行于x轴的线
    :param y: 坐标
    :param ax: 子图
    :param color: 颜色
    :param label: 标签
    :param linestyle: 样式
    :param linewidth: 粗细
    :return:
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象
    ax.axhline(y=y, color=color, linestyle=linestyle, label=label, linewidth=linewidth)
    return fig, ax


def plot_bar(x, y, ax=None, color="#7db3c6", label=None, width=0.8):
    """
    绘制柱状图
    :param x: x
    :param y: y
    :param ax: 子图
    :param color: 柱子颜色
    :param label: 标签
    :param width: 每个柱子的宽度, 默认0.8, 柱子占据横坐标间距的80%
    :return:
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象
    ax.bar(x, y, color=color, label=label, width=width)
    return fig, ax


def fill_area(x, y, where, ax=None, color='#5ea7c2', alpha=0.5, label=None):
    """
    填充区间
    :param x: x
    :param y: y
    :param where: 关于x, y的逻辑表达式, 表示填充区域, 如 (x >= 0) & (x <= 1)
    :param ax:子图
    :param color: 填充颜色
    :param alpha: 透明度
    :param label: 标签
    :return:
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象
    ax.fill_between(x, y,
                    where=where, color=color, alpha=alpha,
                    label=label)
    return fig, ax


def scatter_plot(x, y, ax=None,
                 point_color='#5433AB', no_fill_point=True, point_label=None,
                 shape="o", point_size=15, line_width=1):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象

    face = "none"
    if not no_fill_point:
        face = None

    ax.scatter(x, y, color=point_color, facecolors=face, label=point_label,
               marker=shape, s=point_size, linewidths=line_width)

    ax.legend()  # 显示图例（如果有）
    # 调整布局
    plt.tight_layout()
    # plt.show()
    return fig, ax  # 返回 Figure 和 Axes 对象


def add_text(x, y, ax=None, text="text", color='black', ha='center',
             va='center', fontsize=12, fontweight='bold', rotation=0):
    """
    指定位置添加文字
    :param x: x
    :param y: y
    :param ax: 子图
    :param text: 文本
    :param color: 颜色
    :param ha: 文本的水平对齐方式, 'center'：文本的中心与 (x, y) 对齐。
                                'left'：文本的左边缘与 (x, y) 对齐。
                                'right'：文本的右边缘与 (x, y) 对齐
    :param va: 文本的垂直对齐方式, 'top', 'center', 'bottom'
    :param fontsize: 字体大小, 默认12
    :param fontweight: 字体粗细, 'normal', 'bold'
    :param rotation: 文本旋转角度
    :return:
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))  # 如果没有传入 ax, 则创建新的
    else:
        fig = ax.figure  # 如果传入了 ax, 使用已有的 Figure 对象
    ax.text(x, y, text, color=color, ha=ha, va=va, fontsize=fontsize,
            fontweight=fontweight, rotation=rotation)
    return fig, ax


def axes_smaller(ax, loc, map_loc1, map_loc2, line_color='grey',
                 line_width=1.5, linestyle="--"):
    """
    局部放大图
    :param ax: 原始 ax
    :param loc: 小图所在位置及大小
    (0.1, 0.1, 0.2, 0.2) 表示在大图比例(0.1, 0.1)的地方为左下角, 长高分别为大图的(0.2, 0.2)
    :param map_loc1: 小图与大图连接线的第一个方位点
    :param map_loc2: 小图与大图连接线的第二个方位点
    # 1 (右上) 2 (左上) 3(左下) 4(右下) 大图小图对应点分别对应相连
    :param line_color: 连接线颜色
    :param line_width: 连接线宽度
    :param linestyle: 连接线样式
    :return: 小图的ax
    """
    ax_in = ax.inset_axes(loc)
    # 连接大小图
    mark_inset(ax, ax_in, loc1=map_loc1, loc2=map_loc2,
               fc="none", ec=line_color, lw=line_width, linestyle=linestyle)
    return ax_in


def period_envelope_func_by_data(t, data1, data2, poly_order1, poly_order2,
                                 period=1, init_phase=0, ax=None):
    """
    根据数据点画出震荡周期函数
    :param t:
    :param data1: 下包络数据
    :param data2: 上包络数据
    :param poly_order1: 下数据多项式拟合次数
    :param poly_order2: 上数据多项式拟合次数
    :param period: 震荡周期
    :param init_phase: 初相位
    :param ax:
    :return:
    """
    from fitting.LSM import LSM
    import numpy as np
    from fitting.func import period_envelope_func
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    else:
        fig = ax.figure
    data1 = np.array(data1)
    data2 = np.array(data2)
    lsm1 = LSM(t, data1)
    lsm2 = LSM(t, data2)
    polys1 = LSM.polynomial(poly_order1)
    polys2 = LSM.polynomial(poly_order1)
    a1 = lsm1.lsm(polys1)[0]
    a2 = lsm2.lsm(polys2)[0]

    def f1(t):
        s = 0
        for i in range(poly_order1 + 1):
            s += a1[i] * polys1[i](t)
        return s

    def f2(t):
        s = 0
        for i in range(poly_order2 + 1):
            s += a2[i] * polys2[i](t)
        return s

    x = np.linspace(t[0], t[-1], 200)
    y = period_envelope_func(x, f1, f2, period, init_phase)
    plot_line(x, y, ax=ax)
    return fig, ax
