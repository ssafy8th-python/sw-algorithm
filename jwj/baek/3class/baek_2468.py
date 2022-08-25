from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline


def bfs(tmp_g):
    q = deque()
    count = 0
    for i in range(N):
        for j in range(N):
            if tmp_g[i][j] != 0:
                count += 1
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        n_x = x+delta_x
                        n_y = y+delta_y

                        if 0 <= n_x < N and 0 <= n_y < N:
                            if tmp_g[n_x][n_y] != 0:
                                q.append((n_x, n_y))
                                tmp_g[n_x][n_y] = 0
    return count


N = int(input())

ground = [list(map(int, input().split())) for _ in range(N)]

minV = min(min(ground))
maxV = max(max(ground))

result = 0
for water in range(minV-1, maxV+1):
    tmp_ground = deepcopy(ground)
    for i in range(N):
        for j in range(N):
            if tmp_ground[i][j] <= water:
                tmp_ground[i][j] = 0

    cnt = bfs(tmp_ground)
    if cnt > result:
        result = cnt

print(result)
