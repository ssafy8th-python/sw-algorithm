dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def dfs(x, y, lst):
    global result
    d_x, d_y = dirs.get(zone[x][y])

    n_x, n_y = x + d_x, y + d_y

    if 0 <= n_x < N and 0 <= n_y < M:
        # 방문하지 않았을 때
        if not visited[n_x][n_y]:
            visited[n_x][n_y] = True
            lst.add((n_x, n_y))
            return dfs(n_x, n_y, lst)
        # 방문한 곳일 때
        elif (n_x, n_y) in lst:
            return 1
        else:
            return 0

    # 끝까지 갔을 때
    return 1


N, M = map(int, input().split())

zone = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            lst = set()
            lst.add((i, j))
            visited[i][j] = True
            result += dfs(i, j, lst)
print(result)
