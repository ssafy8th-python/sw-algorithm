import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    lst = input().split()
    if lst[0] == 'push':
        stack.append(lst[1])
    elif lst[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif lst[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif lst[0] == 'top':
        if len(stack):
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif lst[0] == 'size':
        print(len(stack))

