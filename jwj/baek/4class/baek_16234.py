from collections import deque


def open():
    visited = [[False] * N for _ in range(N)]
    people = {i: [] for i in range(N * N)}
    weight = [0] * (N * N)
    country = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                weight[country] += nation[i][j]
                people[country].append((i, j))
                while q:
                    x, y = q.popleft()

                    for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        n_x = x + d_x
                        n_y = y + d_y
                        if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                            n_v = abs(nation[x][y] - nation[n_x][n_y])
                            if L <= n_v <= R:
                                visited[n_x][n_y] = True
                                weight[country] += nation[n_x][n_y]
                                people[country].append((n_x, n_y))
                                q.append((n_x, n_y))

                country += 1

                if country == N * N:
                    return False

    for i in range(country):
        n_v = weight[i] // len(people[i])
        for x, y in people[i]:
            nation[x][y] = n_v

    return True


N, L, R = map(int, input().split())

nation = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

while True:
    if open():
        cnt += 1
    else:
        break

print(cnt)
