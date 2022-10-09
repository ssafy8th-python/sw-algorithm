# 불
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
dir = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(fire, r, c):
    q = deque(fire)
    visited = [[True]*w for _ in range(h)]
    visited[q[0][0]][q[0][1]] = False
    while q:
        f_r, f_c = q.popleft()
        for dr, dc in dir:
            f_nr, f_nc = f_r + dr, f_c + dc
            if 0 <= f_nr < h and 0 <= f_nc < w and visited[f_nr][f_nc] and arr[f_nr][f_nc] == '.':
                arr[f_nr][f_nc] = '*'
                visited[f_nr][f_nc] = False
                q.append((f_nr,f_nc))
    

for _ in range(T):
    w, h = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]
    fire = []     # 불의 위치
    for r in range(h):
        for c in range(w):
            if arr[r][c] == '*':
                fire.append((r, c))
            if arr[r][c] == '@':
                st_r, st_c = r, c
    if not fire:
        print('IMPOSSIBLE')
    else:

        bfs(fire, st_r, st_c)
