# 2164 카드2
# 주소: https://www.acmicpc.net/problem/2164

# 제출한 답
# 큐에 대해 공부 후에 풀 것

import sys
from collections import deque
input = sys.stdin.readline


N = deque(list(i for i in range(1, int(input()) + 1)))

cnt = 1
while len(N) > 1:
        N.popleft()
        N.append(N.popleft())

print(N[0])
