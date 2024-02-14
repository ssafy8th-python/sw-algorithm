# 2559 수열
# 주소: https://www.acmicpc.net/problem/2559

# 제출한 답
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_lst = list(map(int, input().split()))

maxV = sum(n_lst[:k])
sumV = sum(n_lst[:k])
for i in range(k, n):
    sumV = sumV - n_lst[i - k] + n_lst[i]
    maxV = max(maxV, sumV)

print(maxV)
