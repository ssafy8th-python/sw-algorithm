T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]

    sumV = 0

    for idx in range(0, N//2):
        for i in range(N//2 - idx, N//2 + idx + 1):
            sumV += farm[i][idx]

    for i in range(N):
        sumV += farm[i][N//2]

    col = 0
    for idx in range(N//2 + 1, N):
        for i in range(1+col, N-col-1):
            sumV += farm[i][idx]
        col += 1

    print(f'#{tc} {sumV}')


