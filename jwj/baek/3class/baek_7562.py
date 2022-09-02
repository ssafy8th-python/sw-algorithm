from collections import deque


T = int(input())

for tc in range(1, T+1):
    size = int(input())
    x, y = map(int, input().split())
    end = list(map(int, input().split()))

    chess = [[0] * size for _ in range(size)]

    chess[x][y] = 1
    chess[end[0]][end[1]] = 2

    q = deque()

    q.append((x, y, 0))

    check = False
    while q:
        s_x, s_y, cnt = q.popleft()

        if chess[s_x][s_y] == 2:
            break
        

        for d_x, d_y in ((-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)):
            n_x, n_y = s_x + d_x, s_y + d_y

            if 0 <= n_x < size and 0 <= n_y < size and chess[n_x][n_y] != 1:
                if chess[n_x][n_y] == 2:
                    check = True
                    cnt += 1
                    break
                chess[n_x][n_y] = 1

                q.append((n_x, n_y, cnt + 1))

        if check:
            break

    print(cnt)