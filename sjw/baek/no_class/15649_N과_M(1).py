# 15649 N과 M(1)
# 주소: https://www.acmicpc.net/problem/15649

# 제출한 답
import sys
input = sys.stdin.readline

def per(d, n, r):
    if d == r:
        print(*p)
    else:
        for i in range(n):
            if not check[i]:
                check[i] = 1
                p[d] = lst[i]
                per(d + 1, n, r)
                check[i] = 0


N, M = map(int, input().split())

lst = [i for i in range(1, N + 1)]
check = [0] * N
p = [0] * M
per(0, N, M)