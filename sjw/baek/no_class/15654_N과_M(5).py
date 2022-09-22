# 15654 N과 M(5)
# 주소: https://www.acmicpc.net/problem/15654

# 제출한 답
import sys
input = sys.stdin.readline

def per(d, n, r):
    if d == r:
        for i in p:
            print(n_lst[i], end=' ')
        print()
    else:
        for i in range(n):
            if not check[i]:
                check[i] = 1
                p[d] = lst[i]
                per(d + 1, n, r)
                check[i] = 0


N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))
lst = [i for i in range(N)]
check = [0] * N
p = [0] * M
per(0, N, M)