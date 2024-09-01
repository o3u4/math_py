import numpy as np
import sympy as sp


def gm_21_model(x0):
    """
    实现GM(2,1)模型。
    """
    # 一次累加序列 x1(k)
    x1 = np.cumsum(x0)
    end = len(x0)

    # 一次累减序列 α1x0(k)
    alpha_x0 = np.diff(x0)

    # 构建数据矩阵B和数据向量Y
    B = np.vstack([-x0[1:], np.ones(end - 1)]).T
    Y = alpha_x0

    # 4. 使用最小二乘法估计参数
    A = np.linalg.inv(B.T @ B) @ B.T @ Y
    a, b = A[0], A[1]

    # t = sp.symbols('t', real=True)
    # x_ = sp.Function('x1')(t)
    #
    # # 建立二阶微分方程
    # ode = sp.Eq(x_.diff(t, t) + a * x_.diff(t), b)
    #
    # # 应用初始条件
    # ics = {x_.subs(t, 0): x1[0], x_.subs(t, end - 1): x1[end - 1]}
    # # 求解方程
    # x1_sol = sp.dsolve(ode, ics=ics)
    # print(x1_sol)

    # 预测函数
    # def predict(n):
    #     x1_pre = [round(float(x1_sol.rhs.subs(t, i).evalf()), 3) for i in range(n)]
    #     x0_predict = np.append(x0[0], np.diff(x1_pre))
    #     return x0_predict
    #
    # return a, b, predict

    def predict(n):
        k = np.arange(n)
        x1_hat = ((b / a ** 2 - x0[0] / a) * np.exp(-a*k) + b / a * k +
                  (1 + a) / a * x0[0] - b / a ** 2)

        x0_predict = np.append(x0[0], np.diff(x1_hat))
        return x0_predict

    return a, b, predict


def calculate_residuals(x0, predict):
    """
    计算并返回Verhulst模型的残差分析结果。
    """
    n = len(x0)
    x0_predict = predict(n)
    epsilons = np.abs(x0 - x0_predict) / x0
    return epsilons


# 示例数据
data = np.array([2.874, 3.278, 3.39, 3.679, 3.77, 3.8])

# 使用模型
a, b, predict = gm_21_model(data)

# 计算预测
predicted_values = predict(len(data))

epsilons = calculate_residuals(data, predict)

# 打印预测值和残差
print("预测值:", predicted_values)
print("每个点的残差ε(k):", epsilons)
print("模型参数: a =", a, "b =", b)
