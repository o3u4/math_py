import pandas as pd
import re


class ExcelLoader:
    def __init__(self, excel_path):
        self.path = excel_path

    def load_excel(self, sheet_name=None):
        if sheet_name is None:
            data_frame = pd.read_excel(self.path)
            return data_frame
        else:
            data_frame = pd.read_excel(self.path, sheet_name=sheet_name)
            return data_frame

    def load_csv(self):
        data_frame = pd.read_csv(self.path)
        return data_frame

    @staticmethod
    def get_sub_data(data_frame, row_range=None, column_range=None):
        if row_range:
            if column_range:
                sub_data_frame = data_frame.iloc[row_range, column_range]
            else:
                sub_data_frame = data_frame.iloc[row_range, :]
        else:
            if column_range:
                sub_data_frame = data_frame.iloc[:, column_range]
            else:
                sub_data_frame = None
        return sub_data_frame

    @staticmethod
    def str_to_date(date_string, format_date='%Y年%m月'):
        dt = pd.to_datetime(date_string, format=format_date)
        return dt

    @staticmethod
    def trans_to_csv(data_frame, path, index=False, mode="w", sep=",",
                     date_format="%Y-%m-%d", encoding="utf-8"):
        if isinstance(data_frame, pd.DataFrame):
            data_frame.to_csv(path, index=index, mode=mode, sep=sep,
                              date_format=date_format, encoding=encoding)
        else:
            raise TypeError('Not a pandas DataFrame')

    @staticmethod
    def extract_by_re(data_frame, re_pattern, row_index=None, column_index=None):
        """
        抽取数据中某行某列，进行re提取，返回列表
        """
        data_series = None
        result_lst = []
        if row_index is not None:
            data_series = data_frame.iloc[row_index, :]

        else:
            if column_index is not None:
                data_series = data_frame.iloc[:, column_index]

        for i in range(len(data_series)):
            dt = str(data_series[i])
            matches = re.findall(re_pattern, dt)
            if matches:
                match = matches[0]
                result_lst.append(match)
            else:
                match = None
                result_lst.append(match)
        return result_lst


if __name__ == '__main__':
    path = "../2024-08数模/第四轮/data.csv"
    el = ExcelLoader(path)
    df = el.load_csv()
    pat = "(\d+)-(\d+)"
    lst = el.extract_by_re(df, pat, column_index=0)
    print(lst)
