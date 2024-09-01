import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from draw import draw


class GM:
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    def __init__(self, data):
        self.data = data

    def gm11_conditions(self):
        """
        计算级比和每个点的光滑比，并评估是否适合使用GM(1,1)模型。
        :return: 级比和每个点的光滑比，并返回是否适合使用GM(1,1)模型。
        lambda_condition: 级比是否满足
        lambdas: 级比
        smooth_ratios: 每个点的光滑比
        """
        # 1. 计算一次累加序列 x1(k)
        x1 = np.cumsum(self.data)

        # 2. 计算级比
        lambdas = self.data[1:] / self.data[:-1]  # 调整级比的计算，忽略第一个数据
        lambda_min, lambda_max = 1 / np.exp(2), np.exp(2)

        # 3. 计算每个点的光滑比
        smooth_ratios = self.data[1:] / x1[:-1]  # 从第二个数据点开始计算光滑比

        # 4. 级比和光滑比的条件检查
        lambda_condition = np.all((lambdas > lambda_min) & (lambdas < lambda_max))

        return lambda_condition, lambdas, smooth_ratios

    def gm11(self):
        """
        实现GM(1,1)模型。
        :return: 返回模型参数a, b和预测函数。
        """
        # 1. 计算一次累加序列 x1(k)
        x1 = np.cumsum(self.data)

        # 2. 计算均值生成序列 z1(k)
        z1 = 0.5 * (x1[:-1] + x1[1:])

        # 3. 设置数据矩阵B和数据向量Y
        B = np.vstack([-z1, np.ones(len(z1))]).T
        Y = self.data[1:]

        # 4. 使用最小二乘法估计参数
        A = np.linalg.inv(B.T @ B) @ B.T @ Y
        a, b = A[0], A[1]

        # 5. 构建预测函数
        def predict(n):
            k = np.arange(n)
            x1_hat = (self.data[0] - b / a) * np.exp(-a * k) + b / a
            x0_predict = np.append(self.data[0], np.diff(x1_hat))
            return x0_predict

        return a, b, predict

    def gm_verhulst(self):
        """
        实现灰色Verhulst模型，返回模型参数a, b和预测函数。
        :return: 返回模型参数a, b和预测函数。
        """
        # 1. 计算一次累加序列 x1(k)
        x1 = np.cumsum(self.data)

        # 2. 计算均值生成序列 z1(k)
        z1 = 0.5 * (x1[:-1] + x1[1:])

        # 3. 设置数据矩阵B和数据向量Y
        B = np.vstack([-z1, z1 ** 2]).T
        Y = self.data[1:]

        # 4. 使用最小二乘法估计参数
        A = np.linalg.inv(B.T @ B) @ B.T @ Y
        a, b = A[0], A[1]

        # 5. 构建预测函数
        def predict(n):
            """
            使用模型参数预测未来n个数据点的x^0。
            """
            k = np.arange(n)
            x1_hat = a * self.data[0] / (b * self.data[0] + (a - b * self.data[0]) * np.exp(a * k))
            x0_predict = np.append(self.data[0], np.diff(x1_hat))
            return x0_predict

        return a, b, predict

    def gm21(self):
        """
        实现GM(2,1)模型。
        return
        a1, a2, b: 参数
        predict: 预测函数
        """
        # 一次累加序列 x1(k)
        x1 = np.cumsum(self.data)
        end = len(self.data)

        # 一次累减序列 α1x0(k)
        alpha_x0 = np.diff(self.data)

        # 均值生成序列 z1(k)，用于建模
        z1 = 0.5 * (x1[:-1] + x1[1:])

        # 构建数据矩阵B和数据向量Y
        B = np.vstack([-self.data[1:], -z1, np.ones(len(z1))]).T
        Y = alpha_x0

        # 4. 使用最小二乘法估计参数
        A = np.linalg.inv(B.T @ B) @ B.T @ Y
        a1, a2, b = A[0], A[1], A[2]

        t = sp.symbols('t', real=True)
        x_ = sp.Function('x1')(t)

        # 建立二阶微分方程
        ode = sp.Eq(x_.diff(t, t) + a1 * x_.diff(t) + a2 * x_, b)

        # 应用初始条件
        ics = {x_.subs(t, 0): x1[0], x_.subs(t, end - 1): x1[end - 1]}
        # 求解方程
        x1_sol = sp.dsolve(ode, ics=ics)
        latex_solution = sp.latex(x1_sol)
        print("解得方程为:", x1_sol)
        print("latex为:", latex_solution)

        # 预测函数
        def predict(n):
            x1_pre = [x1_sol.rhs.subs(t, i).evalf() for i in range(n)]
            x0_predict = np.append(self.data[0], np.diff(x1_pre))
            return x0_predict

        return a1, a2, b, predict

    def dgm21(self):
        """
        实现DGM(2,1)模型。
        """
        # 一次累加序列 x1(k)
        end = len(self.data)

        # 一次累减序列 α1x0(k)
        alpha_x0 = np.diff(self.data)

        # 构建数据矩阵B和数据向量Y
        B = np.vstack([-self.data[1:], np.ones(end - 1)]).T
        Y = alpha_x0

        # 4. 使用最小二乘法估计参数
        A = np.linalg.inv(B.T @ B) @ B.T @ Y
        a, b = A[0], A[1]

        def predict(n):
            k = np.arange(n)
            x1_hat = ((b / a ** 2 - self.data[0] / a) * np.exp(-a * k) + b / a * k +
                      (1 + a) / a * self.data[0] - b / a ** 2)

            x0_predict = np.append(self.data[0], np.diff(x1_hat))
            return x0_predict

        return a, b, predict

    def calculate_residuals(self, predict):
        """
        计算并返回残差分析的结果。
        """
        n = len(self.data)
        x0_predict = predict(n)
        epsilons = np.abs(self.data - x0_predict) / self.data
        return epsilons

    def gm11_summary(self):
        print("-------------------------GM_11模型-------------------------")
        print(f"共有{len(self.data)}个数据")
        a, b, gm11_predict = self.gm11()
        print("--------------------------事前检验--------------------------")
        lmd_cond, lmd, smt = self.gm11_conditions()
        print("每个点的级比值:", lmd)
        print("级比在合适范围内:", lmd_cond)
        print("每个点的光滑比值:", smt)
        print("光滑比递减，且小于0.5为好，若突然增加则考虑别的模型")
        print("--------------------------构建模型--------------------------")
        print("原始数据为:", self.data.tolist())
        print("预测数据为:", gm11_predict(len(self.data)))
        print(f"模型参数为: a: {a}, b: {b}")

        c1 = round(float((self.data[0] - b / a)), 3)
        c2 = round(float(-a), 3)
        c3 = round(float(b / a), 3)
        latex = "x^{(1)}(k+1)=" + str(c1) + "e^{" + str(c2) + "k}" + str(c3)
        print("方程为:", latex)

        print("--------------------------事后检验--------------------------")
        res = self.calculate_residuals(gm11_predict)
        print("残差比为:", res)
        print("残差比最大值小于0.2为好")

    def gmv_summary(self):
        print("-------------------------GM_V模型--------------------------")
        print(f"共有{len(self.data)}个数据")
        a, b, gmv_predict = self.gm_verhulst()
        print("--------------------------构建模型--------------------------")
        print("原始数据为:", self.data.tolist())
        print("预测数据为:", gmv_predict(len(self.data)))
        print(f"模型参数为: a: {a}, b: {b}")

        c1 = round(float((a * self.data[0])), 3)
        c2 = round(float((b * self.data[0])), 3)
        c3 = round(float((a - b * self.data[0])), 3)
        c4 = round(float(a), 3)
        latex = ("x^{(1)}(k+1)=\\frac{" + str(c1) + "}{" +
                 str(c2) + "+(" + str(c3) + ")" + "e^{" + str(c4) + "k}}")
        print("方程为:", latex)

        print("--------------------------事后检验--------------------------")
        res = self.calculate_residuals(gmv_predict)
        print("残差比为:", res)
        print("残差比最大值小于0.2为好")

    def gm21_summary(self):
        print("-------------------------GM_21模型-------------------------")
        print(f"共有{len(self.data)}个数据")
        print("--------------------------构建模型--------------------------")
        print("原始数据为:", self.data.tolist())
        a1, a2, b, gm21_predict = self.gm21()
        print("预测数据为:", gm21_predict(len(self.data)))
        print(f"模型参数为: a: {a1}, a2: {a2}, b: {b}")
        print("--------------------------事后检验--------------------------")
        res = self.calculate_residuals(gm21_predict)
        print("残差比为:", res)
        print("残差比最大值小于0.2为好")

    def dgm21_summary(self):
        print("------------------------DGM_21模型-------------------------")
        print(f"共有{len(self.data)}个数据")
        print("--------------------------构建模型--------------------------")
        print("原始数据为:", self.data.tolist())
        a, b, dgm21_predict = self.dgm21()
        print("预测数据为:", dgm21_predict(len(self.data)))
        print(f"模型参数为: a: {a}, b: {b}")

        c1 = round(float(b / a - self.data[0] / a), 3)
        c2 = round(float(-a), 3)
        c3 = round(float(b / a), 3)
        c4 = round(float((1 + a) / a * self.data[0] - b / a ** 2), 3)
        latex = ("x^{(1)}(k+1)=" + str(c1) +
                 "e^{" + str(c2) + "k}" +
                 "+(" + str(c3) + ")k" + "+(" + str(c4) + ")")
        print("方程为:", latex)

        print("--------------------------事后检验--------------------------")
        res = self.calculate_residuals(dgm21_predict)
        print("残差比为:", res)
        print("残差比最大值小于0.2为好")

    def plot_fit(self, fitted_point):
        x1 = np.arange(len(self.data))
        x2 = np.arange(len(fitted_point))
        fig, ax = plt.subplots(figsize=(10, 6))
        draw.scatter_plot(x1, self.data, ax=ax)
        draw.plot_line(x1, self.data, line_label="origin line", ax=ax, line_color='#6E8FB2')
        draw.scatter_plot(x2, fitted_point, ax=ax)
        draw.plot_line(x2, fitted_point, line_label="fitted line", ax=ax, line_color="#C16E71")
        ax.set_xlabel("t")
        ax.set_ylabel("data")
        ax.legend(loc=(0.7, 0.5), fontsize=15)
        fig.suptitle('fit line', fontsize=20)


if __name__ == '__main__':
    data1 = np.array([140011, 140541, 141008, 141212, 141260, 141175])
    data2 = np.array([4.93, 2.33, 3.87, 4.35, 6.63, 7.15, 5.37, 6.39,
                      7.81, 8.35])
    data3 = np.array([41, 49, 61, 78, 96, 104])
    data4 = np.array([2.874, 3.278, 3.39, 3.679, 3.77, 3.8])

    gm1 = GM(data1)
    gm1.gm11_summary()

    gm2 = GM(data2)
    gm2.gmv_summary()

    gm3 = GM(data3)
    gm3.gm21_summary()

    gm4 = GM(data4)
    gm4.dgm21_summary()
    a, b, dgm21_predict = gm4.dgm21()
    pre_point = dgm21_predict(10)
    gm4.plot_fit(pre_point)
    plt.show()
