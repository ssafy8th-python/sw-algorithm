# 10866 덱
# 주소: https://www.acmicpc.net/problem/10866

# 제출한 답
import sys
from collections import deque
input = sys.stdin.readline


que = deque([])

t = int(input().rstrip())

for i in range(t):
    order = input().rstrip()

    if order[:6] == 'push_f':
        que.appendleft(int(order[11:]))

    if order[:6] == 'push_b':
        que.append(int(order[10:]))

    elif order == 'pop_front':
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif order == 'pop_back':
        if not que:
            print(-1)
        else:
            print(que.pop())

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
