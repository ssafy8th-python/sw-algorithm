import sys
input = sys.stdin.readline

N, K = map(int, input().split())

box = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

virus = [[] for _ in range(K+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if box[i][j]:
            virus[box[i][j]].append((i, j))


for _ in range(S):
    tmp_virus = [[] for _ in range(K+1)]

    for index in range(1, K + 1):
        for x, y in virus[index]:
            for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0,  -1)):
                n_x = x + d_x
                n_y = y + d_y
                if 0 < n_x <= N and 0 < n_y <= N and not box[n_x][n_y]:
                    box[n_x][n_y] = index
                    tmp_virus[index].append((n_x, n_y))

    virus = tmp_virus

print(box[X][Y])

