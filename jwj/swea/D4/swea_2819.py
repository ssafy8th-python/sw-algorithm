from collections import deque

T = int(input())

for test_case in range(1, T+1):
    arr = [input().split() for _ in range(4)]

    result = set()

    q = deque()
    for i in range(4):
        for j in range(4):
            q.append((i, j, arr[i][j], 1))

    result_set = set()

    while q:
        r, c, s, cnt = q.popleft()

        if (r, c, s) in result:
            continue
        else:
            result.add((r, c, s))

        if cnt == 7:
            result_set.add(s)
            continue

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = r + d_x
            n_y = c + d_y

            if 0 <= n_x < 4 and 0 <= n_y < 4:
                q.append((n_x, n_y, s + arr[n_x][n_y], cnt+1))

    print(f'#{test_case} {len(result_set)}')
