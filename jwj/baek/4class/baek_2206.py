from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

block_map = [input().rstrip() for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


N -= 1
M -= 1

q = deque()

q.append((0, 0, False))

visited[0][0][0] = 1
visited[0][0][1] = 1

result = 0

while q:
    x, y, crash = q.popleft()

    if x == N and y == M:
        result = visited[x][y][crash]
        break

    for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n_x = x + d_x
        n_y = y + d_y

        if 0 <= n_x <= N and 0 <= n_y <= M:
            # 벽을 부수지 않는 경우
            if not visited[n_x][n_y][crash] and block_map[n_x][n_y] == '0':
                visited[n_x][n_y][crash] = visited[x][y][crash] + 1
                q.append((n_x, n_y, crash))

            # 벽을 부수는 경우
            elif not crash and block_map[n_x][n_y] == '1':
                visited[n_x][n_y][1] = visited[x][y][0] + 1
                q.append((n_x, n_y, True))
else:
    result = -1

print(result)