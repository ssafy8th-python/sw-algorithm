from collections import deque


def even_bfs(g_num, bfs_visited):
    x, y, cnt = gates[g_num][0], gates[g_num][1], 1
    sumV = 0
    if not bfs_visited[x]:
        bfs_visited[x] = 1
        sumV += 1
        y -= 1

    while y:
        for d_x in (-cnt, cnt):
            n_x = x + d_x

            if 1 <= n_x <= N and not bfs_visited[n_x]:
                bfs_visited[n_x] = cnt + 1
                sumV += cnt + 1
                y -= 1

            if y == 0:
                break
        cnt += 1
    return sumV


def odd_bfs(g_num, bfs_visited):
    x, y, cnt = gates[g_num][0], gates[g_num][1], 1
    sumV = 0
    if not bfs_visited[x]:
        bfs_visited[x] = 1
        sumV += 1
        y -= 1

    while y:
        for d_x in (cnt, -cnt):
            n_x = x + d_x

            if 1 <= n_x <= N and not bfs_visited[n_x]:
                bfs_visited[n_x] = cnt + 1
                sumV += cnt + 1
                y -= 1

            if y == 0:
                break
        cnt += 1
    return sumV


def dfs(v, p):
    global minV

    if v == 3:
        bfs_visited = [0] * (N + 1)
        s = 0
        for gate, check in visited:
            if check:
                s += odd_bfs(gate, bfs_visited)
            else:
                s += even_bfs(gate, bfs_visited)

        if minV > s:
            minV = s

    else:
        for idx in range(3):
            if visited[idx] == -1:

                if gates[v][1] % 2 == 0:
                    visited[idx] = (v, 0)
                    dfs(v + 1, 0)
                    visited[idx] = -1

                visited[idx] = (v, 1)
                dfs(v + 1, 1)
                visited[idx] = -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    visited = [-1] * 3

    minV = 1000000

    gates = [list(map(int, input().split())) for _ in range(3)]

    dfs(0, 1)

    print(f'#{tc} {minV}')