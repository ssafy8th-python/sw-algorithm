# 간단한 소인수분해

import sys
sys.stdin = open("input (3).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prime = [0] * 5 # 2, 3, 5, 7, 11

    while True:

        if N % 2 == 0:
            prime[0] += 1
            N = N // 2

        elif N % 3 == 0:
            prime[1] += 1
            N = N // 3

        elif N % 5 == 0:
            prime[2] += 1
            N = N // 5

        elif N % 7 == 0:
            prime[3] += 1
            N = N // 7

        elif N % 11 == 0:
            prime[4] += 1
            N = N // 11
        else:
            print(f'#{tc} ',end='')
            print(*prime)
            break