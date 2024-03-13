from algorithm.spearman import calculate_spearman_correlation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def relation(year):
    file = 'relate.xlsx'
    sheet = str(year)

    df = pd.read_excel(file, sheet_name=sheet)
    lakes = []
    if year == 2000:
        for i in range(5):
            data = df.iloc[0: 12, i]
            lakes.append(list(data))
    else:
        for i in range(5):
            data = df.iloc[2: 14, i]
            lakes.append(list(data))
    # print(lakes)

    corr_table = calculate_spearman_correlation(*lakes)
    print(corr_table)
    new = np.array(corr_table).round(1)

    lakes_name = ["Superior", "Michigan and Huron", "St. Clair", "Erie", 'Ontario']

    relate = new

    fig, ax = plt.subplots()
    im = ax.imshow(relate, cmap='YlOrRd')  # 设置颜色映射为黄色和红色系

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(lakes_name)))
    ax.set_yticks(np.arange(len(lakes_name)))
    ax.set_xticklabels(lakes_name, rotation=45, ha="right")
    ax.set_yticklabels(lakes_name)

    # Loop over data dimensions and create text annotations
    for i in range(len(lakes_name)):
        for j in range(len(lakes_name)):
            text = ax.text(j, i, relate[i, j], ha="center", va="center", color="w")

    # 添加颜色条
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.set_label('Harvest amount')

    ax.set_title(f"The relationship heatmap of water level for each lake in {year}")
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    for k in range(2011, 2023):
        relation(k)

