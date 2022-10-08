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
