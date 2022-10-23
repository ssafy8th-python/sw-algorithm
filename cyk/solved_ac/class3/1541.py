# 잃어버린 괄호
import sys
input = sys.stdin.readline

num = ''
op = []
for e in input().strip():
    if e in '0123456789':
        num += e
    else:
        op.append(int(num))
        op.append(e)
        num = ''
else:
    op.append(int(num))

flag = 1
res = 0
tmp = 0
for i in range(len(op)):
    if i == 0:
        res += op[i]
    elif op[i] == '-':
        flag = 0

    if i != 0 and flag:
        if type(op[i]) == int:
            res += op[i]
    elif i != 0 and not flag:
        if type(op[i]) == int:
            res -= op[i]
print(res)

