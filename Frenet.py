import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 使用 Seaborn 设置全局主题
sns.set(style="whitegrid")  # 设置背景为白色网格


# 定义螺旋线参数方程
def helix(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t / (2 * np.pi)
    return np.array([x, y, z])


# 计算切向量 T(t)
def tangent(helix, t, dt=1e-5):
    r_t = helix(t)
    r_t_dt = helix(t + dt)
    T = (r_t_dt - r_t) / np.linalg.norm(r_t_dt - r_t)
    return T


# 计算法向量 N(t)
def normal(helix, t, dt=1e-5):
    T_t = tangent(helix, t, dt)
    T_t_dt = tangent(helix, t + dt, dt)
    N = (T_t_dt - T_t) / np.linalg.norm(T_t_dt - T_t)
    return N


# 计算次法向量 B(t)
def binormal(helix, t, dt=1e-5):
    T_t = tangent(helix, t, dt)
    N_t = normal(helix, t, dt)
    B = np.cross(T_t, N_t)
    return B


# 参数范围
t_vals = np.linspace(0, 4 * np.pi, 100)

# 计算曲线点
curve = np.array([helix(t) for t in t_vals])

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d', facecolor='white')  # 设置背景为白色

# 绘制螺旋线
ax.plot(curve[:, 0], curve[:, 1], curve[:, 2], 'b', lw=2, label='Helix Curve')

# 在几个点绘制Frenet标架
for i in range(0, len(t_vals), 10):
    t = t_vals[i]
    r_t = helix(t)

    # 计算Frenet标架
    T_t = tangent(helix, t)
    N_t = normal(helix, t)
    B_t = binormal(helix, t)

    # 绘制切向量T
    ax.quiver(r_t[0], r_t[1], r_t[2], T_t[0], T_t[1], T_t[2], color='r', length=0.4, normalize=True)
    # 绘制法向量N
    ax.quiver(r_t[0], r_t[1], r_t[2], N_t[0], N_t[1], N_t[2], color='g', length=0.4, normalize=True)
    # 绘制次法向量B
    ax.quiver(r_t[0], r_t[1], r_t[2], B_t[0], B_t[1], B_t[2], color='b', length=0.4, normalize=True)

# 设置标题和标签
ax.set_title('Frenet Frame of Helix', fontsize=16)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)

# 美化外观
ax.grid(True)  # 启用网格
ax.xaxis.pane.fill = False  # 关闭 x 轴的背景颜色
ax.yaxis.pane.fill = False  # 关闭 y 轴的背景颜色
ax.zaxis.pane.fill = False  # 关闭 z 轴的背景颜色

# 设置视角
ax.view_init(elev=20, azim=120)  # 设置视角 (elev: 上下, azim: 左右)

# 显示图例
plt.legend()

# 显示图形
plt.show()
