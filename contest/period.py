import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
from algorithm.func_fit import point_fit

# Fixing random state for reproducibility

file = 'relate.xlsx'
sheet = "2000"

df = pd.read_excel(file, sheet_name=sheet)


def sin_fit(x, a, b, c, d):
    return a * np.sin(b * x + c) + d


def point(*index):
    para_list = []
    l = len(index)
    colors = ['red', 'green', 'blue', 'black', '#FF6F91']
    fit_colors = cm.viridis(np.linspace(0, 1, 5))
    for dex in range(l):
        lake = str(df.columns[index[dex]])
        # print(lake)
        month = df.iloc[0: 12, index[dex]]
        row_mean = month.mean()
        print(row_mean)
        new_df = month - row_mean
        new_df = np.array(new_df)

        lst1 = [i for i in range(1, 13)]
        lst2 = new_df

        paras = point_fit(sin_fit, lst1, lst2)
        para_list.append(paras)

        with plt.style.context('Solarize_Light2'):
            # Number of accent colors in the color scheme
            # 散点图
            plt.scatter(lst1, lst2, color=colors[dex], marker='o', label=f"{lake}")
            # 拟合图
            x = np.linspace(1, 12, 1000)
            plt.plot(x, sin_fit(x, *paras), color=fit_colors[dex],
                     label=f"{lake}'s fitted curve")

    plt.title("height wave")
    plt.xlabel('month', fontsize=14)
    plt.ylabel('height', fontsize=14)
    plt.legend()
    plt.show()
    return para_list


if __name__ == '__main__':
    para = point(0, 1, 2, 3, 4)
    print(para)
    for item in para:
        for p in range(len(item)):
            item[p] = round(item[p], 1)
        print(f'{item[0]}sin({item[1]}x+{item[2]})+{item[3]}')
