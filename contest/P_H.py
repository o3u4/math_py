import numpy as np
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')  # 风格


def precipitation(t, a, b, c):
    return a * np.sin(b * t) + c


def fit(x, x1, x2, x3, x4):
    return x1 * np.sin(x2 * x + x3) + x4


def h(p, d, e, f, g):
    return np.exp(d * (p - e)) * f + g


# 创建定义域内的网格点
m = np.linspace(0, 12, 100)
p_list = [(43.14, 0.26, 5.741), (32.28, 0.25, 7.43),
          (20.14, 0.25, 2.47), (38.46, 0.27, 6.78),
          (45.31, 0.26, 5.63)]
h_p_list = [(0.031, 21.57, 1.06, 181.6),
            (0.034, 16.14, 1.03, 173.9),
            (0.028, 13.2, 1.05, 172.9),
            (0.032, 19.23, 1.04, 172.4),
            (0.029, 27.6, 1.03, 73.8)]
fit_list = [(0.1, 0.7, 2.8, 183.18), (0.1, 0.6, 3.1, 175.978),
            (0.2, 0.6, 3.7, 174.7925), (0.2, 0.6, 3.6, 173.99),
            (0.4, 0.7, 3.6, 74.88)]

P_list = [precipitation(m, p[0], p[1], p[2]) for p in p_list]
H_list = [h(P_list[i], h_p_list[i][0], h_p_list[i][1],
            h_p_list[i][2], h_p_list[i][3]) for i in range(5)]
F_list = [fit(m, fit_list[k][0], fit_list[k][1], fit_list[k][2], fit_list[k][3]) for k in range(5)]

name = ["Superior", "Michigan and Huron", "St. Clair", "Erie", 'Ontario']
for j in range(4):
    plt.plot(m, F_list[j], label=f'{name[j]}')
    plt.plot(m, H_list[j], label=f'{name[j]}-precipitation')

plt.xlabel('month')
plt.ylabel('water level')
plt.title('the precipitation influence in water level')
plt.legend()
plt.show()
