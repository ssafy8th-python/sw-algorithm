# 불
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
dir = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(fire , sr, sc):
    # 불
    q = deque(fire)
    visited = [[0]*w for _ in range(h)]
    for row, col in q:
        visited[row][col] = 1

    while q:
        f_r, f_c = q.popleft()
        for dr, dc in dir:
            f_nr, f_nc = f_r + dr, f_c + dc
            if 0 <= f_nr < h and 0 <= f_nc < w and not visited[f_nr][f_nc] and arr[f_nr][f_nc] != '#':
                visited[f_nr][f_nc] = visited[f_r][f_c] + 1
                q.append((f_nr,f_nc))


    # 상근이 위치
    sq = deque([(sr, sc)])
    s_visited = [[0] * w for _ in range(h)]
    s_visited[sr][sc] = 1



    while sq:
        s_r, s_c = sq.popleft()
        for dr, dc in dir:
            nr, nc = s_r+dr, s_c+dc
            if 0 <= nr < h and 0 <= nc < w and not s_visited[nr][nc] and arr[nr][nc] != '#'  and (visited[nr][nc] > s_visited[s_r][s_c]+1 or visited[nr][nc]==0):
                s_visited[nr][nc] = s_visited[s_r][s_c] + 1
                sq.append((nr, nc))


    res = []

    # 맨 첫 줄, 밑 줄 판별
    for c in range(w):
        if  s_visited[0][c]:
            res.append(s_visited[0][c])

        elif  s_visited[h-1][c]:
            res.append(s_visited[h-1][c])



    for r in range(h):
        if  s_visited[r][0]:
            res.append(s_visited[r][0])


        elif  s_visited[r][w-1]:
            res.append(s_visited[r][w-1])



    if res:
        print(min(res))
    else:
        print('IMPOSSIBLE')

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
    bfs(fire, st_r, st_c)


