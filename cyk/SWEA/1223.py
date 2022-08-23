# import sys
# sys.stdin = open("input (6).txt", "r")

def step1(s):
    ST = []
    postOrder =[]
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    for token in s:
        if token.isdigit():
            postOrder.append(token)
        elif token == ')':
            while ST and ST[-1] != '(':
                postOrder.append(ST.pop())
            ST.pop()
        else:
            while ST and icp[token] <= isp[ST[-1]]:
                postOrder.append(ST.pop())
            ST.append(token)
    while ST:
        postOrder.append(ST.pop())
    return postOrder

def step2(postOrder):
    ST = []
    for token in postOrder:
        if token.isdigit():
            ST.append(token)
        elif token == '+':
            a = ST.pop()
            b = ST.pop()
            ST.append(int(a)+int(b))
        elif token == '-':
            a = ST.pop()
            b = ST.pop()
            ST.append(int(b)-int(a))
        elif token == '*':
            a = ST.pop()
            b = ST.pop()
            ST.append(int(a) * int(b))
        elif token == '/':
            a = ST.pop()
            b = ST.pop()
            ST.append(int(b) / int(a))
    return ST[-1]


for tc in range(1,2):
    N = int(input())
    s = list(input())
    result = step1(s)
    print(f'#{tc} {step2(result)}')
