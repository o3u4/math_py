# 切分数据集
import pandas as pd
import numpy as np
import re

# Load the Excel file
file_path = r"C:\Users\WIN10\Desktop\数模\第四轮\C\data\地区生产总值.xlsx"
path = r"C:\Users\WIN10\Desktop\数模\第四轮\C\data\地区生产总值.csv"
excel_data = pd.ExcelFile(file_path)

# Display the sheet names and a preview of the first sheet to understand the structure of the file
sheet_names = excel_data.sheet_names
first_sheet = excel_data.parse(sheet_names[0])

total = len(first_sheet)
print(total)

# re规则
pattern1 = r'(\d+)年(\d+)月'
pattern2 = r'(\d+).(\d+)'
pattern3 = r'(\d+)年第(\d)季度'

index = 0
item_lst = []
price_list = []
lst2 = []
while 1:
    item = first_sheet.iloc[index, 0]

    item_matches = re.findall(pattern3, str(item))

    if item_matches:
        item_match = item_matches[0]
        st = ""
        if item_match[1] == "1":
            st = "02"
        if item_match[1] == "2":
            st = "05"
        if item_match[1] == "3":
            st = "08"
        if item_match[1] == "4":
            st = "11"
        item_str = item_match[0] + "-" + st

        # if len(item_match[1]) == 1:
        #     it = "0" + item_match[1]
        # else:
        #     it = item_match[1]
        # item_str = "-".join(item_match)
        # item_str = item_match[0] + "-" + it
        item_lst.append(item_str)
        price_list.append(first_sheet.iloc[index, 1])
        lst2.append(first_sheet.iloc[index, 2])
        if item_str == "2017-02":
            break
    index += 1

df = pd.DataFrame({
    'Time': pd.Series(item_lst, dtype='str'),
    'Sum': pd.Series(price_list, dtype='float'),
    'Up': pd.Series(lst2, dtype='float')
})
print(df)

df.to_csv(path, index=False)
