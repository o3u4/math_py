import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# 定义动力学方程
def dynamics(t, y, r, K, a, b, c):
    N, R = y
    dNdt = r * N * (1 - N / K) - a * N * R
    dRdt = b * N - c * R
    return [dNdt, dRdt]


# 定义模型参数
r = 0.1  # 种群增长率
K = 100  # 环境容纳量
a = 0.01  # 描述种群数量对性别比例的影响
b = 0.005  # 描述种群数量对性别比例变化的影响
c = 0.01  # 描述性别比例对种群数量的影响

# 初值条件
y0 = [10, 0.1]  # 初始种群数量和性别比例
t_span = (0, 100)  # 时间范围

# 解方程组
sol = solve_ivp(dynamics, t_span, y0, args=(r, K, a, b, c), t_eval=np.linspace(0, 100, 1000))
sol2 = solve_ivp(dynamics, t_span, y0, args=(r, 300, 0.1, b, 0.5), t_eval=np.linspace(0, 100, 1000))

# 绘制结果
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='Population')
plt.plot(sol.t, sol.y[1], label='Sex ratio')
plt.xlabel('Time')
plt.ylabel('Population/Sex ratio')
plt.plot(sol2.t, sol2.y[0], label='Population2')
plt.plot(sol2.t, sol2.y[1], label='Sex ratio2')
plt.legend()
plt.show()


# # 实际数据
# # TODO: 加载实际数据，并定义误差函数
# def error_function(params):
#     # 使用实际数据和模型输出计算误差
#     # 返回误差的平方和
#     # params 是需要优化的参数
#     # 例如：r, K, a, b, c = params
#     # ...
#     # return error
#     pass
#
#
# # 调整参数使模型输出与实际数据匹配
# # 初始参数猜测值
# initial_guess = np.array([r, K, a, b, c])
#
# # 最小化误差函数
# result = minimize(error_function, initial_guess, method='Nelder-Mead')
#
# # 获取最优参数
# optimal_params = result.x
# print("Optimal parameters:", optimal_params)
