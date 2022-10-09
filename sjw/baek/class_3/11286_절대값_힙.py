# 11286 절댓값 힙
# 주소: https://www.acmicpc.net/problem/11286

# 제출한 답
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, (abs(x), x))
    elif heap and not x:
        print(heappop(heap)[1])
    else:
        print(0)