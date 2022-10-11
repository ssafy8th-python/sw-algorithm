# 보물섬
from collections import deque
import sys

input = sys.stdin.readline

def bfs(r, c):
    global mx
    q = deque([(r,c)])
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))

    for lst in visited:
        mx = max(mx, max(lst))

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
mx = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i,j)

print(mx-1)