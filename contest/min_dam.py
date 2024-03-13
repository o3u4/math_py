import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('Solarize_Light2')  # 风格

H_idea = [183.09, 175.56, 174.8, 173.64, 75.1]
h_fact = [183.145, 175.927, 174.608, 173.816, 74.4316]
f_0 = [1, 1.29, 2.41, 2.28, 4.144]
f_1 = [4.144, 3.674, 1.734, 2.013, 1]


# 定义三维函数
def f(x, y):
    errors = []
    for i in range(5):
        e = np.abs(h_fact[i] - H_idea[i] - f_0[i] * x - f_1[i] * y)
        errors.append(e)
    error = errors[0]
    for j in range(1, 5):
        error += errors[j]
    return error


# 创建定义域内的网格点
x1 = np.linspace(-1, 1, 100)
x2 = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x1, x2)
Z = f(X, Y)
# print(type(Z))

# 画出三维函数的图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('error function ')
ax.set_title('sensitivity analysis')

# 使用optimize.minimize函数求解极小值
result = optimize.minimize(lambda x: f(x[0], x[1]), np.array([0, 0]))

# 输出极小值的坐标和函数值
print('极小值坐标：', result.x)
print('极小值函数值：', result.fun)
Axes3D.text(ax, -1, 0, 20,
            f'Minimum coordinates: {result.x}\nminimum value: {result.fun}',
            color='#8EBF87')

plt.show()

