# 11399 ATM
# 주소: https://www.acmicpc.net/problem/11399

# 제출한 답
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# lst = list(map(int, input().split()))
#
# lst.sort()
#
# result = 0
# for i in range(n):
#     for j in range(i + 1):
#         result += lst[j]
#
# print(result)

import sys
input = sys.stdin.readline


def atm(n):
    if n == 1:
        return lst[0]
    else:
        return atm(n - 1) + atm(n - 2)


N = int(input())
lst = list(map(int, input().split()))

lst.sort()

print(atm(N))
