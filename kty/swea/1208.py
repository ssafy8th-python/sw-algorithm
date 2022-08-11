import sys

sys.stdin = open("input_flatten.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    while N > 0:
        maxV = 0
        minV = 101
        for j in range(len(num)):
            if num[j] > maxV:
                maxV = num[j]
                p = j
            if num[j] < minV:
                minV = num[j]
                q = j
        num[p] -= 1
        num[q] += 1
        N -= 1

    maxV = 0
    minV = 101
    for k in range(len(num)):
        if num[k] > maxV:
            maxV = num[k]
        if num[k] < minV:
            minV = num[k]

    print(f'#{tc} {maxV - minV}')