# 절댓값 힙
import sys, heapq

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x < 0:   # 음수일 때
        heapq.heappush(heap,(-x,x))
    elif x > 0 :
        heapq.heappush(heap,(x,x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)