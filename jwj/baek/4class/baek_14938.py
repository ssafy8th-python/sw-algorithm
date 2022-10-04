import sys
input = sys.stdin.readline


def floyd():
    # 거쳐 가는 곳
    for k in range(1, n+1):
        # 시작 노드
        for i in range(1, n+1):
            # 끝 노드
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])



INF = 10000

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items = [0] + items

distance = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    distance[a][b] = l
    distance[b][a] = l

floyd()
result = 0

for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if distance[i][j] <= m:
            tmp += items[j]
    if result < tmp:
        result = tmp

print(result)
