import sys

sys.stdin = open("input_12712.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    BRD = [list(map(int, input().split())) for _ in range(N)]

    # print(BRD)
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    maxV = 0
    for row in range(N):
        for col in range(N):
            # 사방면
            sumV = BRD[row][col]
            for direction in range(4, 8):
                for distance in range(1, M):
                    newR = row + dr[direction] * distance
                    newC = col + dc[direction] * distance

                    if 0<=newR<N and 0<=newC<N:
                        sumV += BRD[newR][newC]
            if maxV < sumV:
                maxV = sumV
                # print('1', row, col, sumV)

            # 대각선 확인
            sumV = BRD[row][col]
            for direction in range(4, 8):
                for distance in range(1, M):
                    newR = row + dr[direction] * distance
                    newC = col + dc[direction] * distance

                    if 0<=newR<N and 0<=newC<N:
                        sumV += BRD[newR][newC]

            if maxV < sumV:
                maxV = sumV
                # print('2, row, col, sumV)
    print(f'#{tc} {maxV}')