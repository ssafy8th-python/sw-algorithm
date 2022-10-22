# 뱀과 사다리 게임
from collections import deque
import sys

def bfs(cur):
    q = deque([(cur,0)])
    check = set()
    check.add(cur)
    while q:
        cr, cnt = q.popleft()
        if cr == 100:
            print(cnt)
            return
        for i in range(1, 7):
            if cr+i <= 100 and board[cr+i] == 0 and cr+i not in check:
                q.append((cr+i, cnt+1))
                check.add(cr+i)
            elif cr+i <= 100 and board[cr+i] != 0 and cr+i not in check:
                q.append((board[cr+i], cnt+1))
                check.add(cr+i)

N, M = map(int, input().split())
board = [0]*101
for _ in range(N+M):
    n1, n2 = map(int, input().split())
    board[n1] = n2

bfs(1)