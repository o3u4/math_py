import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建一个Basemap对象
map = Basemap(projection='merc', llcrnrlat=40, urcrnrlat=50, llcrnrlon=-100, urcrnrlon=-70, resolution='l')

# 绘制海岸线
map.drawcoastlines()
map.drawrivers()
map.fillcontinents()

# # 定义湖泊和河流的坐标
# lake_coords = {
#     'Superior': (-87.0, 47.7),
#     'Michigan': (-86.7, 45.8),
#     'Huron': (-82.4, 44.8),
#     'Erie': (-81.0, 42.2),
#     'Ontario': (-77.5, 43.5)
# }
#
# river_coords = {
#     'St. Marys': [(-84.4, 46.5), (-83.9, 46.5)],
#     'St. Clair': [(-82.7, 42.6), (-82.5, 42.6)],
#     'Detroit': [(-83.1, 42.3), (-83.0, 42.3)],
#     'Niagara': [(-79.1, 43.3), (-79.0, 43.3)],
#     'St. Lawrence': [(-74.1, 45.0), (-73.5, 45.5)],
#     'Ottawa': [(-75.6, 45.4), (-74.8, 45.4)]
# }
#
# # 绘制湖泊和河流
# for lake, coords in lake_coords.items():
#     x, y = map(coords[0], coords[1])
#     map.plot(x, y, marker='o', markersize=5, label=lake)
#
# for river, coords in river_coords.items():
#     x, y = map([coord[0] for coord in coords], [coord[1] for coord in coords])
#     map.plot(x, y, label=river)
#
# # 添加标题和图例
plt.title('North American Great Lakes and Rivers')
# plt.legend()
# 显示地图
plt.show()
