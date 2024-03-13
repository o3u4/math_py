import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# 求某一行数据的平均数
row_mean = df.mean(axis=1)

# 将每个数据减去这个平均数得到新的数据
new_df = df.sub(row_mean, axis=0)

print(new_df)
