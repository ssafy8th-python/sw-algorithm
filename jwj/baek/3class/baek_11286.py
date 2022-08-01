import heapq
import sys
minus_heap = []
plus_heap = []
result = []
for test_case in range(int(input())):
    x = int(sys.stdin.readline())

    if x == 0:
        if minus_heap and plus_heap:
            minus = abs(minus_heap[0][1])
            plus = abs(plus_heap[0])
            if minus > plus:
                print(heapq.heappop(plus_heap))
            else:
                print(heapq.heappop(minus_heap)[1])
        elif minus_heap:
            print(heapq.heappop(minus_heap)[1])
        elif plus_heap:
            print(heapq.heappop(plus_heap))
        else:
            print(0)
    else :
        if x > 0:
            heapq.heappush(plus_heap, x)    # 오름차순 
        else :
            heapq.heappush(minus_heap, (-x, x)) # 내림차순  (우선순위, 값) 1, 2, 3, 4

