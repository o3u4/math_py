import networkx as nx
import matplotlib.pyplot as plt

# 创建一个无向图
G = nx.Graph()
name = ["Superior", "Michigan and Huron", "St. Clair", "Erie", 'Ontario']
var = 0.1
# 添加边
G.add_edge("Superior", "Michigan", weight=round(1.29 * var, 3))
G.add_edge("Superior", "Huron", weight=round(2.41 * var, 3))
G.add_edge("Superior", "Erie", weight=round(2.28 * var, 3))
G.add_edge("Superior", 'Ontario', weight=round(4.33 * var, 3))
G.add_edge("Michigan", "Huron", weight=round(1.94 * var, 3))
G.add_edge("Michigan", "Erie", weight=round(1.86 * var, 3))
G.add_edge("Michigan", 'Ontario', weight=round(3.68 * var, 3))
G.add_edge("Huron", "Erie", weight=round(0.875 * var, 3))
G.add_edge("Huron", 'Ontario', weight=round(1.734 * var, 3))
G.add_edge("Erie", 'Ontario', weight=round(2.013 * var, 3))

# 求最短路径
shortest_path = nx.shortest_path(G, 'Ontario', "Erie", weight='weight')
shortest_path_length = nx.shortest_path_length(G, 'Ontario', "Erie", weight='weight')

print("最短路径:", shortest_path)
print("最短路径长度:", shortest_path_length)

# 绘制图形
pos = nx.spring_layout(G)  # 定义节点的布局

# 根据边的权重选择不同的颜色
edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
colors = [G[u][v]['weight'] for u, v in edges]
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500,
        font_weight='bold', edge_color=colors, edge_cmap=plt.cm.Blues, width=2)  # 绘制图形

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # 绘制边的权重
plt.show()  # 显示图形
