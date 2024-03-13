# 傅里叶变换

import numpy as np
import matplotlib.pyplot as plt

# 生成二维示例数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
data = np.sin(X) * np.cos(Y)  # 示例二维数据，这里使用正弦和余弦函数生成二维周期性数据
# print(type(data))
# 使用二维傅里叶变换找出数据的周期
fft_result = np.fft.fft2(data)
fft_result_shifted = np.fft.fftshift(fft_result)  # 将零频率移到频谱中心

# 计算傅里叶变换的频率分量
freqs_x = np.fft.fftfreq(data.shape[0])
freqs_y = np.fft.fftfreq(data.shape[1])

# 将频率转换为周期
periods_x = 1 / freqs_x
periods_y = 1 / freqs_y

# 找出傅里叶变换结果中的最大值的索引
max_idx = np.unravel_index(np.argmax(np.abs(fft_result_shifted), axis=None), fft_result_shifted.shape)

# 输出在两个维度上的周期性
print("X轴的周期为:", periods_x[max_idx[0]])
print("Y轴的周期为:", periods_y[max_idx[1]])

# 绘制原始二维数据
plt.figure(figsize=(10, 6))
plt.imshow(data, cmap='viridis')
plt.title('Original 2D Data')
plt.colorbar()
plt.show()

# 绘制二维傅里叶变换结果
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(fft_result_shifted), cmap='viridis')
plt.title('2D Fourier Transform')
plt.colorbar()
plt.show()

