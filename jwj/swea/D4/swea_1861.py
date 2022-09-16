from collections import deque


def bfs(x, y):
    c = 1
    v = rooms[x][y]    # 노드

    q = deque()

    q.append((x, y))

    visited[x][y] = True

    while q:
        c_i, c_j = q.popleft()

        for d_i, d_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_i = c_i + d_i
            n_j = c_j + d_j

            if 0 <= n_i < N and 0 <= n_j < N and not visited[n_i][n_j]:
                if rooms[n_i][n_j] == rooms[c_i][c_j] - 1 or rooms[n_i][n_j] == rooms[c_i][c_j] + 1:
                    visited[n_i][n_j] = True
                    c += 1
                    if rooms[n_i][n_j] < v:
                        v = rooms[n_i][n_j]

                    q.append((n_i, n_j))

    return c, v


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    room = N * N

    visited = [[False] * N for _ in range(N)]

    rooms = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            cnt_res, v_res = bfs(i, j)

            if cnt < cnt_res:
                cnt = cnt_res
                room = v_res
            elif cnt == cnt_res and room > v_res:
                room = v_res

    print(f'#{test_case} {room} {cnt}')
