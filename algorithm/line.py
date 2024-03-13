# 线性拟合

from algorithm.liner import linear_regression
import pandas as pd

df = pd.read_excel('../relate.xlsx', sheet_name='2000')
lakes = []
a, b = linear_regression(df, 0, 1)
print(a, b)
