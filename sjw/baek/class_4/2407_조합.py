# 2407 조합
# 주소: https://www.acmicpc.net/problem/2407

# 제출한 답
# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

a, b = 1, 1
while m > 0:
    a *= n
    n -= 1
    b *= m
    m -= 1

print(a // b)
