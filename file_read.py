import pandas as pd


def func(output_sheet_name, col):
    # 读取第1，3，5，7，9个工作表的第八行数据
    file_path = 'contest/Problem_D_Great_Lakes.xlsx'
    output_file_path = 'contest/relate.xlsx'
    selected_sheets = [1, 3, 5, 7, 9]

    # 使用pd.ExcelFile来打开Excel文件
    xls = pd.ExcelFile(file_path)

    # 获取Excel文件中的所有工作表名称
    sheet_names = xls.sheet_names

    data_frames = []
    for sheet_index in selected_sheets:
        # (..nrows=8).iloc[7], 读取前8行, 选择第8行, 索引7
        df = pd.read_excel(file_path, sheet_name=sheet_index - 1, header=None, nrows=col).iloc[col - 1]
        data_frames.append(df)

    # 将数据写入新的excel文档的新工作表2001中
    with pd.ExcelWriter(output_file_path, mode='a', if_sheet_exists='replace') as writer:
        combined_df = pd.concat([data for data in data_frames], axis=1)
        combined_df.to_excel(writer, sheet_name=output_sheet_name, index=False)


if __name__ == '__main__':
    sheet_name = [str(i) for i in range(2001, 2023)]
    col = [j for j in range(9, 31)]
    for k in range(22):
        func(sheet_name[k], col[k])
