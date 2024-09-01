import pmdarima as pm
import pandas as pd


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
# 自动选择最佳的SARIMA参数
model = pm.auto_arima(stl_df,
                      seasonal=True,  # 需要季节性
                      m=7,  # 季节性周期长度（例如7天）
                      d=2,  # 二阶差分
                      stepwise=True,  # 使用逐步搜索策略
                      trace=True)  # 显示搜索过程中的参数组合
"""
ARIMA(2,2,2)(1,0,1)[7]             : AIC=2222.133
ARIMA(0,2,0)(0,0,0)[7]             : AIC=2267.698
ARIMA(1,2,0)(1,0,0)[7]             : AIC=2233.116
ARIMA(0,2,1)(0,0,1)[7]             : AIC=2218.110
ARIMA(0,2,1)(0,0,0)[7]             : AIC=2216.115
ARIMA(0,2,1)(1,0,0)[7]             : AIC=2218.110
ARIMA(0,2,1)(1,0,1)[7]             : AIC=inf, Tim
ARIMA(1,2,1)(0,0,0)[7]             : AIC=2216.059
ARIMA(1,2,1)(1,0,0)[7]             : AIC=2218.046
ARIMA(1,2,1)(0,0,1)[7]             : AIC=2218.046
ARIMA(1,2,1)(1,0,1)[7]             : AIC=2220.051
ARIMA(1,2,0)(0,0,0)[7]             : AIC=2231.402
ARIMA(2,2,1)(0,0,0)[7]             : AIC=2216.366
ARIMA(1,2,2)(0,0,0)[7]             : AIC=2217.098
ARIMA(0,2,2)(0,0,0)[7]             : AIC=2216.703
ARIMA(2,2,0)(0,0,0)[7]             : AIC=2227.852
ARIMA(2,2,2)(0,0,0)[7]             : AIC=2218.272
ARIMA(1,2,1)(0,0,0)[7] intercept   : AIC=2216.996
"""
# 打印最佳参数
print(model.summary())
