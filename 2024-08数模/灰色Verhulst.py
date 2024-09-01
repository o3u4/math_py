import numpy as np


def grey_verhulst_model(x0):
    """
    实现灰色Verhulst模型，返回模型参数a, b和预测函数。
    :param x0: 原始数据列，numpy array格式。
    :return: 返回模型参数a, b和预测函数。
    """
    # 1. 计算一次累加序列 x1(k)
    x1 = np.cumsum(x0)

    # 2. 计算均值生成序列 z1(k)
    z1 = 0.5 * (x1[:-1] + x1[1:])

    # 3. 设置数据矩阵B和数据向量Y
    B = np.vstack([-z1, z1 ** 2]).T
    Y = x0[1:]

    # 4. 使用最小二乘法估计参数
    A = np.linalg.inv(B.T @ B) @ B.T @ Y
    a, b = A[0], A[1]

    # 5. 构建预测函数
    def predict(n):
        """
        使用模型参数预测未来n个数据点的x^0。
        """
        k = np.arange(n)
        x1_hat = a * x0[0] / (b * x0[0] + (a - b * x0[0]) * np.exp(a * k))
        x0_predict = np.append(x0[0], np.diff(x1_hat))
        return x0_predict

    return a, b, predict


def calculate_verhulst_residuals(x0, predict):
    """
    计算并返回Verhulst模型的残差分析结果。
    """
    n = len(x0)
    x0_predict = predict(n)
    epsilons = np.abs(x0 - x0_predict) / x0
    return epsilons


if __name__ == '__main__':

    # 示例数据
    data = np.array([4.93, 2.33, 3.87, 4.35, 6.63, 7.15, 5.37, 6.39,
                     7.81, 8.35])
    # 使用灰色Verhulst模型
    a, b, verhulst_predict = grey_verhulst_model(data)

    # 打印模型参数
    print("参数a:", a)
    print("参数b:", b)

    # 计算残差
    verhulst_epsilons = calculate_verhulst_residuals(data, verhulst_predict)

    # 打印残差
    print("每个点的残差ε(k):", verhulst_epsilons)
    print("最大残差:", np.max(verhulst_epsilons))

    print("预测结果:", verhulst_predict(5))  # 预测未来5个数据点
    # 检验是否通过
    if np.max(verhulst_epsilons) < 0.2:
        print("残差检验通过")
    else:
        print("残差检验未通过")
