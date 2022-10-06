# 다리만들기 2
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
land = dict()
field = []

# 섬 구분
def bfs(r, c, color):
    q = deque([(r, c)])
    visited = [[True]*M for _ in range(N)]
    visited[r][c] = False
    arr[r][c] = color
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] and arr[nr][nc] == 1:
                arr[nr][nc] = color
                visited[nr][nc] = False
                q.append((nr, nc))
color = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i, j, color)
            color += 1
start = color
land_num = color
# 섬의 좌표 구하기
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            land[(i, j)] = arr[i][j]
            field.append((i, j,arr[i][j]))
            if start > arr[i][j]:
                start = arr[i][j]
# 다리 제작
edges = []
for r, c, color in field:
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        cnt = 0
        nr, nc = r+dr, c+dc
        while True:
            if 0 <= nr < N and 0 <= nc < M:
                tmp_color = land.get((nr, nc))
                if tmp_color == color:      # 같은섬
                    break
                if tmp_color == None:       # 바다
                    nr+=dr                  # 같은방향으로 이동
                    nc+=dc
                    cnt += 1
                    continue
                if cnt < 2:
                    break
                edges.append((cnt, color, tmp_color))
                break
            else:

                break

#크루스칼 알고리즘
def f_p(p, x):
    if p[x] !=x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = f_p(p,a), f_p(p,b)
    p[max(a,b)] = min(a,b)

edges.sort()
result = 0
count = 0
p = [i for i in range(land_num)]
for w, a, b in edges:
    if f_p(p, a)!=f_p(p,b):
        union(p, a, b)
        result += w
        count += 1

if count == land_num-start-1:
    print(result)
else:
    print(-1)

