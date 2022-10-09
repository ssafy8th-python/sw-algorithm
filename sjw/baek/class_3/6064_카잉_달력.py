# 6064 카잉 달력
# 주소: https://www.acmicpc.net/problem/6064

# 제출한 답
import sys
input = sys.stdin.readline


def cain(m, n, x, y):         # 답이 되는 경우는 x에 m을 더한 경우랑 y에 n을 더한 경우가 같아질 때이다
    while x <= m * n:         # 최소공배수보다 작은 동안
        if (x - y) % n == 0:  # x에서 y를 뺀값이 n의 배수라면
            return x          # x가 답
        x += m
    return -1                 # 아니라면 없음


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    print(cain(m, n, x, y))


# 다른 답
import sys;

R = sys.stdin.readline
from math import gcd


def euc(a, b, c):
    if not a:
        return 0, c // b
    if not b:
        return c // a, 0
    if a < b:
        q, r = divmod(b, a)
        s, t = euc(a, r, c)
        return s - t * q, t
    q, r = divmod(a, b)
    s, t = euc(r, b, c)
    return s, t - s * q


for _ in range(int(R())):
    m, n, x, y = map(int, R().split())
    g = gcd(m, n)
    if (y - x) % g:
        print(-1)
        continue
    p, q = euc(m, n, y - x)
    print(p % (n // g) * m + x)