# 10835 큐
# 주소: https://www.acmicpc.net/problem/10835

# 제출한 답
import sys
from collections import deque
input = sys.stdin.readline


que = deque([])

t = int(input().rstrip())

for i in range(t):
    order = input().rstrip()

    if order[:4] == 'push':
        que.append(int(order[5:]))

    elif order == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif order == 'size':
        print(len(que))

    elif order == 'empty':
        if not que:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])

    elif order == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
