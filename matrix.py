import sympy as sp

# 创建一个示例矩阵
matrix = sp.Matrix([[1, 2, 1],
                   [2, 3, 1],
                   [3, 4, 1]])
a = matrix.tolist()     # 转换成列表
sp.zeros(3, 1)      # 零矩阵

m = matrix.rref()[0]    # 返回第一个为矩阵，第二个为主元位置
m.col(0)   # 获取列
# m.col_del(0)    # 删除列

m = m.row_insert(1, sp.Matrix([[2, 1, 1]]))     # 插入行
m = m.T     # 转置

i = sp.eye(3)
i = - i
dt = i.det()    # 行列式
dg = sp.diag(*[1, 2, 3])   # 对角矩阵
