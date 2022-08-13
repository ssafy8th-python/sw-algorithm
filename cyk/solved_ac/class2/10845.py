import sys
input = sys.stdin.readline

n = int(input())

queue = []

for _ in range(n):
    item = input().split()
    cmd = item[0]
    if cmd == 'push':
        queue.append(item[1])
    if cmd == 'pop':
        if len(queue):
            print(queue.pop(0))
        else:
            print('-1')
    if cmd == 'size':
        print(len(queue))
    if cmd == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    if cmd == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    if cmd == 'back':
        if len(queue):
            print(queue[len(queue)-1])
        else:
            print(-1)
