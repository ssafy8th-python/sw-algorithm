# 14940 쉬운 최단거리
# 주소: https://www.acmicpc.net/problem/14940

# 제출한 답
import sys
from collections import deque


def init():
    value = (0, 0)
    for i in range(len(map_lst)):
        for j in range(len(map_lst[0])):
            if map_lst[i][j] == 2:
                value = (i, j)
            elif map_lst[i][j] == 0:
                visited[i][j] = 0

    return value


input = sys.stdin.readline
n, m = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

start = init()
visited[start[0]][start[1]] = 0
queue = deque([start])

while queue:
    r, c = queue.popleft()

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc] == -1 and map_lst[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

for i in range(n):
    print(*visited[i])
