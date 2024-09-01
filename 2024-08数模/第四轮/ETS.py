import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

register_matplotlib_converters()
sns.set_style("darkgrid")

plt.rc("figure", figsize=(16, 12))
plt.rc("font", size=13)

path = r"C:\Users\WIN10\Desktop\数模\第四轮\C\data.csv"
data = pd.read_csv(path)
data['Period'] = pd.to_datetime(data['Time'], format='%Y-%m')
data.set_index("Period", inplace=True)
data = data.dropna()
data = data[~(data == 0).any(axis=1)]
# 按时间升序排序
data.sort_index(ascending=True, inplace=True)
# print("Original Data:\n", data.head())

stl_df = data[['Price']]
# plot_acf(stl_df)
#
# plot_pacf(stl_df.dropna())
# plt.show()

result1 = adfuller(stl_df)
# print(f'ADF Statistic: {result1[0]}')
print("0阶:")
print(f'p-value: {result1[1]}')
print(result1)
#
stl_df_diff = stl_df.diff()     # 一阶差分
stl_df_diff = stl_df_diff.dropna()
# print("一阶差分data:\n", stl_df_diff)
stl_df_diff2 = stl_df_diff.diff()   # 二阶差分
stl_df_diff2 = stl_df_diff2.dropna()
# print("二阶差分data:\n", stl_df_diff2)

print("1阶:")
result2 = adfuller(stl_df_diff)
print(f'p-value: {result2[1]}')
print(result2)

print("2阶:")
result3 = adfuller(stl_df_diff2)
print(f'p-value: {result3[1]}')
print(result3)

# # plt.show()
# 创建模型，Holt-Winters (Additive)
model = ExponentialSmoothing(stl_df_diff2, trend='add', seasonal='add',
                             seasonal_periods=7)

# # 拟合模型
fit = model.fit()
print(fit.summary())

# # print(fit.resid)  # 输出残差，看看是否有异常值
#
# # 预测未来60个周期
# forecast = fit.forecast(steps=60)
#
# forecast_df = pd.DataFrame(forecast, columns=['nonr_forecast'])
#
#
# # 假设原始数据的最后一个索引是原始的时间索引格式
# last_date = pd.to_datetime(stl_df.index[-1])  # 获取原始数据的最后一个日期
#
# # 生成预测期的时间索引，按月增加
# forecast_index = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=60, freq='MS')
#
# # 将生成的时间索引赋值给 forecast_df
# forecast_df.index = forecast_index
#
# # 打印预测数据，确认有正确的时间索引
# print(forecast_df.shape)
# print("预测二阶差分data:\n", forecast_df)
#
# # 画图
# # fig, ax = plt.subplots(figsize=(15, 10))
# #
# # stl_df_diff2.plot.line(ax=ax, y='Price', marker='o', ms=5, lw=2,
# #                        color="#2B4868", fontsize=15, label='real')
# #
# # ax.plot(forecast_df.index, forecast_df['nonr_forecast'], linestyle='--',
# #         marker='x', ms=5, lw=2, color='#7FB3D5', label='Non-Robust Forecast')
# #
# # # 添加 Y 轴标签
# # ax.set_ylabel('Price diff 2', fontsize=15)
# #
# # # 添加图表标题
# # ax.set_title('Price Trend and Forecast', fontsize=18)
# #
# # # 添加网格
# # ax.grid(ls='--')
# #
# # # 添加图例
# # ax.legend(fontsize=12)
#
# # 获取最后一个已知的一阶差分值
# last_diff_value = stl_df_diff.iloc[-1].values[0]
# # print(last_diff_value)
# forecast_l = len(forecast_df)
#
# diff1_series = pd.Series(0.0, index=range(forecast_l))
# # print(diff1_series)
#
# diff1_series[0] = forecast_df.iloc[0, 0] + last_diff_value
#
# for i in range(1, forecast_l):
#     diff1_series[i] = forecast_df.iloc[i, 0] + diff1_series[i - 1]
# print(diff1_series)
# #
# # # 逆二阶差分：从 forecast 预测的二阶差分数据恢复到一阶差分数据
# # forecast_diff = forecast.cumsum() + last_diff_value
# # # print(forecast_diff)
# # # 获取最后一个已知的原始数据值
# # last_value = stl_df.iloc[-1].values[0]
# #
# # # 逆一阶差分：从一阶差分数据恢复到原始数据
# # forecast_original = forecast_diff.cumsum() + last_value
# # print("预测数据\n", forecast_original)
#
# # plt.show()

