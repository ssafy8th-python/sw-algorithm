# 인구이동
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def bfs(r,c):
    q = deque([(r,c)])
    visited[r][c] = False
    union = deque([(r, c)])
    sum_union = arr[r][c]
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[0,-1],[0,1],[-1,0],[1,0]]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] and L <= abs(arr[nr][nc] - arr[cr][cc]) <= R:
                union.append((nr, nc))
                sum_union += arr[nr][nc]
                visited[nr][nc] = False
                q.append((nr, nc))

    for ur, uc in union:
        arr[ur][uc] = sum_union//len(union)

    return len(union)

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
flag = 1

while flag:
    visited = [[True]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                if bfs(i,j) > 1:
                    flag = 1
    if not flag:
        break

    cnt += 1
print(cnt)
