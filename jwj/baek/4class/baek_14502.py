from collections import deque
from copy import deepcopy
import sys

def bfs(p_x, p_y, v_m):

    q = deque()
    q.append((p_x, p_y))

    while q:
        x, y = q.popleft()

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = x + d_x
            n_y = y + d_y

            if 0 <= n_x < N and 0 <= n_y < M and v_m[n_x][n_y] == 0:

                v_m[n_x][n_y] = 2
                q.append((n_x, n_y))
    
    return v_m


def dfs(depth, m):
    global maxV
    if depth == 3:
        sumV = 0
        tmp_m = deepcopy(m)
        for v in virus:
            tmp_m = bfs(v[0], v[1], tmp_m)

        for i in range(N):
            for j in range(M):
                if tmp_m[i][j] == 0:
                    sumV += 1

        if maxV < sumV:
            maxV = sumV
        
    else:
        for i in range(N):
            for j in range(M):
                if m[i][j] == 0:
                    m[i][j] = 1
                    dfs(depth+1, m)
                    m[i][j] = 0

input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

virus = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus.append((i, j))

maxV = 0

dfs(0, maps)

print(maxV)