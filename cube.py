import kociemba

order = ['上面', '右面', '前面', '下面', '左面', '后面']
operate = ['U', 'R', 'F', 'D', 'L', 'B']
center = []
init_color = []
init_state = []

for i in range(6):
    print(f'输入{order[i]}颜色')
    for j in range(9):
        a = input(f'第{j + 1}个:')
        init_color.append(a)
        if j == 4:
            center.append(a)


for item in init_color:
    num = center.index(item)
    init_state.append(operate[num])

init = ''.join(init_state)
'FFR,UUD,BDL    DBF,RRD,BBU    UFB,RFF,LUR    URD,UDR,RBF    DLL,BLD,BFF    DLL,LBL,RUU'
solve = kociemba.solve(init)
action = solve.split(' ')
t = 0
for item in action:
    if '2' in item:
        t += 1
times = t + len(action)
print(solve)
print(f'花了{times}步')
