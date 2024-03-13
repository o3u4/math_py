from algorithm.liner import linear_regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'relate.xlsx'
sheet = "2000"
name = ["Superior", "Michigan and Huron", "St. Clair", "Erie", 'Ontario']
lst = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4),
       (2, 3), (2, 4), (3, 4)]
df = pd.read_excel(file, sheet_name=sheet)
para_list = []
for item in lst:
    x = item[0]
    y = item[1]
    a, b = linear_regression(df, x, y)
    print(a, b)
    para_list.append((a, b))

x = np.linspace(0, 10)
with plt.style.context('Solarize_Light2'):
    # plt.plot(x, np.sin(x) + x + np.random.randn(50))
    for index in range(len(para_list)):
        plt.plot(x, para_list[index][0] * x + para_list[index][1],
                 label=f"{name[lst[index][0]]}-{name[lst[index][1]]}")
    # Number of accent colors in the color scheme
    plt.title('10 relation Lines')
    plt.xlabel('lake1', fontsize=14)
    plt.ylabel('lake2', fontsize=14)

plt.legend()
plt.show()
