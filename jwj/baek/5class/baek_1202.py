import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())    # 보석, 가방

jewelry = []
bags = []

for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, (m, v))

for _ in range(K):
    c = int(input())
    bags.append(c)
bags.sort()

result = 0

tmp_jew = []
for bag in bags:
    # 가방에 들어갈 수 있는 쥬얼리 확인
    while jewelry and bag >= jewelry[0][0]:
        # 가치를 내림차순으로 임시 list에 추가
        heapq.heappush(tmp_jew, -heapq.heappop(jewelry)[1])

    if tmp_jew:
        result -= heapq.heappop(tmp_jew)
    elif not jewelry:
        break


print(result)