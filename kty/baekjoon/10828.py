import sys
n = int(sys.stdin.readline())

memory = []
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        memory.append(order[1])

    elif order[0] == 'pop':
        if memory == []:
            print(-1)
        else:
            print(memory.pop())

    elif order[0] == 'size':
        print(len(memory))

    elif order[0] == 'empty':
        if memory == []:
            print(1)
        else:
            print(0)

    elif order[0] == 'top':
        if memory == []:
            print(-1)
        else:
            print(memory[-1])
