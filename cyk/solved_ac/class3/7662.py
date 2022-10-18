# 다시풀기
'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    heap = []
    heap2 = []
    check = [False]*k
    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heappush(heap, (num, i))
            heappush(heap2, (-num, i))
            check[i] = True
        else:
            if num == 1:
                while heap2 and not check[heap2[0][1]]:
                    heappop(heap2)
                if heap2:
                    check[heap2[0][1]] = False
                    heappop(heap2)
            else:
                while heap and not check[heap[0][1]]:
                    heappop(heap)
                if heap:
                    check[heap[0][1]] = False
                    heappop(heap)


    while heap and not check[heap[0][1]]:
        heappop(heap)

    while heap2 and not check[heap2[0][1]]:
        heappop(heap2)

    if not heap or not heap2:
        print("EMPTY")
    else:
        print(-heap2[0][0], heap[0][0])