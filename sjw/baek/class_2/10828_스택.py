# 10828 스택
# 주소: https://www.acmicpc.net/problem/10828

# 제출한 답
import sys
input = sys.stdin.readline


stack = []

t = int(input().rstrip())

for i in range(t):
    order = input().rstrip()

    if order[:4] == 'push':
        stack.append(int(order[5:]))

    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])