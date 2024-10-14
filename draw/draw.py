from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
