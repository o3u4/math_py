from liner_program.normalize import neg_to_positive
from liner_program.normalize import normal
from liner_program.simple_method import iterate
from liner_program.big_M import big_m_solve
from liner_program.two_stage import two_stage_solve

if __name__ == '__main__':
    f1 = input("是否输入资源配置型问题(y,Y/n,N)")
    if f1 == 'y' or f1 == 'Y':
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
            iterate(matrix, tar, process)
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
            iterate(matrix, tar, process)
    else:
        is_positive = eval(input("以列表形式输入每个决策变量是否非负(1为非负, 0为任意, -1为非正):"))
        matrix = eval(input("以列表形式输入矩阵系数与符号(-1表示 <= , 0表示 = , 1表示 >):"))
        tar = eval(input("以列表形式输入初始的目标函数系数:"))
        f2 = int(input("以什么方法解决问题(1: 大M法/2: 二阶段法)"))
        if f2 == 1:
            m = int(input("输入大M取值(整数):"))
            matrix = neg_to_positive(is_positive, matrix)  # 变量取正
            g = input("是否展示迭代过程(y,Y/n,N):")
            process = False
            if g == 'y' or g == 'Y':
                process = True
            big_m_solve(matrix, tar, m, process)
        else:
            g = input("是否展示迭代过程(y,Y/n,N):")
            process = False
            if g == 'y' or g == 'Y':
                process = True
            two_stage_solve(matrix, tar, process)
