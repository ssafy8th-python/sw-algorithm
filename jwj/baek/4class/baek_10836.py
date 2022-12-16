import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bee = [[1] * N for _ in range(N)]

for _ in range(M):
    growth = list(map(int, input().split()))

    x = N - 1
    y = 1

    for i in range(3):
        for _ in range(growth[i]):
            if i:
                if x != -1:
                    bee[x][0] += i
                    x -= 1
                else:
                    bee[0][y] += i
                    y += 1
            else:
                if x != -1:
                    x -= 1
                else:
                    y += 1

    for i in range(1, N):

        # 아래 방향으로 확인
        n_y = [i, i - 1, i - 1]
        for j in range(i, N):
            for index, tx in enumerate((-1, -1, 0)):
                n_x = tx + j
                bee[j][i] = max(bee[j][i], bee[n_x][n_y[index]])

        # 오른쪽 방향으로 확인
        n_x = [i - 1, i - 1, i]
        for j in range(i, N):
            for index, ty in enumerate((0, -1, -1)):
                n_y = ty + j
                bee[i][j] = max(bee[i][j], bee[n_x[index]][n_y])


for b in bee:
    print(*b)
