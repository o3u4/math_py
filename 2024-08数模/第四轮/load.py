from load_data.load_excel import ExcelLoader
import pandas as pd

excel_path = r"data.xlsx"
csv_path = r"C:\Users\WIN10\Desktop\数模\第四轮\C\tt_data.csv"
e = ExcelLoader(excel_path)
excel_data = pd.read_excel(excel_path)
print(type(excel_data))
# e.trans_to_csv(excel_data, path=csv_path)
