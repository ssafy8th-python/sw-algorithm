import sys

sys.stdin = open("input_4835.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = list(map(int, input().split()))

    maxV = 0
    minV = 1000000
    for i in range(N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += num[j]
        if sum > maxV:
            maxV = sum
        if sum < minV:
            minV = sum
    print(f'#{tc} {maxV-minV}')
