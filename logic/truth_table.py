from sympy import symbols, And, Or, Not, simplify_logic


def logic(table):
    """
    根据真值表得出逻辑表达式
    :param table: 真值表
    :return:
    expression: 表达式
    """
    x = len(table[0][0])  # 事件个数
    var_list = symbols(" ".join([f'A{i}' for i in range(x)]))  # 定义变量

    num_0, num_1 = [], []
    for n in range(len(table)):  # 判断0多还是1多
        # row [[1, 1], 0]
        if table[n][1] == 1:
            num_1.append(n)
        else:
            num_0.append(n)

    if len(num_1) >= len(num_0):  # 输入写成乘积, 每行都相加
        tb = [table[i] for i in num_1]  # 从原始表里提取值为 1 的行
        expr = False
        for row in tb:  # 相并
            expr1 = True
            for j in range(x):  # 相交
                if row[0][j] == 1:
                    expr1 = And(expr1, var_list[j])
                else:
                    expr1 = And(expr1, Not(var_list[j]))
            expr = Or(expr, expr1)
        expression = simplify_logic(expr)
        print("未化简的逻辑表达式:", expr)
        print("化简后的逻辑表达式:", expression)
        return expression

    else:  # 输入写成相加, 每行都乘
        tb = [table[i] for i in num_0]  # 从原始表里提取值为 0 的行
        expr = True
        for row in tb:  # 相加
            expr1 = False
            for j in range(x):  # 相乘
                if row[0][j] == 0:
                    expr1 = Or(expr1, var_list[j])
                else:
                    expr1 = Or(expr1, Not(var_list[j]))
            expr = And(expr, expr1)
        expression = simplify_logic(expr)
        print("未化简的逻辑表达式:", expr)
        print("化简后的逻辑表达式:", expression)
        return expression


def prt(tabel):
    x = len(tabel[0][0])
    for row in tabel:  # [[1, 1], 0]
        for i in range(x):
            print(row[0][i], end=' ')
        print("|", row[1])


def read(row_num):
    print("-----------输入真值表-----------")
    print("格式: 1 1 | 0 ( | 左边为输入, 右边为输出, 以空格分割) ")
    table = []
    for i in range(row_num):
        s = input(f"第{i + 1}行:")
        a = s.split(" ")
        a.remove("|")
        x = len(a)
        b = [int(a[i]) for i in range(x - 1)]
        row = [b, int(a[x - 1])]
        table.append(row)
    return table


if __name__ == '__main__':
    n = int(input("输入真值表行数(有几种状态):"))
    table_ = read(n)
    print("-----------输入的真值表为-----------")
    prt(table_)
    print('-----------表达式为-----------')
    logic(table_)
    print("注: Ai 为变量名, & 为与, | 为并, ~ 为非")

