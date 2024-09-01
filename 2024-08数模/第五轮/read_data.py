import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from load_data.load_excel import ExcelLoader

plt.style.use('seaborn-v0_8')    # 风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

path = r"C:\Users\WIN10\Desktop\数模\第五轮\C题\第七轮死亡人口.xlsx"
csv = r'C:\Users\WIN10\Desktop\数模\第五轮\C题/data/第七轮死亡人口.csv'
el = ExcelLoader(path)
data = el.load_excel()
el.trans_to_csv(data, csv)
print(data.head())

df = pd.DataFrame(data)

# 提取数据
age_labels = df['年龄段']
x = np.arange(len(age_labels))  # 将年龄段转化为数字序列
print(x)
y_male = df['男']
y_female = df['女']

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y_male, color='blue', label='男', marker='o')
plt.scatter(x, y_female, color='red', label='女', marker='x')

# 曲线拟合
z_male = np.polyfit(x, y_male, 6)  # 二次多项式拟合
p_male = np.poly1d(z_male)
plt.plot(x, p_male(x), "b--", label='男 (6阶多项式拟合)')

z_female = np.polyfit(x, y_female, 6)
p_female = np.poly1d(z_female)
plt.plot(x, p_female(x), "r--", label='女 (6阶多项式拟合)')

# 设置图例和标签
plt.xticks(x[::3], age_labels[::3], rotation=0)  # 每隔一个标签显示一次  # 设置x轴为年龄段标签
plt.xlabel('年龄段')
plt.ylabel('死亡人口数')
plt.title('不同年龄段的男女人口数')
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
