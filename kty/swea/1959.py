import sys

sys.stdin = open("input_1959.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if N > M:
        a, b = b, a
        N, M = M, N

    maxV = 0
    i = 0
    while N + i <= M:
        sum = 0
        for idx in range(N):
            sum += a[idx] * b[idx+i]
        if maxV < sum:
            maxV = sum
        i += 1

    print(f'#{tc} {maxV}')


