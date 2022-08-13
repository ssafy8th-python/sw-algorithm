import sys

sys.stdin = open("input_2001.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    sum += lst[a][b]
            if sum > maxV:
                maxV = sum

    print(f'#{tc} {maxV}')


