# 1003 피보나치 함수
# 주소: https://www.acmicpc.net/problem/1003

# 제출한 답
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    result = [(1, 0), (0, 1)]
    n = int(input())
    for i in range(2, n + 1):
        result.append((result[i - 1][0] + result[i - 2][0], result[i - 1][1] + result[i - 2][1]))

    print(*result[n])
