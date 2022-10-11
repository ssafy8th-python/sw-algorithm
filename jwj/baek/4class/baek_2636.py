from collections import deque


def air():
    q = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    cnt = 0
    while q:
        x, y = q.popleft()

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = x + d_x
            n_y = y + d_y
            if 0 <= n_x < N and 0 <= n_y < M and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                if cheese[n_x][n_y] == '1':
                    cnt += 1
                    cheese[n_x][n_y] = '0'
                else:
                    q.append((n_x, n_y))

    if cnt:
        return cnt
    else:
        return cnt


N, M = map(int, input().split())
cheese = [list(input().split()) for _ in range(N)]
res1 = 0
res2 = 0
while True:
    c = air()
    if c:
        res1 += 1
        res2 = c
    else:
        break

print(res1)
print(res2)
