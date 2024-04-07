from sympy import symbols, And, Or, Not, simplify_logic

# 定义逻辑变量
a, b, c, d = symbols('a b c d')

# 定义逻辑表达式
expression = And(Or(a, b, c, d), Or(Not(a), b, c, d), Or(Not(b), a, c, d),
                 Or(Not(c), b, a, d), Or(Not(d), b, c, a))

# 化简逻辑表达式
simplified_expression = simplify_logic(expression)

print(simplified_expression)
