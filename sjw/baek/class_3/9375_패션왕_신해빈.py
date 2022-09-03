# 9375 패션왕 신해빈
# 주소: https://www.acmicpc.net/problem/9375

# 제출한 답
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    c_lst = dict()
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if b in c_lst:
            c_lst[b] += 1
        else:
            c_lst[b] = 1
    c_lst = list(c_lst.values())
    result = 1
    for i in c_lst:
        result *= (i + 1)
    print(result - 1)
