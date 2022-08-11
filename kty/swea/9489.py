import sys

sys.stdin = open("input_9489.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N): # 행 계산
        cnt = 0
        for j in range(M):
            if num[i][j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    for j in range(M): # 열 계산
        cnt = 0
        for i in range(N):
            if num[i][j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')

