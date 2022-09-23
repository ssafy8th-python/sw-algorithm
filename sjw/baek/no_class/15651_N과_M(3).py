# 15651 N과 M(3)
# 주소: https://www.acmicpc.net/problem/15651

# 제출한 답
import sys
input = sys.stdin.readline


def com(d):
    if d == M:
        print(*c)
    else:
        for i in range(N):
            c[d] = lst[i]
            com(d + 1)


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
c = [0] * M
com(0)
