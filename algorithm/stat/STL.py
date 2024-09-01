from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import STL
import seaborn as sns
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.forecasting.stl import STLForecast
from statsmodels.graphics.tsaplots import plot_acf


class STL_MODEL:
    # 画图设置
    register_matplotlib_converters()
    sns.set_style("darkgrid")

    # 设置全局字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    plt.rc("figure", figsize=(16, 12))
    plt.rc("font", size=13)

    def __init__(self, data_frame, date_key, value_key, period, scale, robust=False):
        self.data_frame = data_frame
        self.date_key = date_key
        self.value_key = value_key
        self.period = period  # 周期
        self.scale = scale  # 年, 月, 日
        data_frame.set_index(date_key, inplace=True)    # 必须为时间格式
        data_frame = data_frame.dropna()
        data_frame = data_frame[~(data_frame == 0).any(axis=1)]  # 去除数据为0
        # 按时间升序排序
        data_frame.sort_index(ascending=True, inplace=True)
        self.stl_df = data_frame[[value_key]]  # 用于模型的数据

        self.stl = STL(self.stl_df, period=period, robust=robust)
        self.result = self.stl.fit()
        self.trend_strength = 0
        self.seasonal_strength = 0
        self.forecast_df = None
        self.forecast_index = None

    def model_plot(self):
        """
        模型分解结果4幅子图
        """
        self.result.plot()
        plt.show()

    @staticmethod
    def add_stl_plot(fig, res, legend):
        """Add 3 plots from a second STL fit"""
        axs = fig.get_axes()
        comps = ['trend', 'seasonal', 'resid']

        for ax, comp in zip(axs[1:], comps):
            series = getattr(res, comp)
            if comp == 'resid':
                ax.plot(series, marker='o', linestyle='none')
            else:
                ax.plot(series)
                if comp == 'trend':
                    ax.legend(legend, frameon=False)

    def plot_2_model(self, stl1, stl2, legend):
        """
        2个模型分解结果4幅子图
        :param stl1: 模型1
        :param stl2: 模型2
        :param legend: 列表格式的图例 [模型1, 模型2]
        """
        result1 = stl1.fit()
        fig = result1.plot()
        result2 = stl2.fit()
        self.add_stl_plot(fig, result2, legend)
        plt.show()

    def stat_coefficient(self):
        """
        进行模型数据提取
        :return:
        """
        # 数据提取
        self.stl_df['trend'] = self.result.trend
        self.stl_df['seasonal'] = self.result.seasonal
        self.stl_df['resid'] = self.result.resid

    def calc_coefficient(self):
        """
        先计算stat_coefficient()再运行
        :return:
        """
        self.stl_df['detrend'] = self.stl_df[self.value_key] - self.stl_df['trend']
        self.stl_df['deseasonal'] = self.stl_df[self.value_key] - self.stl_df['seasonal']

        self.trend_strength = max(0, 1 - self.stl_df.resid.var() / self.stl_df.deseasonal.var())

        self.seasonal_strength = max(0, 1 - self.stl_df.resid.var() / self.stl_df.detrend.var())

        print(f'trend_strength={round(self.trend_strength, 3)},'
              f'seasonal_strength={round(self.seasonal_strength, 3)}')

    def fit_trend_plot(self, size=(10, 8)):
        """
        先进行模型数据提取 stat_coefficient()
        :param size: 画布大小
        :return:
        """
        fig, ax = plt.subplots(figsize=size)

        self.stl_df.plot.line(ax=ax, y=self.value_key, marker='o', ms=5, lw=2,
                              color="#2B4868", fontsize=15, label='Real')

        self.stl_df.plot.line(ax=ax, y='trend', ms=5, lw=4,
                              color='#F2788F', fontsize=15, label='Trend')

        ax.grid(ls='--')
        ax.legend(fontsize=12)
        plt.show()

    def forecast(self, units, size=(10, 8)):
        self.stl_df.index.freq = self.stl_df.index.inferred_freq
        stl_forecast = STLForecast(self.stl_df[[self.value_key]], ARIMA,
                                   model_kwargs=dict(order=(1, 1, 0), trend='t'), period=self.period,
                                   robust=False).fit()
        forecast = stl_forecast.forecast(units)
        self.forecast_df = pd.DataFrame(forecast, columns=['forecast'])
        # 假设原始数据的最后一个索引是原始的时间索引格式
        last_date = pd.to_datetime(self.stl_df.index[-1])  # 获取原始数据的最后一个日期
        if self.scale == "m":
            # 生成预测期的时间索引，按月增加
            self.forecast_index = pd.date_range(start=last_date +
                                                      pd.DateOffset(months=1),
                                                periods=units, freq='MS')
        if self.scale == "y":
            # 生成预测期的时间索引，按年增加
            self.forecast_index = pd.date_range(start=last_date +
                                                      pd.DateOffset(year=1),
                                                periods=units, freq='AS')
        if self.scale == "d":
            self.forecast_index = pd.date_range(start=last_date, periods=units, freq='D')
        if self.scale not in ["d", "m", "y"]:
            raise ValueError("scale must be either 'm', 'd', or 'y'")

        self.forecast_df.index = self.forecast_index
        print(self.forecast_df.shape)
        print(self.forecast_df.head())

        fig, ax = plt.subplots(figsize=size)
        self.stl_df.plot.line(ax=ax, y=self.value_key, marker='o', ms=5, lw=2,
                              color="#2B4868", fontsize=15, label='Real')
        self.stl_df.plot.line(ax=ax, y='trend', ms=5, lw=4,
                              color='#F2788F', fontsize=15, label="Trend")

        # 预测的数据
        ax.plot(self.forecast_df.index, self.forecast_df['forecast'],
                linestyle='--', marker='x', ms=5, lw=2,
                color='#7FB3D5', label='Forecast')
        # 添加网格
        ax.grid(ls='--')

        # 添加图例
        ax.legend(fontsize=12)

        # 显示图表
        plt.show()

    def ACF_plot(self):
        # 绘制 ACF 图
        fig, ax = plt.subplots(figsize=(10, 6))
        df = self.stl_df[self.value_key]
        plot_acf(df, lags=100, ax=ax)
        # 设置x轴标签、y轴标签、标题
        ax.set_xlabel('Lags', fontsize=14)
        ax.set_ylabel('Autocorrelation', fontsize=14)
        ax.set_title('ACF of Series', fontsize=16)
        plt.show()


if __name__ == '__main__':
    path = r"D:\python_math\2024-08数模\第四轮\data.csv"
    data = pd.read_csv(path)
    data['Period'] = pd.to_datetime(data['Time'], format='%Y-%m')
    data2 = data.copy()
    m1 = STL_MODEL(data, 'Period', "Price", 7, "m")
    m2 = STL_MODEL(data2, 'Period', "Price", 7, "m", robust=True)
    # m1.model_plot()
    # m1.plot_2_model(m1.stl, m2.stl, ["n", "r"])
    m1.stat_coefficient()
    m1.calc_coefficient()
    # m1.fit_trend_plot()
    # m1.forecast(60)
    m1.ACF_plot()
