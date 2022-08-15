# 1929 소수 구하
# 주소: https://www.acmicpc.net/problem/1929

# 제출한 답
primes = [False] * 2 + [True] * 999999

m, n = map(int, input().split())

for i in range(2, n + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

for k in range(m, n + 1):
    if primes[k] == True:
        print(k)