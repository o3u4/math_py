from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import STL
import seaborn as sns
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.forecasting.stl import STLForecast
from statsmodels.graphics.tsaplots import plot_acf

register_matplotlib_converters()
sns.set_style("darkgrid")

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

plt.rc("figure", figsize=(16, 12))
plt.rc("font", size=13)

path = r"data.csv"
data = pd.read_csv(path)
data['Period'] = pd.to_datetime(data['Time'], format='%Y-%m')
data.set_index("Period", inplace=True)
data = data.dropna()
data = data[~(data == 0).any(axis=1)]
# 按时间升序排序
data.sort_index(ascending=True, inplace=True)
print(data.head())

stl_df = data[['Price']]
print(stl_df["Price"].head())

# # 绘制 ACF 图
# fig, ax = plt.subplots(figsize=(10, 6))
# plot_acf(stl_df, lags=100, ax=ax)
# # 设置x轴标签、y轴标签、标题
# ax.set_xlabel('Lags', fontsize=14)
# ax.set_ylabel('Autocorrelation', fontsize=14)
# ax.set_title('ACF of Series', fontsize=16)
# plt.show()
#
# print(stl_df.shape)
# print(stl_df.head())
#
#
# # stl = STL(stl_df, period=7)
# # res = stl.fit()
# # fig = res.plot()
# # plt.show()
# # plt.savefig(r'SAMPLE_STL.pdf')
# #
# # # ====================stl robust fitting======================
# def add_stl_plot(fig, res, legend):
#     """Add 3 plots from a seconde STL fit"""
#     axs = fig.get_axes()
#     comps = ['trend', 'seasonal', 'resid']
#
#     for ax, comp in zip(axs[1:], comps):
#         series = getattr(res, comp)
#         if comp == 'resid':
#             ax.plot(series, marker='o', linestyle='none')
#         else:
#             ax.plot(series)
#             if comp == 'trend':
#                 ax.legend(legend, frameon=False)
#
#
# stl = STL(stl_df, period=7, robust=True)
# res_robust = stl.fit()
# # fig = res_robust.plot()
# # #
# res_non_robust = STL(stl_df, period=7, robust=False).fit()
# # add_stl_plot(fig, res_non_robust, ['Real', "Robust_fit"])
# # plt.show()
# #
# # 数据提取
# stl_df['nonr_trend'] = res_non_robust.trend
# stl_df['nonr_seasonal'] = res_non_robust.seasonal
# stl_df['nonr_resid'] = res_non_robust.resid
# #
# stl_df['r_trend'] = res_robust.trend
# stl_df['r_seasonal'] = res_robust.seasonal
# stl_df['r_resid'] = res_robust.resid
# #
# # # 瞅一眼
# # print(stl_df.shape)
# # print(stl_df.head())
# #
# # # 计算指标
# stl_df['nonr_detrend'] = stl_df['Price'] - stl_df['nonr_trend']
# stl_df['nonr_deseasonal'] = stl_df['Price'] - stl_df['nonr_seasonal']
# #
# stl_df['r_detrend'] = stl_df['Price'] - stl_df['r_trend']
# stl_df['r_deseasonal'] = stl_df['Price'] - stl_df['r_seasonal']
# # #
# nonr_trend_strength = max(0, 1 - stl_df.nonr_resid.var() / stl_df.nonr_deseasonal.var())
# r_trend_strength = max(0, 1 - stl_df.r_resid.var() / stl_df.r_deseasonal.var())
# #
# nonr_seasonal_strength = max(0, 1 - stl_df.nonr_resid.var() / stl_df.nonr_detrend.var())
# r_seasonal_strength = max(0, 1 - stl_df.r_resid.var() / stl_df.r_detrend.var())
# #
# print(f'No Robust的trend_strength={round(nonr_trend_strength, 3)},'
#       f'seasonal_strength={round(nonr_seasonal_strength, 3)}')
# print(f'Robust的trend_strength={round(r_trend_strength, 3)},'
#       f'seasonal_strength={round(r_seasonal_strength, 3)}')
# # #
# # # #
# # # 画图
# fig, ax = plt.subplots(figsize=(10, 8))
# #
# # stl_df.plot.line(ax=ax, y='Price', marker='o', ms=5, lw=2, color="#2B4868", fontsize=15, label='real')
# #
# # stl_df.plot.line(ax=ax, y='nonr_trend', ms=5, lw=4, color='#F8CC5A', fontsize=15, label='No Robust Trend')
# #
# # stl_df.plot.line(ax=ax, y='r_trend', ms=5, lw=4, color='#F2788F', fontsize=15, label="Robust Trend")
# #
# # ax.grid(ls='--')
# # plt.show()
# #
#
# stl_df.index.freq = stl_df.index.inferred_freq
#
# nonr_stlf = STLForecast(stl_df[['Price']], ARIMA, model_kwargs=dict(order=(1, 1, 0), trend='t'), period=7,
#                         robust=False).fit()
# r_stlf = STLForecast(stl_df[['Price']], ARIMA, model_kwargs=dict(order=(1, 1, 0), trend='t'), period=7,
#                      robust=True).fit()
#
# nonr_forecast = nonr_stlf.forecast(60)
# r_forecast = r_stlf.forecast(60)
#
# forecast_df = pd.DataFrame(nonr_forecast, columns=['nonr_forecast'])
# forecast_df['r_forecast'] = r_forecast
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
# print(forecast_df.head())
#
# stl_df.plot.line(ax=ax, y='Price', marker='o', ms=5, lw=2, color="#2B4868", fontsize=15, label='real')
# # stl_df.plot.line(ax=ax, y='nonr_trend', ms=5, lw=4, color='#F8CC5A', fontsize=15, label='No Robust Trend')
# stl_df.plot.line(ax=ax, y='r_trend', ms=5, lw=4, color='#F2788F', fontsize=15, label="Robust Trend")
#
# # # 绘制预测的非鲁棒数据
# ax.plot(forecast_df.index, forecast_df['nonr_forecast'], linestyle='--', marker='x', ms=5, lw=2, color='#7FB3D5', label='Robust Forecast')
#
# # # 绘制预测的鲁棒数据
# # ax.plot(forecast_df.index, forecast_df['r_forecast'], linestyle='--', marker='x', ms=5, lw=2, color='#C39BD3', label='Robust Forecast')
#
#
# # 添加网格
# ax.grid(ls='--')
#
# # 添加图例
# ax.legend(fontsize=12)
#
# # 显示图表
# plt.show()
