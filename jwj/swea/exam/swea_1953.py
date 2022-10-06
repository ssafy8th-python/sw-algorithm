from collections import deque

shape = [[], [(1, 0), (-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(1, 0), (0, -1)],
         [(-1, 0), (0, -1)], [(0, 1), (-1, 0)], [(1, 0), (0, 1)]]

m_shape = [[], [(1, 0), (-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(-1, 0), (0, 1)],
         [(1, 0), (0, 1)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]]

T = int(input())

for test_case in range(1, T+1):

    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 1

    visited = [[0] * M for _ in range(N)]

    visited[R][C] = 1
    q = deque()
    q.append((R, C, 0))

    while q:
        r, c, cnt = q.popleft()

        if cnt == L - 1:
            continue

        for d_r, d_c in m_shape[arr[r][c]]:
            n_r = r + d_r
            n_c = c + d_c
            if 0 <= n_r < N and 0 <= n_c < M and not visited[n_r][n_c]:
                for p_r, p_c in shape[arr[n_r][n_c]]:
                    if d_r == p_r and d_c == p_c:
                        q.append((n_r, n_c, cnt+1))
                        visited[n_r][n_c] = visited[r][c] + 1
                        result += 1

    print(f'#{test_case} {result}')
