from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    visited = [[False] * M for _ in range(N)]

    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 1

    while q:
        i, j, cnt = q.popleft()

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = i + d_x
            n_y = j + d_y
            if 0 <= n_x < N and  0 <= n_y < M and maps[n_x][n_y] == 'L' and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                q.append((n_x, n_y, cnt+1))

    return cnt

N, M = map(int, input().split())

maps = [list(input()) for _ in range(N)]

maxV = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            result = bfs(i, j)
            if maxV < result:
                maxV = result

print(maxV)
