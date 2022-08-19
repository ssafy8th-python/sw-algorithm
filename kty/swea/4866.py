import sys

sys.stdin = open("input_4866.txt", "r")

def pack(N):

    for i in N:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '(' and i == ')':
                stack.pop()
    if stack:
        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    N = input()
    stack = []

    print(f'#{tc} {pack(N)}')
