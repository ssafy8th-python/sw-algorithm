from collections import deque


def bfs():
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        i, j = q.popleft()

        for d_x, d_y in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            n_x, n_y = i + d_x, j + d_y

            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                q.append((n_x, n_y))
                visited[n_x][n_y] = visited[i][j] + 1
                if maps[n_x][n_y] != 0:
                    print(maps[n_x][n_y])
                    print(visited[n_x][n_y] - 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    x, y = 0, 0

    maps = [list(map(int, input().split())) for _ in range(N)]

    monster = []

    bfs()

    print(f'#{tc}')
