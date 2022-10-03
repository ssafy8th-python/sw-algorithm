# 7662 이중 우선순위 큐
# 주소: https://www.acmicpc.net/problem/7662

# 제출한 답
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    k = int(input())
    heap_s = []  # 최소 힙 저장
    heap_l = []  # 최대 힙 저장
    visited = [0] * 1_000_001  # 최소 힙과 최대 힙의 동기화를 위한 방문 표시
    length, idx = 0, 0  # 힙의 크기, 방문 표시를 위한 인덱스
    for _ in range(k):
        order, num = input().rstrip().split()
        if order == 'I':
            num = int(num)
            heappush(heap_s, (num, idx))  # 최소힙에 수와 인덱스 저장
            heappush(heap_l, (-num, idx))  # 최대힙에 수와 인덱스 저장
            length += 1
            idx += 1
        elif length:
            if num == '1':
                while True:  # 동기화를 위한 과정 이미 방문한 노드를 전부 날린 후 마지막 안 방문한 노드를 pop한 뒤 방문 표시
                    tmp = heappop(heap_l)
                    if not visited[tmp[1]]:
                        visited[tmp[1]] = 1
                        break
            else:
                while True:
                    tmp = heappop(heap_s)
                    if not visited[tmp[1]]:
                        visited[tmp[1]] = 1
                        break
            length -= 1

    if length:
        # 이미 방문한 노드를 제거한 최대값과 최소값을 찾는 과정
        large, small = 0, 0
        while True:
            tmp = heappop(heap_l)
            if not visited[tmp[1]]:
                large = -tmp[0]
                break
        while True:
            tmp = heappop(heap_s)
            if not visited[tmp[1]]:
                small = tmp[0]
                break
        print(large, small)
    else:
        print('EMPTY')


# 다른 답
import sys
import collections
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    exist = collections.defaultdict(int)

    def clear(heap, k=1):
        while heap and not exist[heap[0] * k]:
            heapq.heappop(heap)

    # execute the commands.
    for _ in range(int(input())):
        command = input().split()
        # I n
        if command[0] == 'I':
            n = int(command[1])
            if not exist[n]:
                heapq.heappush(min_heap, n)
                heapq.heappush(max_heap, -n)
            exist[n] += 1
        # D -1
        elif command[1] == '-1':
            clear(min_heap)
            if not min_heap:
                continue
            exist[min_heap[0]] -= 1
            if not exist[min_heap[0]]:
                heapq.heappop(min_heap)
        # D 1
        else:
            clear(max_heap, -1)
            if not max_heap:
                continue
            exist[-max_heap[0]] -= 1
            if not exist[-max_heap[0]]:
                heapq.heappop(max_heap)

    clear(min_heap)
    clear(max_heap, -1)

    # print the result.
    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')
