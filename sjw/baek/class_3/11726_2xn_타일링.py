# 11726 2xn 타일링
# 주소: https://www.acmicpc.net/problem/11726

# 제출한 답
import sys
input = sys.stdin.readline


def square(k):
    if memo[k]:
        return memo[k]
    else:
        memo[k] = square(k - 1) + square(k - 2)
        return memo[k]


n = int(input())
memo = [0] * 1001
memo[1] = 1
memo[2] = 2

print(square(n) % 10007)
