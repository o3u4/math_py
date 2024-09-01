import numpy as np


def check_conditions(x0):
    """
    检查数据序列是否适合灰色预测。
    :param x0: 原始数据列，numpy array格式。
    :return: 级比和光滑比是否在合适范围内。
    """
    # 计算级比
    lambdas = x0[:-1] / x0[1:]
    lambda_min, lambda_max = 1 / np.exp(2), np.exp(2)

    # 检查级比是否在允许的范围内
    lambda_condition = np.all((lambdas > lambda_min) & (lambdas < lambda_max))

    # 计算光滑比
    dx0 = np.diff(x0)
    smooth_ratio = np.std(dx0) / np.std(x0)

    # 检查光滑比是否在允许的范围内
    # smooth_condition = smooth_ratio <= 0.05

    return lambda_condition, lambdas, smooth_ratio


def grey_model_conditions(x0):
    """
    计算级比和每个点的光滑比，并评估是否适合使用GM(1,1)模型。
    :param x0: 原始数据列，numpy array格式。
    :return: 级比和每个点的光滑比，并返回是否适合使用GM(1,1)模型。
    """
    # 1. 计算一次累加序列 x1(k)
    x1 = np.cumsum(x0)

    # 2. 计算级比
    lambdas = x0[1:] / x0[:-1]  # 调整级比的计算，忽略第一个数据
    lambda_min, lambda_max = 1 / np.exp(2), np.exp(2)

    # 3. 计算每个点的光滑比
    smooth_ratios = x0[1:] / x1[:-1]  # 从第二个数据点开始计算光滑比

    # 4. 级比和光滑比的条件检查
    lambda_condition = np.all((lambdas > lambda_min) & (lambdas < lambda_max))
    # smooth_condition = np.all(smooth_ratios <= 0.5)  # 检查所有光滑比是否小于等于0.5

    return lambda_condition, lambdas, smooth_ratios


def grey_model_1_1(x0):
    """
    实现GM(1,1)模型。
    :param x0: 原始数据列，numpy array格式。
    :return: 返回模型参数a, b和预测函数。
    """
    # 1. 计算一次累加序列 x1(k)
    x1 = np.cumsum(x0)

    # 2. 计算均值生成序列 z1(k)
    z1 = 0.5 * (x1[:-1] + x1[1:])

    # 3. 设置数据矩阵B和数据向量Y
    B = np.vstack([-z1, np.ones(len(z1))]).T
    Y = x0[1:]

    # 4. 使用最小二乘法估计参数
    A = np.linalg.inv(B.T @ B) @ B.T @ Y
    a, b = A[0], A[1]

    # 5. 构建预测函数
    def predict(n):
        k = np.arange(n)
        x1_hat = (x0[0] - b / a) * np.exp(-a * k) + b / a
        x0_predict = np.append(x0[0], np.diff(x1_hat))
        return x0_predict

    return a, b, predict


def calculate_residuals(x0, predict):
    """
    计算并返回残差分析的结果。
    """
    n = len(x0)
    x0_predict = predict(n)
    epsilons = np.abs(x0 - x0_predict) / x0
    return epsilons


if __name__ == '__main__':
    # 示例数据
    data = np.array([225, 214, 205, 196, 189, 181, 177])
    data2 = np.array([140011, 140541, 141008, 141212, 141260, 141175])

    # 检查条件
    lambda_cond, lambdas, smooth_ratio = grey_model_conditions(data2)

    print("级比在合适范围内:", lambda_cond)
    # print("光滑比在合适范围内:", smooth_cond)
    print("级比值:", lambdas)
    print("光滑比值:", smooth_ratio)

    # 使用模型
    a, b, predict1 = grey_model_1_1(data2)

    # 打印参数和预测结果
    print("参数a:", a)
    print("参数b:", b)
    print("预测结果:", predict1(5))  # 预测未来5个数据点

    # 计算残差
    epsilons = calculate_residuals(data2, predict1)

    # 打印残差
    print("每个点的残差ε(k):", epsilons)
    print("最大残差:", np.max(epsilons))

    # 检验是否通过
    if np.max(epsilons) < 0.2:
        print("残差检验通过")
    else:
        print("残差检验未通过")
