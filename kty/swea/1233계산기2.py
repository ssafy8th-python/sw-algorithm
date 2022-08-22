import sys

sys.stdin = open("input_1223.txt", "r")

def step1(inputV):
    ST = []
    postOrder = []
    isp = {'+': 1, '*': 2}
    icp = {'+': 1, '*': 2}
    for token in inputV:
        if token in '0123456789':
            postOrder.append(token)

        else :
            if not ST:
                ST.append(token)
            elif isp[ST[-1]] < icp[token]:
                ST.append(token)
            else:
                while ST and isp[ST[-1]] >= icp[token]:
                    postOrder.append(ST.pop())
                ST.append(token)
    while ST:
        postOrder.append(ST.pop())

    return postOrder

def step2(inputV):
    ST = []

    for token in inputV:
        if token in '0123456789':
            ST.append(token)
        elif token == '+':
            right = int(ST.pop())
            left = int(ST.pop())
            ST.append(left+right)
        elif token == '*':
            right = int(ST.pop())
            left = int(ST.pop())
            ST.append(left*right)

    return ST[-1]

T = 10
for tc in range(1, T + 1):
    n = int(input())
    cal = input()
    postfix = ''.join(step1(cal))
    print(f'#{tc} {step2(postfix)}')
