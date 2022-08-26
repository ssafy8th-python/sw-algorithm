from collections import deque


def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    while que:
        x, y = que.popleft()

        for d_x, d_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            n_x = x + d_x
            n_y = y + d_y

            if 0 <= n_x < N and 0 <= n_y < M and not visited[n_x][n_y] and ice[n_x][n_y] != 0:
                visited[n_x][n_y] = True
                que.append((n_x, n_y))


N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

q = deque()

cnt = 0

for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            q.append((i, j, 0))

check_num = 0

while q:
    x, y, cnt = q.popleft()
    overlap = 0

    if cnt == check_num:
        check_num += 1
        tmp_value = 0

        visited = [[False] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if ice[i][j] != 0 and not visited[i][j]:
                    if tmp_value == 1:
                        tmp_value += 1
                        break
                    bfs(i, j)
                    tmp_value += 1

            if tmp_value == 2:
                break

    if tmp_value == 2:
        break

    for d_x, d_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        n_x = x + d_x
        n_y = y + d_y

        if 0 <= n_x < N and 0 <= n_y < M:
            if ice[n_x][n_y] != 0:
                ice[n_x][n_y] -= 1

                if not overlap:
                    q.append((x, y, cnt + 1))

                overlap += 1

                if ice[n_x][n_y] == 0:
                    q.append((n_x, n_y, cnt+1))

if not tmp_value:
    cnt = 0

print(cnt)



