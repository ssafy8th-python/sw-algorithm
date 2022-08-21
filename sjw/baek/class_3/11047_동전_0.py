# 11047 동전 0
# 주소: https://www.acmicpc.net/problem/11047

# 제출한 답
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0

for coin in coins[::-1]:
    result += k // coin
    k %= coin

print(result)
