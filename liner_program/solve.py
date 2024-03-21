from liner_program.normalize import normal
from liner_program.simple_method import iterate

dimension = 3
max_f = [2, 4, 5, 0, 0, 0]
A = [[1, 3, -1, 1, 0, 0, 6],
     [0, 2, 2, 0, 1, 0, 4],
     [3, 1, 2, 0, 0, 1, 7]]


if __name__ == '__main__':
    f = input("是否输入标准型(y,Y/n,N):")
    flag = False
    if f == 'y' or f == 'Y':
        flag = True
        d = int(input('输入决策变量个数:'))
        tar = eval(input("以列表形式输入目标函数系数:"))
        matrix = eval(input("以列表形式输入标准型矩阵:"))
        g = input("是否展示迭代过程(y,Y/n,N):")
        process = False
        if g == 'y' or g == 'Y':
            process = True
        iterate(d, matrix, tar, process)
    else:
        is_positive = eval(input("以列表形式输入每个决策变量是否非负(1为非负, 0为任意, -1为非正):"))
        matrix = eval(input("以列表形式输入矩阵系数与符号(-1表示 <= , 0表示 = , 1表示 >):"))
        tar = eval(input("以列表形式输入未标准化前的目标函数系数:"))
        d, matrix = normal(is_positive, matrix)  # 决策变量个数, 标准型矩阵
        n = len(matrix[0])
        print(f'新增变量{n - d - 1}个')
        for i in range(d, n):
            tar.append(0)

        g = input("是否展示迭代过程(y,Y/n,N):")
        process = False
        if g == 'y' or g == 'Y':
            process = True
        iterate(d, matrix, tar, process)
