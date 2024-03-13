# 相关系数

from algorithm.spearman import calculate_spearman_correlation, find_representative_variable
import pandas as pd

# 读取Excel文件
df = pd.read_excel('dt.xlsx')


def choose_data(relate):
    data_lst = []
    name_lst = []
    for item in relate:
        column_data = df.iloc[:, item]  # 通过列的索引位置提取，假设这里是第一列
        name_lst.append(column_data.name)  # 标题
        data_lst.append(list(column_data[0: 6]))  # 数据
    return name_lst, data_lst


def anls(relate):
    name, data = choose_data(relate)
    corr_table = calculate_spearman_correlation(*data)  # spearman表格

    # 找出代表所有变量的一个变量
    representative_index = find_representative_variable(corr_table)
    representative_item = [name[representative_index], data[representative_index]]
    return corr_table, representative_item


if __name__ == '__main__':
    relate1 = [1, 2, 6]
    relate2 = [3, 4, 5, 8, 9, 10, 16]
    relate3 = [7, 11, 12, 13, 14, 15, 17]
    relates = [relate1, relate2, relate3]
    rep_data_lst = []  # 代表元
    rep_name_lst = []
    table_lst = []  # 0-2为组内关系, 3为组间关系
    for it in relates:
        table, rep_item = anls(it)
        # print(table)
        table_lst.append(table)
        # print(rep_item)
        rep_data_lst.append(rep_item[1])
        rep_name_lst.append(rep_item[0])
    crr_table = calculate_spearman_correlation(*rep_data_lst)  # 组别间的关系
    table_lst.append(crr_table)

    nm = choose_data(relates[0])[0]     # 前三个输出
    print(nm)
    print(table_lst[0])

    print(rep_name_lst)     # 第4个输出
    print(table_lst[3])
