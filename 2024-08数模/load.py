# 切分数据集
import pandas as pd
import numpy as np
import re

# Load the Excel file
file_path = 'C:/Users/WIN10/Desktop/数模/第三轮/B-2021B/附件1.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display the sheet names and a preview of the first sheet to understand the structure of the file
sheet_names = excel_data.sheet_names
first_sheet = excel_data.parse(sheet_names[0])

total = len(first_sheet)  # 114

group_index = []
group_comp = []
# re规则
pattern = r'(\d+)mg\s*(\d+\.?\d*)wt%Co/SiO2.\s*(\d+)mg\s*(.*)-乙醇浓度(\d+\.?\d*)ml/min.*'
comp = [set() for _ in range(5)]

for i in range(total):
    group_name = first_sheet.iloc[i, 0]
    if group_name is not np.nan:
        group_index.append(i)
        group_comp.append(first_sheet.iloc[i, 1])

for j in range(len(group_index)):
    group_name = first_sheet.iloc[group_index[j], 0]

    name = first_sheet.iloc[group_index[j], 1]
    matches = re.findall(pattern, name)
    comp_str = ",".join(matches[0])
    for i in range(len(matches[0])):
        match = matches[0]
        a = match[i]
        comp[i].add(a)

    if j == len(group_index) - 1:
        group_data = first_sheet.iloc[group_index[j]: total - 1, 2:]
    else:
        group_data = first_sheet.iloc[group_index[j]: group_index[j + 1], 2:]

    group_data.insert(0, "催化剂组合", [comp_str] * len(group_data))

    # output_file_path = f'C:/Users/WIN10/Desktop/数模/第三轮/B-2021B/切分数据集/xlsx/{group_name}.xlsx'
    # group_data.to_excel(output_file_path, index=False)
    output_file_path = f'C:/Users/WIN10/Desktop/数模/第三轮/B-2021B/切分数据集/csv2/{group_name}.csv'
    group_data.to_csv(output_file_path, index=False)
print(comp)

