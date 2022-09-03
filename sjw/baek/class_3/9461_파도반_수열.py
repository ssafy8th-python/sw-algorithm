# 9461 파도반 수열
# 주소: https://www.acmicpc.net/problem/9461

# 제출한 답
import sys
input = sys.stdin.readline


def pado(k):
    if pado_tri[k]:
        return pado_tri[k]
    else:
        pado_tri[k] = pado(k - 1) + pado(k - 5)
        return pado_tri[k]


t = int(input())

pado_tri = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12] + [0] * 89

for _ in range(t):
    n = int(input())

    print(pado(n))
