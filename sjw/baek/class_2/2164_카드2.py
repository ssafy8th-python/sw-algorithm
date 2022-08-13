# 2164 카드2
# 주소: https://www.acmicpc.net/problem/2164

# 제출한 답
# 큐에 대해 공부 후에 풀 것

import sys
input = sys.stdin.readline

N = int(input())

if N % 2:
    M = [i for i in range(2, N - 2, 2)]
    N = [N - 1] + M
else:
    N = [i for i in range(2, N + 1, 2)]

while len(N) != 1:
    N.remove(N[0])
    N.append(N.pop(0))
print(N[0])

