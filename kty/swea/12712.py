import sys

sys.stdin = open("input_12712.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0~3 : 오, 아, 왼, 위 , 4~7 : 오위, 오아, 왼아, 왼위
    dr = [0, 1, 0, -1, -1, 1, 1, -1]
    dc = [1, 0, -1, 0, 1, 1, -1, -1]

    max_flies = 0
    for i in range(N):
        for j in range(N):
            sum = arr[i][j] # 중앙값 초기화
            for k in range(0, 4): # 상하좌우 확인
                for d in range(1, M): # M의 범위만큼 스프레이 길이 늘어남
                    ni = i + dr[k] * d
                    nj = j + dc[k] * d
                    if 0 <= ni < N and 0 <= nj < N:
                        sum += arr[ni][nj]

            if max_flies < sum:
                max_flies = sum

            # 대각선 확인
            sum = arr[i][j] # 중앙값 초기화
            for k in range(4, 8):
                for d in range(1, M):
                    ni = i + dr[k] * d
                    nj = j + dc[k] * d
                    if 0 <= ni < N and 0 <= nj < N:
                        sum += arr[ni][nj]

            if max_flies < sum:
                max_flies = sum

    print(f'#{tc} {max_flies}')