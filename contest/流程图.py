import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 字体黑体

# 定义节点和其坐标
nodes = {
    '开始': (1, 5),
    '条件1': (1, 4),
    '条件2': (1, 3),
    '条件3': (1, 2),
    '结束': (1, 1)
}

# 定义节点之间的连接关系
edges = [('开始', '条件1'), ('条件1', '条件2'), ('条件2', '条件3'), ('条件3', '结束')]

# 创建图表
fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 6)

# 绘制节点
for node, (x, y) in nodes.items():
    ax.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.2'))
    ax.plot(x, y, 'o', markersize=20, markerfacecolor='lightblue', markeredgewidth=2, markeredgecolor='black')

# 绘制连接线
for start, end in edges:
    start_x, start_y = nodes[start]
    end_x, end_y = nodes[end]
    ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y), arrowprops=dict(arrowstyle='->', color='black'))


plt.show()
