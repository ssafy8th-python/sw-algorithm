# 15652 N과 M(4)
# 주소: https://www.acmicpc.net/problem/15652

# 제출한 답
import sys
input = sys.stdin.readline


def com(d, n):
    if d == M:
        print(*c)
    else:
        for i in range(N):
            if i >= n:
                c[d] = lst[i]
                com(d + 1, i)


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
c = [0] * M
com(0, 0)
