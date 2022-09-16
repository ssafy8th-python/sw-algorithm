from collections import deque

T = int(input())

costs = [0] * 41

for k in range(1, 41):
    costs[k] = k * k + (k - 1) * (k - 1)


def bfs(x, y):
    visited = [[False] * N for _ in range(N)]

    visited[x][y] = True
    house = 0
    result = 0

    cur_num = 2

    if city[x][y] == '1':
        house += 1
        result += 1

    q = deque()
    q.append((x, y, 1))

    while q:
        c_i, c_j, k= q.popleft()

        if cur_num == k:
            cur_num += 1
            if costs[cur_num - 1] <= house * M:
                result = house

        for d_i, d_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_i, n_j = c_i + d_i, c_j + d_j
            if 0 <= n_i < N and 0 <= n_j < N and not visited[n_i][n_j]:
                if city[n_i][n_j] == '1':
                    house += 1

                q.append((n_i, n_j, k+1))
                visited[n_i][n_j] = True

    return result


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    city = [input().split() for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(N):
            result = bfs(i, j)

            if answer < result:
                answer = result

    print(f'#{test_case} {answer}')
