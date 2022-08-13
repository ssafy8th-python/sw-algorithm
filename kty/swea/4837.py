import sys

sys.stdin = open("input_4837.txt", "r")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
L = len(A)

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    num = 0
    for i in range(1<<L):
        cnt = 0
        value = 0
        for j in range(L):
            if i & (1<<j):
                cnt += 1
                value += A[j]
        if cnt == N and value == K:
            num += 1

    print(f'#{tc} {num}')

