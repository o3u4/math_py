import plotly.graph_objects as go

# 创建数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建线图
fig = go.Figure(data=go.Scatter(x=x, y=y))

# 设置图表标题和轴标签
fig.update_layout(title='Simple Line Chart', xaxis_title='X Axis', yaxis_title='Y Axis')

# 保存为矢量图（SVG 格式）
# fig.write_image("vector_plot.svg")      # 用到 kaleido包 渲染引擎
fig.show()
