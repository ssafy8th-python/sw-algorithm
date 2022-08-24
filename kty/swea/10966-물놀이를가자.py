import sys
from collections import deque
sys.stdin = open("input_10966.txt", "r")

def bfs(n, m):
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if world[row][col] == 'W':
                q.append((row, col))
                visited[row][col] = 0

    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    sumV = 0
    for i in range(n):
        for j in range(m):
            sumV += visited[i][j]

    return sumV

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    world = [input() for _ in range(n)]
    print(f'#{tc} {bfs(n, m)}')
